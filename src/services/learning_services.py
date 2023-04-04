from UI.ui import (MyFrame2, LogininDialog, NewQDialog, NewUserDialog)
from entities.user import User
from repository.user_repository import user_repo

import wx

class MainClass(MyFrame2):
    def __init__(self):
        MyFrame2.__init__(self, None)

        self.onlogin()
        
    def onlogin(self):
        with Login() as log_in:
            if log_in.ShowModal() == wx.ID_OK:
                credentials = log_in.GetCredentials()
                if user_repo.find_one_user(User(credentials[0], credentials[1])):
                    pass
                else:
                    wx.MessageDialog(None, 'The username or password is incorrect!')
            

class Login(LogininDialog):
    def __init__(self):
        LogininDialog.__init__(self, None)

    def GetCredentials(self) -> tuple:
        username = self.UsernameTC1.GetValue()
        password = self.PasswordTC1.GetValue()
        return (username, password)
    
    def OnSignUp(self, event):
        with NewUser() as newuser:
            if newuser.ShowModal() == wx.ID_OK:
                new_info = newuser.GetCredentials()
                try:
                    user_repo.new_user(User(new_info[0], new_info[1]))
                except:
                    wx.MessageDialog(None, 'Username already exists!')
                    self.OnSignUp(wx.EVT_BUTTON)

            elif newuser.ShowModal() == wx.ID_CANCEL:
                newuser.Destroy()
        
class NewUser(NewUserDialog):
    def __init__(self):
        NewUserDialog.__init__(self, None)

    def GetCredentials(self):
        username = self.UsernameTC.GetValue()
        password1 = self.FrstPasswordTC.GetValue()
        password2 = self.ScndPasswordTC.GetValue()
        if password1 != password2:
            wx.MessageDialog(None, '''The two password don't match''').ShowModal()
            return
        if len(password1) < 3:
            wx.MessageDialog(None, 'The password has to longer than 3 characters').ShowModal()
            return
        return (username, password1)
        