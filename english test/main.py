BGCOLOR = "#21325E"
CORRECT_COLOR = "#F1D00A"
WRONG_COLOR = "#3E497A"
BTN_COLOR = "#F0F0F0"

import csv
from tkinter import *
import random
import pandas as pd
from english_test_func import *
from gtts import gTTS
import pyglet
import os



right_answer_once = 0

#문제 출력
def next_question():
    global answer
    global cur_question

    for i in range(4):
        button[i].config(bg=BTN_COLOR)

    multi_choice = random.sample(question,4)
    find_current(multi_choice)                  # 맞힌 적 있는 문제 거름

    answer = random.randint(0,3)
    cur_question = multi_choice[answer][0]

    question_label.config(text=cur_question)

    #음성 출력
    tts = gTTS(text=cur_question)
    tts.save('english test/sample.mp3')
    music = pyglet.resource.media("sample.mp3")
    music.play()
    os.remove('english test\\sample.mp3')

    for i in range(4):
        button[i].config(text=multi_choice[i][1])


#정답 체크
def check_answer(idx):
    global right_answer_once
    idx = int(idx)
    
    if answer == idx:
        button[idx].config(bg=CORRECT_COLOR)
        window.after(1000, next_question)

        #정답 pandas로 읽고 맞으면 +1
        if right_answer_once == 0:
            question_pd.loc[question_pd.단어==cur_question, '맞힌 수'] += 1
            question_pd.to_csv("english test\\단어장\\voca.csv", index=False)

        else:
            question_pd.loc[question_pd.단어==cur_question, '틀린 수'] += 1
            question_pd.to_csv("english test\\단어장\\voca.csv", index=False)

        right_answer_once = 0

    else:        
        button[idx].config(bg=WRONG_COLOR)
        right_answer_once += 1


with open("english test\\단어장\\voca.csv", "r", encoding="UTF-8-sig") as file:
    question = list(csv.reader(file))    
    
with open("english test\\단어장\\voca.csv", "r", encoding="UTF-8-sig") as file_pd:
    question_pd = pd.read_csv(file_pd)

window = Tk()
window.title("영퀴")
window.config(padx=30, pady=10, bg=BGCOLOR)

#문제 출력 // 박스 그리기
question_label = Label(window, width=20, height=2, text="test", font=("함초롬돋움",25,"bold"), bg=BGCOLOR, fg="white")
question_label.pack(pady=30)

#4지선다 출력 // 박스 그리기
button = []
for i in range(4):
    btn = Button(window, text=f"{i}번", width=50, height=2, font=("함초롬돋움",15,"bold"), bg=BTN_COLOR, command=lambda idx = i:check_answer(idx))
    btn.pack()
    button.append(btn)

#다음 문제 버튼 출력 // 박스 그리기
next_btn = Button(window, text="다음 문제", width=15, height=2, font=("함초롬돋움",15,"bold"), bg=CORRECT_COLOR, command=next_question)
next_btn.pack(pady=30)


next_question()

window.mainloop()