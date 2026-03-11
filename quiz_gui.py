import tkinter as tk
from tkinter import messagebox, ttk
import random

# ---------------- QUESTIONS ---------------- #

quiz_data = [
("What does CPU stand for?", ["Central Processing Unit","Computer Power Unit","Control Program Unit","Central Program Unit"], "Central Processing Unit"),
("What does RAM stand for?", ["Random Access Memory","Read Access Memory","Run Access Memory","Real Access Memory"], "Random Access Memory"),
("Which language is used for Data Science?", ["Java","Python","C++","HTML"], "Python"),
("Which company created Windows?", ["Apple","Microsoft","Google","IBM"], "Microsoft"),
("Which symbol is used for comments in Python?", ["#","//","/*","--"], "#"),
("Which keyword defines a function?", ["function","define","def","fun"], "def"),
("Which data type stores True/False?", ["Boolean","Integer","Float","String"], "Boolean"),
("Which operator multiplies numbers?", ["*","+","/","-"], "*"),
("Which keyword creates loops?", ["repeat","loop","for","iterate"], "for"),
("Which keyword is used for condition checking?", ["if","check","when","case"], "if"),
("Which keyword exits a loop?", ["stop","break","exit","return"], "break"),
("Which keyword skips an iteration?", ["skip","continue","pass","next"], "continue"),
("Which keyword imports libraries?", ["import","include","add","load"], "import"),
("Which keyword creates a class?", ["object","class","define","structure"], "class"),
("Which Python function prints output?", ["echo","print","display","write"], "print"),
("Which function gets user input?", ["scan","input","read","ask"], "input"),
("Which symbol divides numbers?", ["/","%","//","*"], "/"),
("Which data type stores decimals?", ["float","int","double","decimal"], "float"),
("Which operator checks equality?", ["=","==","===","!="], "=="),
("Which keyword handles errors?", ["try","catch","handle","error"], "try"),
("Which block catches errors?", ["catch","except","error","finally"], "except"),
("Which module generates random numbers?", ["math","random","numbers","calc"], "random"),
("Which module works with time?", ["timer","clock","time","date"], "time"),
("Which data structure stores ordered values?", ["set","dictionary","list","map"], "list"),
("Which structure stores key-value pairs?", ["list","dictionary","array","tuple"], "dictionary"),
("Which keyword defines inheritance?", ["inherit","extends","super","parent"], "super"),
("Which method adds item to list?", ["insert","append","add","push"], "append"),
("Which function finds length?", ["count","length","len","size"], "len"),
("Which extension is used for Python files?", [".pt",".python",".py",".p"], ".py"),
("Which company developed Python?", ["Google","Microsoft","Python Software Foundation","IBM"], "Python Software Foundation")
]

random.shuffle(quiz_data)

# ---------------- VARIABLES ---------------- #

question_index = 0
score = 0
timer_id = None
time_left = 20
max_time = 20
difficulty = "Medium"

# ---------------- FUNCTIONS ---------------- #

def hover(btn, color):
    btn.bind("<Enter>", lambda e: btn.config(bg=color))
    btn.bind("<Leave>", lambda e: btn.config(bg="#4CAF50"))

def update_difficulty_label():
    selected = difficulty_var.get()
    difficulty_status.config(text=f"Selected Level: {selected}")

def set_difficulty():
    global difficulty, max_time

    difficulty = difficulty_var.get()

    if difficulty == "Easy":
        max_time = 30
        difficulty_badge.config(bg="green", text="Easy Level")
    elif difficulty == "Medium":
        max_time = 20
        difficulty_badge.config(bg="orange", text="Medium Level")
    else:
        max_time = 10
        difficulty_badge.config(bg="red", text="Hard Level")

def start_quiz():

    if player_name.get() == "":
        messagebox.showwarning("Warning","Please enter your name")
        return

    set_difficulty()

    messagebox.showinfo("Welcome", f"Welcome {player_name.get()}!\nGood luck in the quiz.")

    start_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)

    load_question()

def load_question():
    global time_left

    time_left = max_time

    progress_bar["maximum"] = max_time
    progress_bar["value"] = max_time

    update_timer()

    question, options, answer = quiz_data[question_index]

    progress_label.config(text=f"Question {question_index+1}/30")

    question_label.config(text=question)

    for i in range(4):
        radio_buttons[i].config(text=options[i], value=options[i])

    selected_option.set(None)

def update_timer():
    global time_left, timer_id

    timer_label.config(text=f"⏳ {time_left}s")

    progress_bar["value"] = time_left

    if time_left > 0:
        time_left -= 1
        timer_id = window.after(1000, update_timer)
    else:
        next_question()

def check_answer():
    global score

    question, options, answer = quiz_data[question_index]

    if selected_option.get() == answer:
        score += 1

def next_question():
    global question_index, timer_id

    if timer_id:
        window.after_cancel(timer_id)

    check_answer()

    question_index += 1

    if question_index < len(quiz_data):
        load_question()
    else:
        finish_quiz()

def finish_quiz():

    percentage = (score/len(quiz_data))*100

    messagebox.showinfo(
        "Quiz Finished",
        f"Name: {player_name.get()}\n"
        f"Difficulty: {difficulty}\n"
        f"Score: {score}/30\n"
        f"Percentage: {round(percentage,2)}%"
    )

    window.destroy()

# ---------------- UI ---------------- #

window = tk.Tk()
window.title("Python Quiz Game")
window.geometry("650x550")
window.config(bg="#1e1e2f")

# -------- START SCREEN -------- #

start_frame = tk.Frame(window,bg="#1e1e2f")
start_frame.pack(pady=70)

tk.Label(start_frame,
text="Welcome to the Python Quiz Game!",
font=("Arial",18,"bold"),
bg="#1e1e2f",
fg="#00d4ff").pack(pady=10)

tk.Label(start_frame,
text="Enter Your Name",
font=("Arial",14),
bg="#1e1e2f",
fg="white").pack()

player_name = tk.Entry(start_frame,font=("Arial",12))
player_name.pack(pady=10)

difficulty_var = tk.StringVar(value="Medium")

tk.Label(start_frame,
text="Select Difficulty",
font=("Arial",14),
bg="#1e1e2f",
fg="white").pack(pady=10)

tk.Radiobutton(start_frame,text="Easy",variable=difficulty_var,value="Easy",
command=update_difficulty_label,bg="#1e1e2f",fg="white").pack()

tk.Radiobutton(start_frame,text="Medium",variable=difficulty_var,value="Medium",
command=update_difficulty_label,bg="#1e1e2f",fg="white").pack()

tk.Radiobutton(start_frame,text="Hard",variable=difficulty_var,value="Hard",
command=update_difficulty_label,bg="#1e1e2f",fg="white").pack()

difficulty_status = tk.Label(start_frame,
text="Selected Level: Medium",
font=("Arial",11,"bold"),
bg="#1e1e2f",
fg="yellow")

difficulty_status.pack(pady=5)

start_btn = tk.Button(start_frame,
text="Start Quiz",
font=("Arial",12,"bold"),
bg="#4CAF50",
fg="white",
command=start_quiz)

start_btn.pack(pady=15)

hover(start_btn,"#2e7d32")

# -------- QUIZ SCREEN -------- #

quiz_frame = tk.Frame(window,bg="#1e1e2f")

difficulty_badge = tk.Label(quiz_frame,
text="Level",
font=("Arial",10,"bold"),
fg="white")

difficulty_badge.pack(pady=5)

progress_label = tk.Label(quiz_frame,
text="Question",
font=("Arial",12),
bg="#1e1e2f",
fg="white")

progress_label.pack()

progress_bar = ttk.Progressbar(quiz_frame,length=400)
progress_bar.pack(pady=10)

timer_label = tk.Label(quiz_frame,
text="⏳",
font=("Arial",12,"bold"),
bg="#1e1e2f",
fg="orange")

timer_label.pack()

question_label = tk.Label(quiz_frame,
text="",
wraplength=500,
font=("Arial",16),
bg="#2d2d44",
fg="white",
padx=20,
pady=20)

question_label.pack(pady=20)

selected_option = tk.StringVar()

radio_buttons = []

for i in range(4):

    rb = tk.Radiobutton(quiz_frame,
    text="",
    variable=selected_option,
    font=("Arial",13),
    bg="#1e1e2f",
    fg="white",
    selectcolor="#444")

    rb.pack(anchor="w", padx=50)

    radio_buttons.append(rb)

next_btn = tk.Button(quiz_frame,
text="Next Question",
font=("Arial",12,"bold"),
bg="#4CAF50",
fg="white",
command=next_question)

next_btn.pack(pady=20)

hover(next_btn,"#2e7d32")

window.mainloop()