num = int(input("enter no"))
i= 2
t = 0

while i<num:
    if num % i ==0:
        t = 1
        break
    i = i+1
if t == 1:
    print("NUMBER IS NOT PRIME")
else:
    print("NUMBER IS PRIME")


