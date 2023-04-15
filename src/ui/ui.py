# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Feb  6 2018)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
# Class MyFrame2
###########################################################################


class MyFrame2 (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            500, 401), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer47 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook2 = wx.Notebook(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.HomePanel = wx.Panel(
            self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer56 = wx.BoxSizer(wx.VERTICAL)

        self.AppNameST = wx.StaticText(
            self.HomePanel, wx.ID_ANY, u"Learning App", wx.DefaultPosition, wx.DefaultSize, 0)
        self.AppNameST.Wrap(-1)
        self.AppNameST.SetFont(wx.Font(
            20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        bSizer56.Add(self.AppNameST, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.TopicST = wx.StaticText(
            self.HomePanel, wx.ID_ANY, u"Choose topics to start learning:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.TopicST.Wrap(-1)
        bSizer56.Add(self.TopicST, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        SubjectsCheckListBoxChoices = [u"Maths", u"Physics", u"Programming"]
        self.SubjectsCheckListBox = wx.CheckListBox(
            self.HomePanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, SubjectsCheckListBoxChoices, 0)
        bSizer56.Add(self.SubjectsCheckListBox, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer86 = wx.StaticBoxSizer(wx.StaticBox(
            self.HomePanel, wx.ID_ANY, wx.EmptyString), wx.HORIZONTAL)

        gSizer73 = wx.GridSizer(1, 2, 0, 0)

        self.QAmountST = wx.StaticText(sbSizer86.GetStaticBox(
        ), wx.ID_ANY, u"Question amount:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.QAmountST.Wrap(-1)
        gSizer73.Add(self.QAmountST, 0, wx.ALL |
                     wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.m_spinCtrl1 = wx.SpinCtrl(sbSizer86.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS | wx.SP_WRAP, 1, 10, 1)
        gSizer73.Add(self.m_spinCtrl1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer86.Add(gSizer73, 1, wx.EXPAND, 5)

        bSizer56.Add(sbSizer86, 0, wx.EXPAND, 5)

        self.StartBtn = wx.Button(
            self.HomePanel, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer56.Add(self.StartBtn, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.HomePanel.SetSizer(bSizer56)
        self.HomePanel.Layout()
        bSizer56.Fit(self.HomePanel)
        self.m_notebook2.AddPage(self.HomePanel, u"Home", True)
        self.ResultPanel = wx.Panel(
            self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer55 = wx.BoxSizer(wx.VERTICAL)

        self.LatestResults = wx.StaticText(
            self.ResultPanel, wx.ID_ANY, u"Latest results:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.LatestResults.Wrap(-1)
        self.LatestResults.SetFont(wx.Font(
            15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        bSizer55.Add(self.LatestResults, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.ResultGrid = wx.grid.Grid(
            self.ResultPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.ResultGrid.CreateGrid(10, 3)
        self.ResultGrid.EnableEditing(True)
        self.ResultGrid.EnableGridLines(True)
        self.ResultGrid.EnableDragGridSize(False)
        self.ResultGrid.SetMargins(0, 0)

        # Columns
        self.ResultGrid.EnableDragColMove(False)
        self.ResultGrid.EnableDragColSize(True)
        self.ResultGrid.SetColLabelSize(30)
        self.ResultGrid.SetColLabelValue(0, u"Topic")
        self.ResultGrid.SetColLabelValue(1, u"Question")
        self.ResultGrid.SetColLabelValue(2, u"Result")
        self.ResultGrid.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.ResultGrid.EnableDragRowSize(True)
        self.ResultGrid.SetRowLabelSize(80)
        self.ResultGrid.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.ResultGrid.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer55.Add(self.ResultGrid, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.ResultPanel.SetSizer(bSizer55)
        self.ResultPanel.Layout()
        bSizer55.Fit(self.ResultPanel)
        self.m_notebook2.AddPage(self.ResultPanel, u"Results", False)
        self.SettingsPanel = wx.Panel(
            self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer54 = wx.BoxSizer(wx.VERTICAL)

        bSizer57 = wx.BoxSizer(wx.HORIZONTAL)

        self.LanguageST = wx.StaticText(
            self.SettingsPanel, wx.ID_ANY, u"Language:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.LanguageST.Wrap(-1)
        bSizer57.Add(self.LanguageST, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        LanguageRadioChoices = [u"Suomi", u"English"]
        self.LanguageRadio = wx.RadioBox(self.SettingsPanel, wx.ID_ANY, wx.EmptyString,
                                         wx.DefaultPosition, wx.DefaultSize, LanguageRadioChoices, 1, wx.RA_SPECIFY_ROWS)
        self.LanguageRadio.SetSelection(0)
        bSizer57.Add(self.LanguageRadio, 0, wx.ALL |
                     wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer54.Add(bSizer57, 0, wx.EXPAND, 5)

        self.HelpBtn = wx.Button(
            self.SettingsPanel, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer54.Add(self.HelpBtn, 0, wx.ALL, 5)

        bSizer59 = wx.BoxSizer(wx.HORIZONTAL)

        self.AddQST = wx.StaticText(
            self.SettingsPanel, wx.ID_ANY, u"Add a question:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.AddQST.Wrap(-1)
        bSizer59.Add(self.AddQST, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.AddQBtn = wx.Button(
            self.SettingsPanel, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer59.Add(self.AddQBtn, 0, wx.ALL, 5)

        bSizer54.Add(bSizer59, 0, wx.EXPAND, 5)

        self.SettingsPanel.SetSizer(bSizer54)
        self.SettingsPanel.Layout()
        bSizer54.Fit(self.SettingsPanel)
        self.m_notebook2.AddPage(self.SettingsPanel, u"Settings", False)

        bSizer47.Add(self.m_notebook2, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer47)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
# Class NewQDialog
###########################################################################

class NewQDialog (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"New question",
                           pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer60 = wx.BoxSizer(wx.VERTICAL)

        self.FillboxesST = wx.StaticText(
            self, wx.ID_ANY, u"Fill the boxes to add a new question", wx.DefaultPosition, wx.DefaultSize, 0)
        self.FillboxesST.Wrap(-1)
        bSizer60.Add(self.FillboxesST, 0, wx.ALL, 5)

        bSizer62 = wx.BoxSizer(wx.HORIZONTAL)

        sbSizer81 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"Topic"), wx.VERTICAL)

        m_choice23Choices = [u"Maths", u"Physics", u"Programming"]
        self.m_choice23 = wx.Choice(sbSizer81.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice23Choices, 0)
        self.m_choice23.SetSelection(0)
        sbSizer81.Add(self.m_choice23, 0, wx.ALL, 5)

        bSizer62.Add(sbSizer81, 0, wx.EXPAND, 5)

        sbSizer83 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"Question type"), wx.VERTICAL)

        m_choice24Choices = [u"Multiple choice", u"Single choice", u"Text"]
        self.m_choice24 = wx.Choice(sbSizer83.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice24Choices, 0)
        self.m_choice24.SetSelection(0)
        sbSizer83.Add(self.m_choice24, 0, wx.ALL, 5)

        bSizer62.Add(sbSizer83, 1, wx.EXPAND, 5)

        sbSizer84 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"Question"), wx.VERTICAL)

        self.m_textCtrl64 = wx.TextCtrl(sbSizer84.GetStaticBox(
        ), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer84.Add(self.m_textCtrl64, 0, wx.ALL, 5)

        bSizer62.Add(sbSizer84, 1, wx.EXPAND, 5)

        sbSizer85 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"Answer"), wx.VERTICAL)

        bSizer62.Add(sbSizer85, 1, wx.EXPAND, 5)

        bSizer60.Add(bSizer62, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer60)
        self.Layout()
        bSizer60.Fit(self)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
# Class HelpDialog
###########################################################################

class HelpDialog (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Help", pos=wx.DefaultPosition, size=wx.Size(
            182, 117), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer58 = wx.BoxSizer(wx.VERTICAL)

        self.SetSizer(bSizer58)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
# Class LogininDialog
###########################################################################

class LogininDialog (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Log in",
                           pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gSizer66 = wx.GridSizer(1, 1, 0, 0)

        bSizer51 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText220 = wx.StaticText(
            self, wx.ID_ANY, u"Learning app", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText220.Wrap(-1)
        self.m_staticText220.SetFont(wx.Font(
            20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        bSizer51.Add(self.m_staticText220, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer661 = wx.GridSizer(3, 2, 0, 0)

        self.m_staticText2101 = wx.StaticText(
            self, wx.ID_ANY, u"Username:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2101.Wrap(-1)
        gSizer661.Add(self.m_staticText2101, 0, wx.ALL |
                      wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.UsernameTC1 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer661.Add(self.UsernameTC1, 0, wx.ALL |
                      wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText2111 = wx.StaticText(
            self, wx.ID_ANY, u"Password:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2111.Wrap(-1)
        gSizer661.Add(self.m_staticText2111, 0, wx.ALL |
                      wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.PasswordTC1 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        gSizer661.Add(self.PasswordTC1, 0, wx.ALL |
                      wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.NewUserBtn1 = wx.Button(
            self, wx.ID_ANY, u"Sign up", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer661.Add(self.NewUserBtn1, 0, wx.ALL |
                      wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.LoginBtn1 = wx.Button(
            self, wx.ID_OK, u"Log in", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer661.Add(self.LoginBtn1, 0, wx.ALL |
                      wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer51.Add(gSizer661, 1, wx.EXPAND, 5)

        gSizer66.Add(bSizer51, 1, wx.EXPAND, 5)

        self.SetSizer(gSizer66)
        self.Layout()
        gSizer66.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.NewUserBtn1.Bind(wx.EVT_BUTTON, self.OnSignUp)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnSignUp(self, event):
        event.Skip()


###########################################################################
# Class NewUserDialog
###########################################################################

class NewUserDialog (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"New User",
                           pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gSizer67 = wx.GridSizer(1, 1, 0, 0)

        bSizer49 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText215 = wx.StaticText(
            self, wx.ID_ANY, u"Learning app", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText215.Wrap(-1)
        self.m_staticText215.SetFont(wx.Font(
            20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        bSizer49.Add(self.m_staticText215, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer68 = wx.GridSizer(4, 2, 0, 0)

        self.UsernameST = wx.StaticText(
            self, wx.ID_ANY, u"Username:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.UsernameST.Wrap(-1)
        gSizer68.Add(self.UsernameST, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.UsernameTC = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer68.Add(self.UsernameTC, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.FrstPassword = wx.StaticText(
            self, wx.ID_ANY, u"Password:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.FrstPassword.Wrap(-1)
        gSizer68.Add(self.FrstPassword, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.FrstPasswordTC = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        gSizer68.Add(self.FrstPasswordTC, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.ScndPassword = wx.StaticText(
            self, wx.ID_ANY, u"Give your password again:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ScndPassword.Wrap(-1)
        gSizer68.Add(self.ScndPassword, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.ScndPasswordTC = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        gSizer68.Add(self.ScndPasswordTC, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.CancelBtn = wx.Button(
            self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer68.Add(self.CancelBtn, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.CreateUserBtn = wx.Button(
            self, wx.ID_OK, u"Create user", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer68.Add(self.CreateUserBtn, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer49.Add(gSizer68, 1, wx.EXPAND, 5)

        gSizer67.Add(bSizer49, 1, wx.EXPAND, 5)

        self.SetSizer(gSizer67)
        self.Layout()
        gSizer67.Fit(self)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
