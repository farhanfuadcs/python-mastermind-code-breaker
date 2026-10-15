import random 

COLORS=['R','G','B','Y','W','O']
CODELENGTH=4

def easy():
    TRIES=10
    return TRIES

def medium():
    TRIES=7
    return TRIES

def hard():
    TRIES=5
    return TRIES


def generate_code():
    code=[]
    for color in range(CODELENGTH):
        colorchoice=random.choice(COLORS)
        code.append(colorchoice)

    return code 


def guess_code():
    while True:
        guess=input("Enter your guess (with space): ").upper().split(" ")
        if len(guess)!=CODELENGTH:
            print(f"Code length is {CODELENGTH} ! ")
            continue
        for color in guess:
            if color not in COLORS:
                print(f"Invalid Color: {color}")
                break
        else:
            break
    return guess


def position_check(guess,code):
    color_count={}
    correct_position=0
    incorrect_position=0

    for color in code:
        if color not in color_count:
            color_count[color]=0
        color_count[color]+=1


    for guesscode,realcode in zip(guess,code):
        if guesscode==realcode:
            correct_position+=1
            color_count[guesscode]-=1


    for guesscode,realcode in zip(guess,code):
        if guesscode in color_count and color_count[guesscode]>0:
            incorrect_position+=1
            color_count[guesscode]-=1


    return correct_position,incorrect_position







def main():
    code=generate_code()
    try:
        lvl=input("Choose Level\n1.Easy\n2.Medium\n3.Hard\nChoose Between (1-3): ")
        if lvl=="1":
            TRIES=easy()
        elif lvl=="2":
            TRIES=medium()
        elif lvl=="3":
            TRIES=hard()


        for attempts in range(TRIES):
            guess=guess_code()
            correct,incorrect=position_check(guess,code)
            if correct==CODELENGTH:
                print(f"You won and you take {attempts+1} attempts")
                break
            else:
                print(f"Correct Position: {correct} | Incorrect Position: {incorrect}")

        else:
            print(f"You lose!\nThe code was: {code}")
    except:
        print("Something is wrong!")




main()