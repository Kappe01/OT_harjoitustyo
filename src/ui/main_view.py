from tkinter import ttk, constants, IntVar
from services.learning_services import learning_service

class SubjectListView:
    def __init__(self, root, subjects, checkbox_handler):
        self._root = root
        self._subjects = subjects
        self._handle_checkbox = checkbox_handler
        self._frame = None

        self._init()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _init_subject(self, subject):
        subject_frame = ttk.Frame(master=self._frame)

        var = IntVar()

        checkbox = ttk.Checkbutton(
            master=subject_frame,
            text=subject.subject,
            variable=var,
            command=lambda: self._handle_checkbox(subject.subject, var.get())
        )

        checkbox.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        subject_frame.grid_columnconfigure(0, weight=1)
        subject_frame.pack(fill=constants.X)

    def _init(self):
        self._frame = ttk.Frame(master=self._root)

        for subject in self._subjects:
            self._init_subject(subject)

class MainView:
    def __init__(self, root, handle_logout, handle_new_question, handle_question, handle_results_view):
        self._root =  root
        self._handle_logout = handle_logout
        self._handle_new_question = handle_new_question
        self._handle_question = handle_question
        self._handle_results_view = handle_results_view
        self._user = learning_service.get_current_user()
        self._frame = None
        self._subjects_list_view = None
        self._subjects_list_frame = None

        self._init()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _logout_handler(self):
        learning_service.logout()
        self._handle_logout()

    def _question_handler(self):
        self._handle_question()

    def _new_question_handler(self):
        self._handle_new_question()

    def _checkbox_handler(self, subject, check):
        learning_service.add_subject_to_list(subject, check)
    
    def _init_subject_list(self):
        if self._subjects_list_view:
            self._subjects_list_view.destroy()

        subjects = learning_service.get_subjects()

        self._subjects_list_view = SubjectListView(
            self._subjects_list_frame,
            subjects,
            self._checkbox_handler
        )

        self._subjects_list_view.pack()

    def _init_header(self):
        results_btn = ttk.Button(
            master=self._frame,
            text='Results',
            command=self._handle_results_view
        )

        logout_btn = ttk.Button(
            master=self._frame,
            text='Logout',
            command=self._logout_handler
        )

        results_btn.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        logout_btn.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _init_footer(self):
        new_question_btn = ttk.Button(
            master=self._frame,
            text='New Question',
            command=self._handle_new_question
        )

        question_btn = ttk.Button(
            master=self._frame,
            text='Start',
            command=self._handle_question
        )

        new_question_btn.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        question_btn.grid(
           row=0,
           column=0,
           padx=5,
           pady=5,
           sticky=constants.EW 
        )

    def _init(self):
        self._frame = ttk.Frame(master=self._root)
        self._subjects_list_frame = ttk.Frame(master=self._frame)

        self._init_header()
        self._init_subject_list()
        self._init_footer()

        self._subjects_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)