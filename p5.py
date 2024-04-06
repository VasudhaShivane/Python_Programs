# f1 = open("pika.txt","r")
# content = f1.read()
# #print(f1.readlines())
# for line in content:
#      print(line)
# f=open("pikachu.txt","a")
# content =f.write("Hi I am testing this write function!!!!!!!!!!!!!!!!!!! \n")


# fff=open("pikachu.txt","r+")
# line=fff.read()
# fff.write("hi hi hi hi hi hi hi \n")
# print(line)
#
# fff.close()


print("Hello!! This is a pattern printing exercise!!")
print("Up to how many rows do you want to print the pattern??")
n = int(input())
print("Enter 1 for forward pattern and 0 for reverse pattern..")
var = bool(int(input()))
if var:
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print("*", end="")
            j = j + 1
        print("")
        i = i + 1
else:
    i = n
    while i >= 1:
        j = i
        while j >= 1:
            print("*", end="")
            j = j - 1
        print("")
        i = i - 1