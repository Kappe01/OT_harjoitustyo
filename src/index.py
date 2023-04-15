import wx
from services.learning_services import MainClass


def start():
    app = wx.App()
    frame = MainClass()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    start()
