n = (input("enter the number of letters:"))
counts =0
countd =0
countsp =0
for i in n:
    if i.isalpha():
        counts +=1
    elif i.isdigit():
        countd +=1
    else:
        countsp +=1
print(f"count of all strings is {counts}")
print(f"coutn of all diguts id {countd}")
print(f"count of all spl char is {countsp}")
