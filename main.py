from tkinter import *
from os import path
from math import floor
from vlc import MediaPlayer

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
work_reps = 0
timer_variable = ''
check_mark_arr = []
# function

music_path = path.dirname(__file__)+'/alarm.mp3'
music_proc = MediaPlayer(music_path)


def play_alarm():
    music_proc.play()


def stop_alarm():
    music_proc.stop()


def start_timer():
    global work_reps
    work_reps += 1
    NO_OF_MINUTES_IN_SECONDS = 60
    SHORT_BREAK_SEC = SHORT_BREAK_MIN * NO_OF_MINUTES_IN_SECONDS
    LONG_BREAK_SEC = LONG_BREAK_MIN * NO_OF_MINUTES_IN_SECONDS
    WORK_SEC = WORK_MIN * NO_OF_MINUTES_IN_SECONDS
    if work_reps % 8 == 0:
        count_down(LONG_BREAK_SEC)
        timer_label.config(fg=GREEN, text='Long break')
        play_alarm()
    elif work_reps % 2 == 0:
        count_down(SHORT_BREAK_SEC)
        timer_label.config(fg=PINK, text='Short break')
        play_alarm()
    else:
        count_down(WORK_SEC)
        timer_label.config(fg=RED, text='Work time')
    if floor(work_reps / 2) > 0:
        add_check_mark(int(work_reps / 2))


def reset_timer():
    global work_reps
    work_reps = 0
    timer_label.config(fg=GREEN, text='Timer')
    canvas.itemconfig(timer_text, text=f"00:00")
    global timer_variable
    window.after_cancel(timer_variable)
    if len(check_mark_arr) > 0:
        for check_label in check_mark_arr:
            check_label.destroy()


def count_down(count):
    count_min = floor(count / 60)
    count_sec = '{:02d}'.format(count % 60)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_variable
        timer_variable = window.after(1000, count_down, count - 1)
    else:
        start_timer()


def add_check_mark(row):
    tick_label = Label(text='✅', font=(
        FONT_NAME, 20, 'bold'), bg=GREEN, padx=10, pady=10)
    tick_label.grid(row=2+row, column=1)
    global check_mark_arr
    check_mark_arr.append(tick_label)


# ---------------------------- TIMER RESET ------------------------------- #
img_path = path.dirname(__file__)+'/tomato.png'
window = Tk()
window.title('Pomodora')
window.minsize(width=500, height=500)
window.config(padx=100, height=50, bg=YELLOW)

# Canvas adding picture
canvas = Canvas(width=250, height=250, bg=YELLOW,
                borderwidth=0, highlightthickness=0)
tomato_image = PhotoImage(file=img_path)
canvas.create_image(125, 125, image=tomato_image)
timer_text = canvas.create_text(125, 140, text='00:00', fill='white',
                                font=(FONT_NAME, 35, 'bold'))


# Label
timer_label = Label(text='Timer', font=(
    FONT_NAME, 25, 'bold'), bg=YELLOW, fg=GREEN, padx=20, pady=20)

# Buttons

start_btn = Button(text='Start', bg=GREEN, fg=RED, padx=6,
                   pady=3, highlightthickness=0, font=(FONT_NAME, 12, 'bold'), command=start_timer, borderwidth=0, border=0)
reset_btn = Button(text='Reset', bg=RED, fg=YELLOW, padx=6,
                   pady=3, highlightthickness=0, font=(FONT_NAME, 12, 'bold'), command=reset_timer, borderwidth=0, border=0)
stop_alarm_btn = Button(text='Stop alarm', bg=YELLOW, fg=RED, padx=6,
                        pady=3, highlightthickness=0, font=(FONT_NAME, 12, 'bold'), command=stop_alarm, borderwidth=0, border=0)

# Label


# -------------- LAYOUT IMPLEMENTATION ----------------------
timer_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_btn.grid(row=2, column=0)
reset_btn.grid(row=2, column=2)
stop_alarm_btn.grid(row=2, column=1)
# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #


window.mainloop()
