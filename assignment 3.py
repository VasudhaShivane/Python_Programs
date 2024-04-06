# Program to print whether the given number is odd or even

if __name__ == "__main__":
    num = int( input("Enter a number : "))

    if num%2 == 0:
        print("%d is an even number"%num )
    else:
        print("%d is an odd number" %num)



if __name__ == "__main__":
    num1 = int( input("Enter a number to check whether it is divisible by 7 or 3 : "))
    
    if num1%3 == 0 or num1%7 == 0:
        if num1%3 == 0:
            print("%d is divisible by 3" %num1)
        else:
            print("%d is divisible by 7" %num1 )
    else:
        print("Your given number is not divisible by 7 or 3")



if __name__ == "__main__":
    
    l2 = list(filter(lambda x:x%2==0, range(1,101)))
    print("List of even numbers is :")
    print(l2)


if __name__ == "__main__":

    l3 = list(filter(lambda a : a%2 != 0 , range(1,101)))
    print("List of odd numbers is :")
    print(l3)