from ui.login_view import LoginView
from ui.create_user_view import CreateUserView
from ui.main_view import MainView
from ui.new_question_view import NewQuestionView
from ui.questions_view import QuestionView
from ui.results_view import ResultView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._show_main_view,
            self._show_create_user_view
        )

        self._current_view.pack()

    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateUserView(
            self._root,
            self._show_main_view,
            self._show_login_view
        )

        self._current_view.pack()

    def _show_main_view(self):
        self._hide_current_view()

        self._current_view = MainView(
            self._root,
            self._show_login_view,
            self._show_new_question_view,
            self._show_question_view,
            self._show_results_view
        )

        self._current_view.pack()

    def _show_new_question_view(self):
        self._hide_current_view()

        self._current_view = NewQuestionView(
            self._root,
            self._show_main_view,
            self._show_main_view
        )

        self._current_view.pack()

    def _show_question_view(self):
        self._hide_current_view()

        self._current_view = QuestionView(
            self._root,
            self._show_main_view,
            self._show_results_view
        )

        self._current_view.pack()

    def _show_results_view(self):
        self._hide_current_view()

        self._current_view = ResultView(
            self._root,
            self._show_main_view
        )

        self._current_view.pack()
