print("welcome")
i=0
while(True):

    num1=int(input("enter no"))
    num2=int(input("enter no"))
    num3=(input("enter operation +  -  *  /"))
    if(num1==45 and num2==3 and num3=="*"):

        print("555")
    elif(num1==56 and num2==9 and num3=="+"):
        print("77")
    elif(num1==56 and num2==6 and num3=="/"):
        print("4")
    elif(num3=='+'):
        print(num1+num2)
    elif(num3=='-'):
        print(num1-num2)
    elif(num3=='*'):
        print(num1*num2)
    elif(num3=='/'):
        print(int(num1/num2))
    else:
        print("wrong")
        i=i+1









