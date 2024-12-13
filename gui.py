from tkinter import Tk, Label, Frame, Entry, IntVar, Radiobutton, Button


class Gui:
    def __init__(self, window: Tk):
        self.window = window

        self.label_title: Label = Label(self.window, text="VOTING BOOTH")
        self.label_title.pack(pady=10)

        self.frame_id: Frame = Frame(self.window)
        self.label_id: Label = Label(self.frame_id, text="ID")
        self.input_id: Entry = Entry(self.frame_id)

        self.label_id.pack(side="left")
        self.input_id.pack(side="right")
        self.frame_id.pack(ipadx=10, pady=10)

        self.frame_voter_options: Frame = Frame(self.window)
        self.label_voter_options: Label = Label(
            self.frame_voter_options, text="CANDIDATES"
        )
        self.radio_choice: IntVar = IntVar()
        self.radio_choice.set(0)
        self.radio_candidate_bianca: Radiobutton = Radiobutton(
            self.frame_voter_options, text="Bianca", value=1, variable=self.radio_choice
        )
        self.radio_candidate_edward: Radiobutton = Radiobutton(
            self.frame_voter_options, text="Edward", value=2, variable=self.radio_choice
        )
        self.radio_candidate_felicia: Radiobutton = Radiobutton(
            self.frame_voter_options,
            text="Felicia",
            value=3,
            variable=self.radio_choice,
        )
        self.label_voter_options.pack(pady=10)
        self.radio_candidate_bianca.pack(anchor="w")
        self.radio_candidate_edward.pack(anchor="w")
        self.radio_candidate_felicia.pack(anchor="w")
        self.frame_voter_options.pack()

        self.button_submit: Button = Button(
            self.window, text="SUBMIT", command=self.vote
        )
        self.button_submit.pack(pady=10)

        self.label_alert: Label = Label(self.window)
