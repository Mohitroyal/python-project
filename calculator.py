a=int(input("enter the number: "))
b=int(input("enter the number: "))
choice = int(input("enter the number  of yout choice: "))
print("1.add,2.sub,3.multi,4.div")
match choice:
    case 1:
        print(f"you choose addition {a+b}")
    case 2:
        print(f"you choose subtraction {a-b}")  
    case 3:
        print(f"youe choose multiplaction {a*b}") 
    case 4:
        print(f"youe choose division {a/b}") 
