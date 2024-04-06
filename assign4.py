"""print("*** HOTEL SHREE ***")
print("Cost As per rooms ...")
print("1. Delux Room ")
print("2. Executive Room ")

name = input("\n Enter Customer's name : ")
age = int(input("Enter the age of customer : "))
choice = int(input("Enter 1 if Delux \n Enter 2 if Executive "))

if(choice == 1):

    if (age >60):
        cost = (329
                2000 * 0.2)+1000#* (15/100)
        print("Total Cost :" ,cost)
    else:
        cost = (2000 * (20/100)+1000)
        print("Total Cost :" ,cost)

else:

    if (age >60):
        cost = (5000 * (20/100)+1000)#* (15/100)
        print("Total Cost :" ,cost)
    else:
        cost = (5000 * (20/100)+1000)
        print("Total Cost :" ,cost)"""

print("*** HOTEL SHREE ***")
print("Cost As per rooms ...")
print("1. Delux Room : 2000 ")
print("2. Executive Room : 5000 ")

n_people = int(input("Entre the number of people want ot stay in hotel : "))

for i in range(n_people):
    name = input("\n Enter Customer's name : ")
    age = int(input("Enter the age of customer : "))
    totalcost = 0
    discount = 0
    if (age > 60):
        discount = discount + 15
    else:
        discount = discount
    totalcost = totalcost + discount
    if(n_people == 1):
        totalcost = totalcost
    elif(n_people == 2):
        totalcost  = totalcost+2500
    elif (n_people == 2):
        totalcost = totalcost + 3500
    elif (n_people == 3):
        totalcost = totalcost + 4500
    else:
        totalcost = totalcost+1000

print("cost : " ,totalcost)











