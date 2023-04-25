from tkinter import ttk, constants
from services.learning_services import learning_service


class QuestionView:
    def __init__(self, root, handle_main_view, handle_results_view):
        self._root = root
        self._handle_main_view = handle_main_view
        self._handle_result_view = handle_results_view
        self._question = None
        self._questions = None
        self._iterator = 0
        self._frame = None
        self._answer_entry = None
        self._correct_answer_frame = None
        self._correct_answer_view = None

        self._init()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_incorrect(self):
        learning_service.result(
            self._questions[self._iterator].subject, self._questions[self._iterator].question, 'Incorrect')
        self._iterator += 1
        self._init_start()

    def _handle_correct(self):
        learning_service.result(
            self._questions[self._iterator].subject, self._questions[self._iterator].question, 'Correct')
        self._iterator += 1
        self._init_start()

    def _init_header(self):
        cancel_btn = ttk.Button(
            master=self._frame,
            text='Cancel',
            command=self._handle_main_view
        )

        cancel_btn.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _init_question(self, question):
        question_label = ttk.Label(master=self._frame, text=question.question)

        answer_label = ttk.Label(master=self._frame, text='Your answer:')

        self._answer_entry = ttk.Entry(master=self._frame)

        check_answer_btn = ttk.Button(
            master=self._frame,
            text='Check correct answer',
            command=self._init_correct_answer_field(question)
        )

        question_label.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.W
        )

        answer_label.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.W
        )

        self._answer_entry.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        check_answer_btn.grid(
            row=3,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _init_correct_answer_field(self, question):
        correct_answer_label1 = ttk.Label(
            master=self._frame,
            text='Correct answer:'
        )

        correct_answer_label2 = ttk.Label(
            master=self._frame,
            text=question.answer
        )

        correct_answer_label1.grid(
            row=4,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.W
        )

        correct_answer_label2.grid(
            row=4,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _init_footer(self):
        incorrect_btn = ttk.Button(
            master=self._frame,
            text='Incorrect',
            command=self._handle_incorrect
        )

        correct_btn = ttk.Button(
            master=self._frame,
            text='Correct',
            command=self._handle_correct
        )

        incorrect_btn.grid(
            row=4,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        correct_btn.grid(
            row=4,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def get_questions(self):
        self._questions = learning_service.get_current_questions()

    def _init_start(self):
        if self._iterator >= len(self._questions):
            self._handle_main_view()
            return
        self._init_header()
        self._init_question(self._questions[self._iterator])
        self._init_footer()

    def _init(self):
        self._frame = ttk.Frame(master=self._root)
        self._correct_answer_frame = ttk.Frame(master=self._frame)

        self.get_questions()
        self._init_start()

        self._correct_answer_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
