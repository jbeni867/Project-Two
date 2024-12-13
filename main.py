from tkinter import Tk
from logic import Logic


def main() -> None:
    window: Tk = Tk()
    window.title("Voting Booth")
    window.geometry("350x325")
    window.resizable(False, False)
    Logic(window)
    window.mainloop()


if __name__ == "__main__":
    main()
