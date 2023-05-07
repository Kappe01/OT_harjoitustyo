from tkinter import ttk, constants
from services.learning_services import learning_service


class ResultListView:
    'Näyttää tulokset listana'
    def __init__(self, root, results):
        self._root = root
        self._results = results
        self._frame = None

        self._init()

    def pack(self):
        'Näyttää listan'
        self._frame.pack(fill=constants.X)

    def destroy(self):
        'Piilottaa listan'
        self._frame.destroy()

    def _init_result(self, result, value):
        'Alustaa yhden tuloksen'
        result_frame = ttk.Frame(master=self._frame)

        subject = ttk.Label(master=self._frame, text=result[0])

        question = ttk.Label(master=self._frame, text=result[1])

        answer = ttk.Label(master=self._frame, text=result[2])

        subject.grid(
            row=value,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        question.grid(
            row=value,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        answer.grid(
            row=value,
            column=2,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        result_frame.grid_columnconfigure(0, weight=1)

    def _init(self):
        'Alustaa listan'
        self._frame = ttk.Frame(master=self._root)

        for i, result in enumerate(self._results):
            self._init_result(result, i)


class ResultView:
    'Itse vastaus ikkuna'
    def __init__(self, root, handle_main_view):
        self._root = root
        self._handle_main_view = handle_main_view
        self._result_frame = None
        self._result_view = None

        self._frame = None

        self._init()

    def pack(self):
        'Näyttää ikkunan'
        self._frame.pack(fill=constants.X)

    def destroy(self):
        'Piilottaa ikkunan'
        self._frame.destroy()

    def _init_header(self):
        'Alustaa headerin'
        home_btn = ttk.Button(
            master=self._frame,
            text='Home',
            command=self._handle_main_view
        )

        home_btn.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _init_results(self):
        'alustaa vastaus listan'
        if self._result_view:
            self._result_view.destroy()
        subject_label = ttk.Label(master=self._frame, text='Subject')

        question_label = ttk.Label(master=self._frame, text='Question')

        result_label = ttk.Label(master=self._frame, text='Result')

        subject_label.grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.W
        )

        question_label.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.W
        )

        result_label.grid(
            row=1,
            column=2,
            padx=5,
            pady=5,
            sticky=constants.W
        )

        results = learning_service.get_results()

        self._result_view = ResultListView(
            self._result_frame,
            results
        )

        self._result_view.pack()

    def _init(self):
        'Alustaa ikkunan'
        self._frame = ttk.Frame(master=self._root)
        self._result_frame = ttk.Frame(master=self._frame)

        self._init_header()
        self._init_results()

        self._result_frame.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
