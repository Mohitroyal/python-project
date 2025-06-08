import random
computer = random.choice([-1, 0, 1])
your = input("Enter your choice from s, w, g: ")  
yourDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1 : "snake",-1 : "water",0: "gun"}
you = yourDict[your]
print(f"your choice {reverseDict[you]} \ncomputer choice {reverseDict[computer]}")



if (computer == you):
        print(f"Draw because you choose {you}computer choose{computer}")
elif (computer == -1 and you== 1):
        print("You win because you choose {you}computer choose{computer}")
elif (computer == -1 and you== 0):
        print("You lose because you choose {you}computer choose{computer}")
elif (computer == 1 and you== -1):
        print("You lose because you choose {you}computer choose{computer}")
elif (computer == 1 and you)== 0:
        print("You win because you choose {you}computer choose{computer}")
elif (computer == 0 and you)== -1:
        print("You lose because you choose {you}computer choose{computer}")
elif (computer == 0 and you)== 1:
        print("You lose because you choose {you}computer choose{computer}")
else:
        print("something went wrong")

 