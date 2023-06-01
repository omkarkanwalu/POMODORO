from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count(long_break_sec)
        label.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        count(short_break_sec)
        label.config(text="SHORT BREAK", fg=PINK)
    else:
        count(work_sec)
        label.config(text="WORK", fg=GREEN)

    # count(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count(num):
    count_min = math.floor(num / 60)
    conut_sec = num % 60
    if conut_sec < 10:
        conut_sec = f"0{conut_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{conut_sec}")
    if num > 0:
        global timer
        timer = window.after(1000, count, num - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

label = Label(text="Timer", font=(FONT_NAME, 35), bg=YELLOW, fg=GREEN)
# label.config(text="miles")
label.grid(column=2, row=1)

start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

check_mark = Label(text="✔", font=(FONT_NAME, 20), bg=YELLOW, fg=GREEN)
# label.config(text="miles")
check_mark.grid(column=2, row=4)

window.mainloop()
