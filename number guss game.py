import random
computer= random.choice([1,10])
user = int(input("enter the number form 1 to 10 : "))
if(user>10):
    print("invalid")
elif(computer == user):
    print(f"you choose {user} and computer choose {computer} you win")
elif(computer>user):
    print(f"you choose {user} and computer choose {computer}  you lose")
else:
    print(f"you choose {user} and computer choose {computer}  you win")
    