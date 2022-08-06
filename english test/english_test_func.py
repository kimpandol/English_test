import csv
import random


with open("english test\\단어장\\voca.csv", "r", encoding="UTF-8-sig") as file:
    question = list(csv.reader(file))
    
multi_choice = random.sample(question,4) 

#맞힌 적 있는 문제 삭제 후 다른거 넣기
def find_current(multi_choice):
    while True:
        i = 0
        del multi_choice[i]
        multi_choice += random.sample(question,1)
        overlap_del(multi_choice)
        i+=1
        if i>3: i=0
        if multi_choice[0][2] == "0" and multi_choice[1][2] == "0" and multi_choice[2][2] == "0" and multi_choice[3][2] == "0": break

#중복 제거
def overlap_del(multi_choice):
    mul_cho = []
    for i in multi_choice:
        if i not in mul_cho:
            mul_cho.append(i)
            
        else:
            while True:
                trash = random.sample(question,1)
                if (trash[0] not in mul_cho) and (trash[0][2] == "0"):
                    mul_cho += trash
                    break

    for i in range(len(mul_cho)):
        multi_choice[i] = mul_cho[i]

    if len(multi_choice) <4:
        for i in range(4-len(multi_choice)):
            multi_choice += random.sample(question,1)
