from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.logger import Logger

from functools import partial

from jnius import autoclass, PythonJavaClass, java_method, cast
from android import activity
from android.runnable import run_on_ui_thread

Builder = autoclass('android.app.AlertDialog$Builder')
DialogFragment = autoclass('android.support.v4.app.DialogFragment')
String = autoclass('java.lang.String')
context = autoclass('org.renpy.android.PythonActivity').mActivity    


class _OnClickListener(PythonJavaClass):
    __javainterfaces__ = ['android.content.DialogInterface$OnClickListener',]
    __javacontext__ = 'app'

    def __init__(self, action):
        self.action = action
        super(_OnClickListener, self).__init__()
        
    @java_method('(Landroid/content/DialogInterface;I)V')
    def onClick(self, dialog, which):
        self.action()

class AndroidDialog(EventDispatcher):

    __events__ = ('on_dismiss',)

    def __init__(self, 
                 callback, 
                 action_name = 'okay',
                 cancel_name = 'cancel',
                 text = 'Are you sure?',
                 title = 'Alert!',
                 **kwargs):
        self.callback = callback if callback else lambda *args: None
        self.title = title
        self.text = text
        self.action_name = action_name
        self.cancel_name = cancel_name

    def answer(self, yesno):
        ''' Callbacks in prompts that open prompts lead to errant clicks'''
        #Clock.schedule_once(lambda dt: self.callback(yesno), 1/30.0)
        self.callback(yesno)

    @run_on_ui_thread
    def open(self):
        ''' using dialog builder.  simplest way'''
        builder = self.builder = Builder(
            cast('android.app.Activity', context))
        builder.setMessage(String(self.text))
        builder.setTitle(String(self.title))
        self.positive = _OnClickListener(partial(self.answer, True))
        self.negative = _OnClickListener(partial(self.answer, False))
        builder.setPositiveButton(String(self.action_name),
                                  self.positive)
        builder.setNegativeButton(String(self.cancel_name),
                                  self.negative)
        self.dialog = builder.create()
        self.dialog.show()

    def dismiss(self):
        self.dispatch('on_dismiss')

    def on_dismiss(self):
        # guessing fragment activity will get back button
        # instead of app like my usual setup
        pass
        
