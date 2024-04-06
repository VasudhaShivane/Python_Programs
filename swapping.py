# a = int(input("enter first number "))
# b = int(input("enter second number "))
# temp = 0
# temp = a
# a = b
# b = temp
#
# print("a = ",a)
# print("b= ",b)

a = int(input("enter first number "))
b = int(input("enter second number "))
print("BEFORE SWAPPING")
print("a= ", a)
print("b =", b)

b = a + b
a = b - a
b = b - a

print("AFTER SWAPPING")
print("a= ", a)
print("b =", b)
