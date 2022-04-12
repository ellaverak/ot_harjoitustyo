from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title('Mömmöystävä')

    ui_view = UI(window)
    ui_view.main_view()

    window.mainloop()


if __name__ == '__main__':
    main()
