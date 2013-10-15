from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

from dialog import Dialog

class DialogUI(BoxLayout):
    yesno = StringProperty('might do')
    
    def ask_user(self):
        d = Dialog(callback=self.set_yesno,
                   text='Just do it?',
                   action_name='Do It',
                   title = 'This is a Dialog')
        app.dialog = d
        d.bind(on_dismiss=app.clear_dialog)
        d.open()
    
    def set_yesno(self, yesno):
        self.yesno = 'did' if yesno else 'didn\'t do'


class DialogApp(App):
    def __init__(self, *args, **kwargs):
        super(DialogApp, self).__init__(*args, **kwargs)
        global app
        app = self

    def build(self):
        return DialogUI()

    def on_key_down(self, key, keycode, scancode):
        #Logger.info('key_info' + str([key, keycode, scancode]))
        if key == 4:
            if getattr(app, 'dialog', None):
                app.dialog.dismiss()
                return True
        #if key == 82:
        #    ctl.load_state('options')
        #    return True

    def clear_dialog(self, *args):
        self.dialog = None


if __name__ == '__main__':
    DialogApp().run()
