from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from kivy.logger import Logger

DIALOG_CONTENT_KV='''
<DialogContent@RelativeLayout>:
    Label:
        text_size: (self.width, self.height)
        # font sizes based on avg of height and width
        font_size: (self.width + self.height) / 2.0 * 0.07
        text: root.text
        size_hint: (0.9, 0.6)
        pos_hint: {'x' : 0.05, 'y' : 0.475}
        text_size: self.size
    Button:
        text: root.action_name
        size_hint: (0.425, 0.3)
        pos_hint: {'x' : 0.525, 'y': 0.025}
        on_press: root.answer(True)
        font_size: self.height * 0.34
    Button:
        text: 'Cancel'
        size_hint: (0.425, 0.3)
        pos_hint: {'x' : 0.05, 'y': 0.025}
        on_press: root.answer(False)
        font_size: self.height * 0.34
'''

Builder.load_string(DIALOG_CONTENT_KV)

class DialogContent(RelativeLayout):
    ''' Callback(bool) if user wants to do something'''
    action_name = StringProperty()
    cancel_name = StringProperty()
    text = StringProperty()
    
    def __init__(self, 
                 answer,
                 action_name='Okay', 
                 cancel_name='Cancel', 
                 text='Are you Sure?',
                 *args, **kwargs):
        self.action_name = action_name
        self.cancel_name = cancel_name
        self.answer = answer
        self.text = text
        super(DialogContent, self).__init__(*args, **kwargs)


class KivyDialog(Popup):
    def __init__(self, callback, **kwargs):
        self.content = DialogContent(answer=self.answer, **kwargs)
        self.callback = callback
        defaults = {'size_hint' : (0.8, 0.4),
                    'pos_hint' : {'x':0.1, 'y': 0.35}}
        defaults.update(kwargs)
        kwargs = defaults
        super(KivyDialog, self).__init__(**kwargs)

    def answer(self, yesno):
        ''' Callbacks in prompts that open prompts lead to errant clicks'''
        self.dismiss()
        Clock.schedule_once(lambda dt: self.callback(yesno), 1/30.0)
