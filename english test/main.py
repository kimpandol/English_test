BGCOLOR = "#21325E"
CORRECT_COLOR = "#F1D00A"
WRONG_COLOR = "#3E497A"
BTN_COLOR = "#F0F0F0"

import csv
from tkinter import *
import random
from english_test_func import *

answer = 0

#문제 출력
def next_question():
    global answer

    for i in range(4):
        button[i].config(bg=BTN_COLOR)

    multi_choice = random.sample(question,4)
    find_current(multi_choice)                  # 맞힌 적 있는 문제 거름
    retry_find(multi_choice)                    # 한번 더 거름

    answer = random.randint(0,3)
    cur_question = multi_choice[answer][0]

    question_label.config(text=cur_question)

    for i in range(4):
        button[i].config(text=multi_choice[i][1])
        print(multi_choice[i])


#정답 체크
def check_answer(idx):
    idx = int(idx)
    if answer == idx:
        button[idx].config(bg=CORRECT_COLOR)
        window.after(1000, next_question)
    else:        
        button[idx].config(bg=WRONG_COLOR)


with open("english test\\단어장\\voca.csv", "r", encoding="UTF-8-sig") as file:
    question = list(csv.reader(file))

window = Tk()
window.title("영퀴")
window.config(padx=30, pady=10, bg=BGCOLOR)

#question BOX
question_label = Label(window, width=20, height=2, text="test", font=("함초롬돋움",25,"bold"), bg=BGCOLOR, fg="white")
question_label.pack(pady=30)

#multiple choice BOX
button = []
for i in range(4):
    btn = Button(window, text=f"{i}번", width=50, height=2, font=("함초롬돋움",15,"bold"), bg=BTN_COLOR, command=lambda idx = i:check_answer(idx))
    btn.pack()
    button.append(btn)

#next btn BOX
next_btn = Button(window, text="다음 문제", width=15, height=2, font=("함초롬돋움",15,"bold"), bg=CORRECT_COLOR, command=next_question)
next_btn.pack(pady=30)

next_question()

window.mainloop()