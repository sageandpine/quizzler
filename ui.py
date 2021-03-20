from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas_1 = Canvas(width=300, height=250)
        self.question_text = self.canvas_1.create_text(150,
                                                       125,
                                                       width=280,
                                                       text="Question Here",
                                                       fill="white",
                                                       font=(
                                                           "Arial", 17, "italic"))
        self.canvas_1.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_img, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.score_label = Label(text="Score: insert score")
        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas_1.itemconfig(self.question_text, text=q_text)