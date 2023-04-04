import wx
from services.learning_services import MainClass
from UI.ui import MyFrame2

def start():
    app = wx.App()
    frame = MainClass()
    frame.Show()
    app.MainLoop()

if __name__=='__main__':
    start()
