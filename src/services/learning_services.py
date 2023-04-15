import sqlite3
import traceback

import wx

from entities.questions import Question
from entities.user import User
from repository.question_repository import question_repo
from repository.user_repository import user_repo
from ui.ui import LogininDialog, MyFrame2, NewQDialog, NewUserDialog


class MainClass(MyFrame2):
    def __init__(self):
        MyFrame2.__init__(self, None)

        self.user = ''
        self.results = []

        self.add_base_questions()

        self.LanguageRadio.SetSelection(1)

        self.StartBtn.Bind(wx.EVT_BUTTON, self.on_start_btn)
        self.AddQBtn.Bind(wx.EVT_BUTTON, self.on_new_q)

        login = self.onlogin()
        if not login:
            MainClass()

    def add_base_questions(self):
        try:
            question_repo.create(
                Question('What is 1+1', 'Maths', '2',
                         'Normal', 'All'))
            question_repo.create(
                Question('Derive x: x^2+x+1', 'Maths',
                         '2x+1', 'Normal', 'All'))
            question_repo.create(
                Question('Solve x: 5x+5=5', 'Maths',
                         'x=0', 'Normal', 'All'))

            question_repo.create(Question(
                'What is the gravitational acceleration of the earth?',
                'Physics', '9,81m/s^2', 'Normal', 'All'))
            question_repo.create(Question(
                'What is the unit for energy?', 'Physics', 'Joule (J)', 'Normal', 'All'))
            question_repo.create(Question('What are the two main components of a generator?',
                                 'Physics', 'A coil and a magnet', 'Normal', 'All'))

            question_repo.create(Question(
                'What is the timecomplexity of a for loop?',
                'Programming', 'O(n)', 'Normal', 'All'))
            question_repo.create(Question(
                'Name 3 programming languages', 'Programming',
                'Python, Java, C++', 'Normal', 'All'))
            question_repo.create(Question(
                'What is a käpistelijä?', 'Programming',
                'CS student', 'Normal', 'All'))

        except sqlite3.IntegrityError:
            print(traceback.format_exc())

    def onlogin(self):
        with Login() as log_in:
            if log_in.ShowModal() == wx.ID_OK:
                credentials = log_in.get_credentials()
                if user_repo.find_one_user(User(credentials[0], credentials[1])):
                    self.user = credentials[0]
                    return True

                wx.MessageDialog(
                    None, 'The username or password is incorrect!').ShowModal()
                return False
            return None

    def on_start_btn(self, event):

        questions = []
        subjects_index = self.SubjectsCheckListBox.GetCheckedItems()
        subjects_str = []
        amount = self.m_spinCtrl1.GetValue()

        for i in subjects_index:
            subjects_str.append(self.SubjectsCheckListBox.GetString(i))
        subjects_str.insert(0, self.user)
        subjects_str.insert(len(subjects_str)+1, amount)

        questions = question_repo.get_questions(subjects_str)

        self.results = []
        self.show_question(questions)

        self.ResultGrid.ClearGrid()

        self.show_results()

    def show_question(self, questions):
        for i in questions:
            q_dia = wx.TextEntryDialog(None, i.question, i.subject)
            if q_dia.ShowModal() == wx.ID_OK:
                answer = q_dia.GetValue()
                msg = wx.MessageDialog(
                    None, f'Your answer: {answer}\n Correct answer: {i.answer}',
                    'Answer', wx.YES_NO)
                msg.SetYesNoLabels('Correct', 'Incorrect')
                if msg.ShowModal() == wx.ID_YES:
                    self.results.append((i.subject, i.question, 'Correct'))
                else:
                    self.results.append((i.subject, i.question, 'Incorrect'))
            return None

    def show_results(self):
        for i, value in enumerate(self.results):
            self.ResultGrid.SetCellValue(i, 0, value[0])
            self.ResultGrid.SetCellValue(i, 1, value[1])
            self.ResultGrid.SetCellValue(i, 2, value[2])

    def on_new_q(self, event):
        with NewQDialog(self) as new_q:
            if new_q.ShowModal() == wx.ID_OK:
                pass  # TODO


class Login(LogininDialog):
    def __init__(self):
        LogininDialog.__init__(self, None)

    def get_credentials(self) -> tuple:
        username = self.UsernameTC1.GetValue()
        password = self.PasswordTC1.GetValue()
        return (username, password)

    def OnSignUp(self, event):
        with NewUser() as newuser:
            if newuser.ShowModal() == wx.ID_OK:
                new_info = newuser.get_credentials()
                try:
                    user_repo.new_user(User(new_info[0], new_info[1]))

                except sqlite3.IntegrityError:
                    wx.MessageDialog(None, 'Username already exists!')
                    self.OnSignUp(wx.EVT_BUTTON)

            elif newuser.ShowModal() == wx.ID_CANCEL:
                newuser.Destroy()


class NewUser(NewUserDialog):
    def __init__(self):
        NewUserDialog.__init__(self, None)

    def get_credentials(self):
        username = self.UsernameTC.GetValue()
        password1 = self.FrstPasswordTC.GetValue()
        password2 = self.ScndPasswordTC.GetValue()
        if password1 != password2:
            wx.MessageDialog(
                None, '''The two password don't match''').ShowModal()
            return None
        if len(password1) < 3:
            wx.MessageDialog(
                None, 'The password has to be longer than 3 characters').ShowModal()
            return None
        return (username, password1)
