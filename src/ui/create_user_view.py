from tkinter import ttk, StringVar, constants
from services.learning_services import *

class CreateUserView:
    def __init__(self, root, handle_create_user, handle_show_login_view):
        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_show_login_view = handle_show_login_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._init()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error('Username and password is required')

        if len(password) <= 3:
            self._show_error('Password has to be longer than 3 characters')

        try:
            #Tähän koittaa tehdä käyttäjän
            self._handle_create_user()
        except:
            self._show_error(f'Username {username} already exists')

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _init_username_field(self):
        username_label = ttk.Label(master=self._frame, text='Username')

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _init_password_field(self):
        password_label = ttk.Label(master=self._frame, text='Password')

        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _init(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(master=self._frame, textvariable=self._error_variable, foreground='red')

        self._error_label.grid(padx=5, pady=5)

        self._init_username_field()
        self._init_password_field()

        create_user_btn = ttk.Button(master=self._frame, text='Create', command=self._create_user_handler)

        login_btn = ttk.Button(master= self._frame, text='Login', command=self._handle_show_login_view)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        create_user_btn.grid(padx=5, pady=5, sticky=constants.EW)
        login_btn.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()