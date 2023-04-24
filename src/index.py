from tkinter import Tk
from ui.ui import ui


def main():
    window = Tk()
    window.title("Learning app")

    ui_view = ui(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()