name = "vasudha"
age=19

print("Hello my name is {} and my age is {}".format(name ,age))

print("Hello my name is {n} and my age is {a}".format(n = name , a = age))


n = int(input("enter number of lines"))
for i in range (0,n+1):
    for j in range (0,i):
        print (i , end="")
    print()

print()
# num = int (input ("enter number of lines"))
# for i in range (num):
#     for j in range(0,i):
#         print("$",i)
#     print()

for i in range(1,6):
    for j in range(1,i+1):
        print("$" ,end="")
    print()



for i in range (5,0,-1):
    for j in range(1,i+1):
        print("$" , end="")
    print()

k = 1
for i in range (5,0,-1):
    for j in range(1,i+1):
        print(" "*(i-1),end="")
        if (j == i):
            print("$"*k)
            k=k+1
            
    print()
    
