from tkinter import ttk, constants
from services.learning_services import learning_service

class AnswerView:
    'Vastaus kohta'
    def __init__(self, root, question):
        self._root = root
        self._question = question
        self._frame = None

        self._init()

    def pack(self):
        'Näyttää vastauksen'
        self._frame.pack(fill=constants.X)

    def destroy(self):
        'Piilottaa vastauksen'
        self._frame.destroy()

    def _init_answer(self):
        'Alustaa vastaus kohdan'
        answer_label1 = ttk.Label(
            master=self._frame,
            text='Correct answer:'
        )

        answer_label2 = ttk.Label(
            master=self._frame,
            text=self._question.answer
        )

        answer_label1.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.W
        )

        answer_label2.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _init(self):
        'Alustaa vastauskohdan'
        self._frame = ttk.Frame(
            master=self._root
        )

        self._init_answer()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)


class QuestionFrame:
    'Kysymys kohta'
    def __init__(self, root, question, handle_correct, handle_incorrect):
        self._root = root
        self._question = question
        self._handle_correct = handle_correct
        self._handle_incorrect = handle_incorrect
        self._answer_view = None
        self._answer_frame = None
        self._frame = None

        self._init()

    def pack(self):
        'Näyttää kysymyksen'
        self._frame.pack(fill=constants.X)

    def destroy(self):
        'Piilottaa kysymyksen'
        self._frame.destroy()

    def _init_correct_answer_field(self):
        'alustaa vastaus kohdan'
        if self._answer_view:
            self._answer_view.destroy()

        self._answer_view = AnswerView(
            self._answer_frame,
            self._question
        )

        self._answer_view.pack()


    def _init_question(self):
        'Alustaa kysymyksen'
        question_label = ttk.Label(
            master=self._frame, text=self._question.question)

        answer_label = ttk.Label(master=self._frame, text='Your answer:')

        answer_entry = ttk.Entry(master=self._frame)

        check_answer_btn = ttk.Button(
            master=self._frame,
            text='Check correct answer',
            command=self._init_correct_answer_field
        )

        question_label.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.W
        )

        answer_label.grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.W
        )

        answer_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        check_answer_btn.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        incorrect_btn = ttk.Button(
            master=self._frame,
            text='Incorrect',
            command=lambda: self._handle_incorrect(self._question)
        )

        correct_btn = ttk.Button(
            master=self._frame,
            text='Correct',
            command=lambda: self._handle_correct(self._question)
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

    def _init(self):
        'Näyttää kysymyksen'
        self._frame = ttk.Frame(master=self._root)
        self._answer_frame = ttk.Frame(master=self._frame)

        self._init_question()

        self._answer_frame.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)


class QuestionView:
    'Itse näkymä'
    def __init__(self, root, handle_main_view, handle_results_view):
        self._root = root
        self._handle_main_view = handle_main_view
        self._handle_result_view = handle_results_view
        self._questions = [],
        self._iterator = 0
        self._frame = None
        self._question_frame = None
        self._question_view = None

        self._init()

    def pack(self):
        'Näyttää ikkunan'
        self._frame.pack(fill=constants.X)

    def destroy(self):
        'Piilottaa ikkunan'
        self._frame.destroy()

    def _handle_incorrect(self, question):
        'Lisää vastauksen listaan jos vastaus ei ollut oikein'
        learning_service.result(
            question.subject, question.question, 'Incorrect')
        self._iterator += 1
        self._init_questions()

    def _handle_correct(self, question):
        'Lisää vastauksen listaan jos vastaus oli oikein'
        learning_service.result(
            question.subject, question.question, 'Correct')
        self._iterator += 1
        self._init_questions()

    def _init_header(self):
        'Alustaa headerin'
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

    def _init_questions(self):
        'Näyttää kysymyksen'
        if self._question_view:
            self._question_view.destroy()

        if self._iterator >= len(self._questions):
            self._handle_result_view()
            return

        self._question_view = QuestionFrame(
            self._question_frame,
            self._questions[self._iterator],
            self._handle_correct,
            self._handle_incorrect
        )

        self._question_view.pack()

    def _init(self):
        'alustaa ikkunan'
        self._frame = ttk.Frame(master=self._root)
        self._question_frame = ttk.Frame(master=self._frame)

        self._questions = learning_service.get_current_questions()
        learning_service.reset_subjects()

        self._init_header()
        self._init_questions()

        self._question_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
