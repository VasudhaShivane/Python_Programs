a = 100
b = 4

print('Arithmetic operators')
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

print()
print('concatination')
print('good  ' + 'morning')

print('multiplication')
print('good' * 3)

print('RELATIONAL OPERATORS')
print()
print('a > b', a>b)
print('a<=b',a<=b)

print()
print("LOGICAL OPERATORS")
print()
print('a and b =',a and b )
print('0 and 10 = ', 0 and 10)

print()
print('100 or 4=',a or b)
print('4 or 100 = ', 4 or 100)
print()
print('not 10= ',not 10)
print('not True=', not True)
print('not 0=',not 0)

print()
print('ASSIGNMENT OPERATOR')
print(a+2)
print()
print("BITWISE OPERATORS")
print('0 ^ 1=',0^1)
print('0 | 1=',0|1)
print('0 & 1=',0&1)

print()
print('CONDITIONAL OPERATORS')
l = a if a>b else b
print('largest no is = ',l)

no = a if a%2==0 else b
print('Even number =',no)

print()
print("MEMBERSHIP OPERATOR")
str= 'good morning'
print('good' in str)
print('hjbhjv' in str)
print('sdbdu' not in str)

print()
print('IDENTITY OPERATORS')
print(a is b)
print(a is not b)

print()
print("good")
print("morning")
print("good" ,end=' ')
print("evening")
print('a=%d' %a)