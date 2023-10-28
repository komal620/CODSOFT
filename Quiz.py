import tkinter as tk
import random

class QuizGame:
    def _init_(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.quiz_data = [
            {
                "question": "What is the capital of France?",
                "choices": ["a) London", "b) Berlin", "c) Paris", "d) Madrid"],
                "correct_choice": "c"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "choices": ["a) Earth", "b) Mars", "c) Jupiter", "d) Venus"],
                "correct_choice": "c"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "choices": ["a) William Shakespeare", "b) Charles Dickens", "c) Stephen King", "d) J. K. Rowling"],
                "correct_choice": "a"
            },
            {
                "question": "What is the capital of Bihar?",
                "choices": ["a) Patna", "b) Ranchi", "c) Delhi", "d) Mumbai"],
                "correct_choice": "a"
            },
            {
                "question": "who developed this?",
                "choices": ["a) IDK", "b) no one", "c) Vaibhav", "d) Ayush"],
                "correct_choice": "c" 
            }
        ]

        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.question_label.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.radio_var, value=str(i), font=("Helvetica", 12))
            self.radio_buttons.append(rb)
            rb.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("Helvetica", 12))
        self.next_button.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.feedback_label.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.current_question < len(self.quiz_data):
            question_data = self.quiz_data[self.current_question]
            self.question_label.config(text=question_data["question"])
            if "choices" in question_data:
                for i in range(4):
                    self.radio_buttons[i].config(text=question_data["choices"][i])
            self.feedback_label.config(text="")
        else:
            self.display_final_results()

    def next_question(self):
        question_data = self.quiz_data[self.current_question]
        user_answer = self.radio_var.get()
        if user_answer == question_data["correct_choice"]:
            self.score += 1
        else:
            self.feedback_label.config(text=f"Wrong! The correct answer is: {question_data['correct_choice']}")

        self.current_question += 1
        self.radio_var.set("")
        self.load_question()

    def load_question(self):
        if self.current_question < len(self.quiz_data):
            question_data = self.quiz_data[self.current_question]
            self.question_label.config(text=question_data["question"])
            if "choices" in question_data:
                for i in range(4):
                    self.radio_buttons[i].config(text=question_data["choices"][i])
            self.feedback_label.config(text=f"Score: {self.score}/{len(self.quiz_data)}")
        else:
            self.display_final_results()

if _name_ == "_main_":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
