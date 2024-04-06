a = 60
b = 45

print("a= ", a, "b= ", b)
print("1. Addition")
print("2. Subtraction")
print("3. multiplication")
print("4. Division")
print("5. Floor Division")

op = int(input("select which operation you want to perform ..."))

if op == 1:
    print("Subtraction =",a-b)
elif op==2:
    print("Addition =", a + b)
elif op==3:
    print("Multiplication =",a*b)
elif op==4:
    print("Division =",a/b)
else:
    print(("Floor Division =",a//b))

