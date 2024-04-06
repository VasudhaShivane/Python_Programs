"""
#var1=100
#var2=200
#print(var1+var2)
print("enter first number")
num1=input()
print("enter second number")
num2=input()
print("sum of these numbers is",int(num1)+int(num2))

# Typecasting in Python :
abc = 5
abc2 = '45'
abc3 = 55.95
xyz = 5.0

abc4=int(abc2)

print(abc+abc4) # Output : 50
print(abc+int(abc2)) # Output : 50

print(float(abc)+xyz) # It will add 5.0 + 5.0 and will return 10.0

print(str(abc)+45) # It will give an error as abc has been changed into string.


str1="hello i am starting now"
print(str1[1:5:2])
print(len(str1))
print(str1.count("a"))
print(str1.replace("a","s"))
print(str1.upper())
print(str1.capitalize())

"""

#numbers = [2,28,5,9,10,33,60]
#numbers.sort()
#numbers.reverse()
#print(numbers)
#print(numbers[0:6])
#print(min(numbers))
#print(max(numbers))
#numbers.append(66,)
#print(numbers)
#str1="hello i am starting now"
#print(str1)



#d1={}
#print(type(d1))
#d2={"hi":"hello","hey":"what" }
#print(d2)
#del d2["hi"]
#print(d2)
#d2.update({"hhii":"what"})
#print(d2)
#print(d2.get("hi"))
#print(d2.keys())
#print(d2.items())
#print(d2.values())

d3={"mutable" : "changable","variable":" whose value changes","constant":"whose value doesnt change","set":"set of something"}
print(d3)
print("enter your word ")
w1=input()
print(d3[w1])

#l=[1,2,3,4,5]
#print(type(l))
#l1={1,2,3}
#print(type(l1))
#l2=(11,22,33)
#print(type(l2))

#print("enter your age")
#age=int(input())

#if age > 18 :
 #   print("you are illigeble")
#elif age==18:
 #   print("cannot decide")
#else:
 #   print("you are not illigeble")



