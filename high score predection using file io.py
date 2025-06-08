import random
def game():
    print("your playing a game ")
    score = random.randint(1, 55)
    print(f"your score{score}")
    with open("hiscore.txt") as f:
        hiscore=f.read(score)
        if(hiscore !=""):
            hiscore=int(hiscore)
        else:
              hiscore=0
              print(f"your score is {score: }")
    if(score>hiscore):
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
game()