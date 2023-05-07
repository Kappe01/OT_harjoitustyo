from tkinter import ttk, constants
from services.learning_services import learning_service

class DeleteQListView:
    'Näyttää kaikki käyttäjän kysymykset listana'
    def __init__(self, root, questions, handle_button):
        self._root = root
        self._questions = questions
        self._handle_button = handle_button
        self._frame = None

        self._init()

    def pack(self):
        'Näyttää listan'
        self._frame.pack(fill=constants.X)

    def destroy(self):
        'Piilottaa listan'
        self._frame.destroy()

    def _init_questions(self, question,i):
        'alustaa yhden kysymyksen'
        delete_frame = ttk.Frame(
            master=self._frame
        )

        question_label = ttk.Label(
            master=self._frame,
            text=question.question
        )

        subject_label = ttk.Label(
            master=self._frame,
            text=question.subject
        )

        q_type_label = ttk.Label(
            master=self._frame,
            text=question.q_type
        )

        delete_button = ttk.Button(
            master=self._frame,
            text='Delete',
            command=lambda: self._handle_button(question.question)
        )

        question_label.grid(
            row=i,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.W
        )

        subject_label.grid(
            row=i,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.W
        )

        q_type_label.grid(
            row=i,
            column=2,
            padx=5,
            pady=5,
            sticky=constants.W
        )

        delete_button.grid(
            row=i,
            column=3,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        delete_frame.grid_columnconfigure(0, weight=1)

    def _init(self):
        'Alustaa listan'
        self._frame = ttk.Frame(master=self._root)

        for i, question in enumerate(self._questions):
            self._init_questions(question, i)


class SettingsView:
    'Asetus näkymä'
    def __init__(self, root, handle_main_view):
        self._root = root
        self._handle_main_view = handle_main_view
        self._delete_question_list_view = None
        self._delete_question_frame_view = None
        self._frame = None

        self._init()

    def pack(self):
        'Näyttää ikkunan'
        self._frame.pack(fill=constants.X)

    def destroy(self):
        'Piilottaa ikkunan'
        self._frame.destroy()

    def _handle_button(self, question):
        'Poistaa kysymyksen'
        learning_service.delete_question(question)

        self._init_delete_question()

    def _add_default_questions(self):
        'Lisää perus kysymykset'
        learning_service.default_questions()

    def _init_header(self):
        'Alustaa headerin'
        home_button = ttk.Button(
            master=self._frame,
            text='Home',
            command=self._handle_main_view
        )

        add_default_q_button = ttk.Button(
            master=self._frame,
            text='Add default questions',
            command=self._add_default_questions
        )

        home_button.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        add_default_q_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _init_delete_question(self):
        'Alustaa kysymys listan'
        if self._delete_question_list_view:
            self._delete_question_list_view.destroy()

        all_q = learning_service.get_all_questions()
        
        self._delete_question_list_view = DeleteQListView(
            self._delete_question_frame_view,
            all_q,
            self._handle_button
        )

        self._delete_question_list_view.pack()

    def _init(self):
        'Alustaa koko ikkunan'
        self._frame = ttk.Frame(master=self._root)
        self._delete_question_frame_view = ttk.Frame(master=self._frame)

        self._init_header()
        self._init_delete_question()

        self._delete_question_frame_view.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)

        