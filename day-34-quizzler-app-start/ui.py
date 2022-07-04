from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Button
        check_button_img = PhotoImage(file='./images/true.png')
        self.check_button = Button(image=check_button_img, highlightthickness=0, command=self.check_button_clicked)
        self.check_button.grid(row=2, column=0)

        x_button_img = PhotoImage(file='./images/false.png')
        self.x_button = Button(image=x_button_img, highlightthickness=0, command=self.x_button_clicked)
        self.x_button.grid(row=2, column=1)

        # Label
        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Canvas/text
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="quiz",
            font=FONT,
            fill=THEME_COLOR)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.check_button.config(state="disabled")
            self.x_button.config(state="disabled")

    def x_button_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def check_button_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

