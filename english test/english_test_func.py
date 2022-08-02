import csv
import random


with open("english test\\단어장\\voca.csv", "r", encoding="UTF-8-sig") as file:
    question = list(csv.reader(file))
    
multi_choice = random.sample(question,4) 

#맞힌 적 있는 문제 삭제 후 다른 거 넣기
def rechoice(multi_choice, number):
    del multi_choice[number]
    multi_choice += random.sample(question,1)

#맞힌 적 있는 문제 거르기
def find_current(multi_choice):   # 4개 뽑고
    for i in range(4):                          # 맞힌 적 있는문제 거름
        for i in range(4):
            if multi_choice[i][2] != "0":
                rechoice(multi_choice, i)       # 맞힌 적 있는 문제가 있으면 다시 뽑음
                overlap_del(multi_choice)

#반복하면서 맞힌 적 있는 문제 거르기
###### 중복값 제거가 안됨
def retry_find(multi_choice):
    for i in range(4):
        for i in range(4):
            find_current(multi_choice)
            overlap_del(multi_choice)

def overlap_del(multi_choice):
    mul_cho = []
    for i in multi_choice:
        if i not in mul_cho:
            mul_cho.append(i)
            
        else:
            while True:
                trash = random.sample(question,1)
                if trash not in mul_cho:
                    mul_cho += trash
                    break

    for i in range(len(mul_cho)):
        multi_choice[i] = mul_cho[i]

    if len(multi_choice) <4:
        for i in range(4-len(multi_choice)):
            multi_choice += random.sample(question,1)
    
#for i in mul_cho:

retry_find(multi_choice)