def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("1.add,2.sub,3.multiply,4.divide")
choice =int(input("select option: "))
x = float(input("enter the number 1: "))
y = float(input("enter the number 1: "))
if choice == 1:
       print(f"result is{add(x,y)}")
elif choice == 2:
     print(f"result is{subtract(x,y)}")
elif choice == 3:
     print(f"result is {multiply(x,y)}")
elif choice == 4:
     print(f"result is {divide(x,y)}")
else:
     print("invalid")