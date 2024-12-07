from .StatusBar import StatusBar

from fabric import Application

statusBar = StatusBar()
app = Application("StatusBar", statusBar)
app.run()
