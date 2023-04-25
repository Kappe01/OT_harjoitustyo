from tkinter import ttk, constants, StringVar
from services.learning_services import learning_service, QuestionExistserror


class AnswerEntryField:
    '''Useless atm but still here if I decide to add multiple question types'''

    def __init__(self, root, q_type, answer_handler):
        self._root = root
        self._q_type = 'Text'
        self._handle_answer = answer_handler
        self._frame = None

        self._init()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _init_text(self):
        text_frame = ttk.Frame(master=self._frame)

        label = ttk.Label(master=text_frame, text='Answer:')
        entry = ttk.Entry(master=text_frame)

        label.grid(padx=5, pady=5, sticky=constants.W)
        entry.grid(padx=5, pady=5, sticky=constants.EW)

        text_frame.grid_columnconfigure(0, weight=1)
        text_frame.pack(fill=constants.X)

    def _init_true_or_false(self):
        true_or_false_frame = ttk.Frame(master=self._frame)

        label = ttk.Label(master=true_or_false_frame, text='Answer:')

        radio1 = ttk.Radiobutton(
            master=true_or_false_frame,
            text='True',
            value=True,
            variable=StringVar()
        )
        radio2 = ttk.Radiobutton(
            master=true_or_false_frame,
            text='False',
            value=False,
            variable=StringVar()
        )

        label.grid(padx=5, pady=5, sticky=constants.W)
        radio1.grid(padx=5, pady=5, sticky=constants.EW)
        radio2.grid(padx=5, pady=5, sticky=constants.EW)

        true_or_false_frame.grid_columnconfigure(0, weight=1)
        true_or_false_frame.pack(fill=constants.X)

    def _init_choose_all(self):
        pass  # Tee tämä loppuun

    def _init(self):
        self._frame = ttk.Frame(master=self._root)

        if self._q_type == 'Text':
            self._init_text()

        elif self._q_type == 'True or False':
            self._init_true_or_false()

        else:
            self._init_choose_all()


class NewQuestionView:
    def __init__(self, root, handle_add_question, handle_main_view):
        self._root = root
        self._handle_add_question = handle_add_question
        self._handle_main_view = handle_main_view
        self._frame = None
        self._user = learning_service.get_current_user()
        self._question_entry = None
        self._subject_entry = None
        self._question_type_entry = None
        self._answer_entry = None
        # self._answer_entry_view = None
        # self._answer_entry_frame = None
        self._error_variable = None
        self._error_label = None

        self._init()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _add_question_handler(self):
        question = self._question_entry.get()
        subject = self._subject_entry.get()
        q_type = self._question_type_entry.get()
        answer = self._answer_entry.get()  # Väliaikainen ratkaisu

        try:
            # Lisää vielä tapa saada vastaus
            learning_service.add_question(question, subject, q_type, answer)
            self._handle_add_question()
        except QuestionExistserror:
            self._show_error(
                'Something went wrong with adding the question, check your entrys and try again!')

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _init_question_field(self):
        question_label = ttk.Label(master=self._frame, text='Question:')

        self._question_entry = ttk.Entry(master=self._frame)

        question_label.grid(padx=5, pady=5, sticky=constants.W)
        self._question_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_subject_field(self):
        subject_label = ttk.Label(master=self._frame, text='Subject:')

        subjects = learning_service.get_subjects()

        subjects_names = [i.subject for i in subjects]

        self._subject_entry = ttk.Combobox(
            master=self._frame, values=subjects_names)

        subject_label.grid(padx=5, pady=5, sticky=constants.W)
        self._subject_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_question_type_field(self):
        question_type_label = ttk.Label(
            master=self._frame, text='Question type:')

        # , 'True or False', 'Choose all correct answers'])
        self._question_type_entry = ttk.Combobox(
            master=self._frame, values=['Text'])

        question_type_label.grid(padx=5, pady=5, sticky=constants.W)
        self._question_type_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_answer_field(self):
        answer_label = ttk.Label(master=self._frame, text='Answer:')

        self._answer_entry = ttk.Entry(master=self._frame)

        answer_label.grid(padx=5, pady=5, sticky=constants.W)
        self._answer_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_footer(self):
        add_question_btn = ttk.Button(
            master=self._frame,
            text='Add question',
            command=self._add_question_handler
        )

        cancel_btn = ttk.Button(
            master=self._frame,
            text='Cancel',
            command=self._handle_main_view
        )

        add_question_btn.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        cancel_btn.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _init(self):
        self._frame = ttk.Frame(master=self._root)
        self._answer_entry_frame = ttk.Frame(master=self._frame)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._init_footer()
        self._init_question_field()
        self._init_subject_field()
        self._init_question_type_field()
        self._init_answer_field()

        self._answer_entry_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
