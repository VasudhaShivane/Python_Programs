a = int(input("enter 1st no"))
b = int(input("enter 2nd no"))
c = int(input("enter 3rd no"))

l = a if a>b and a>c else b if b>a and b>c else c
print('largest no is ', l)