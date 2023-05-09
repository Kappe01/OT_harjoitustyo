from tkinter import ttk, constants, StringVar
from services.learning_services import learning_service, QuestionExistserror


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
        self._error_variable = None
        self._error_label = None

        self._init()

    def pack(self):
        'Näyttää ikkunan'
        self._frame.pack(fill=constants.X)

    def destroy(self):
        'Tuhoaa ikkunan'
        self._frame.destroy()

    def _add_question_handler(self):
        'Lisää kysymyksen tietokantaan'
        question = self._question_entry.get()
        subject = self._subject_entry.get()
        q_type = self._question_type_entry.get()
        answer = self._answer_entry.get()

        try:
            learning_service.add_question(question, subject, q_type, answer)
            self._handle_add_question()
        except QuestionExistserror:
            self._show_error(
                'Something went wrong with adding the question, check your entrys and try again!')

    def _show_error(self, message):
        'Näyttää vihre ilmoituksen'
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        'Piilottaa virhe ilmoituksen'
        self._error_label.grid_remove()

    def _init_question_field(self):
        'Alustaa kysymys kohdan'
        question_label = ttk.Label(master=self._frame, text='Question:')

        self._question_entry = ttk.Entry(master=self._frame)

        question_label.grid(padx=5, pady=5, sticky=constants.W)
        self._question_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_subject_field(self):
        'Alustaa aihe kohdan'
        subject_label = ttk.Label(master=self._frame, text='Subject:')

        subjects = learning_service.get_subjects()

        subjects_names = [i.subject for i in subjects]

        self._subject_entry = ttk.Combobox(
            master=self._frame, values=subjects_names)

        subject_label.grid(padx=5, pady=5, sticky=constants.W)
        self._subject_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_question_type_field(self):
        'Alustaa kysymyksen tyyppi kohdan'
        question_type_label = ttk.Label(
            master=self._frame, text='Question type:')

        self._question_type_entry = ttk.Combobox(
            master=self._frame, values=['Text'])

        question_type_label.grid(padx=5, pady=5, sticky=constants.W)
        self._question_type_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_answer_field(self):
        'Alustaa vastaus kohdan'
        answer_label = ttk.Label(master=self._frame, text='Answer:')

        self._answer_entry = ttk.Entry(master=self._frame)

        answer_label.grid(padx=5, pady=5, sticky=constants.W)
        self._answer_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_footer(self):
        'Alustaa alimman rivin'
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
        'Alustaa koko ikkunan'
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
