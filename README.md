kivy-dialog
=============

[Android Dialogs.](http://developer.android.com/guide/topics/ui/dialogs.html)  Frequently you need to ask the user to do something and execute some function with a Yes/No value.  The dialog module implements this API and can use native Android dialogs that have the user's Android theme and are familiar.

![dialog](http://developer.android.com/images/ui/dialogs.png "Android dialogs")

#### Install
Pre-built application in ```/bin```.  Install with:
```adb install -r /bin/Dialog-Example-0.1-debug-unaligned.apk```

#### Build
Copy the netcheck.sh to a P4A dist then run:
```dialog.sh my/path/to/app/```
If it doesn't work, edit dialog.sh to configure P4A to build this.  Need PyJNIus in your dist. 

#### Emulation in Kivy for Development
```python ./dialog/src/main.py``` Implemented with kv and popup instead.

#### Docs
Public API.
