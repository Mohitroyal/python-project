p1 = "hi click this"
p2 = "subscribe" 
p3 = "you won a jackpot"
message = input("enter the text: ")
if((p1 in message)) or (p2 in message)or (p3 in message):
    print("spam")
else:
    print("not spam")
