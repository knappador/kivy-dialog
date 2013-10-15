from kivy import platform

__all__ = ('Dialog')

if platform() == 'android':
    from androiddialog import AndroidDialog as Dialog
else:
    from kivydialog import KivyDialog as Dialog
