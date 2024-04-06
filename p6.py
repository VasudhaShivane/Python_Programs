# from array import *
# arr=array('i',[])
# n=int(input("enter the length of array "))
# for i in range(n):
#     x=int(input("enter next element "))
#     arr.append(x)
# print(arr)

# from array import *
# arr=array('u',[])
# n=int(input("enter length of array"))
# for i in range(n):
#
#   nnn=str(input("enter next element"))
#   arr.append(nnn)
# print(arr)

# from array import *
# val=array('i',[10,22,1,234,22,33])
# val=sorted(val)
# print(val)



# from array import *
#
# arr=array('i',[])
# val=int(input("enter the length of array"))
#
# for i in range(val):
#   x=int(input("enter next element"))
#   arr.append(x)
# print(arr)
#
# e=int(input("enter the element to be searched"))
# k=0
# for ef in arr:
#   if ef==e:
#
#     print(k)
#     break
#   k=k+1


# from array import *
# arr=array('i',[])
# a=int(input("enter length of array"))
# for i in range(a):
#   n=int(input("enter next element"))
#   arr.append(n)
# print(arr)
#
# for i in range(-1,-6,-1):
#   print(arr[i],end="")


# def add_sub(a, b):
#     aaa = a+b
#     bbb = a-b
#     return aaa, bbb
#
# result1 , result2 = add_sub(8, 4)
# print(result1, result2)


# def fib(n):
#     count = n
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     else:
#          if n > 0:
#             print(a)
#             print(b)
#             for i in range(2, count):
#                     c = a + b
#                     a = b
#                     b = c
#                     if c < count:
#                            print(c)
#
#          else:
#              print("wrong input")
#
#
# fib(100)

def fact(n):
    if n == 0:
        return 1

    return n * fact(n-1)

result = fact(5)
print(result)









