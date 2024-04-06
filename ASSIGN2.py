name = input("Enter name :")
basic_salary = float(input("enter basic salary : "))

DA = basic_salary * 0.12
HRA = basic_salary * 0.15
TA = basic_salary * 0.075
PF = basic_salary * 0.12

gross_salary = basic_salary + DA + HRA + TA
if gross_salary <= 250000:
    tax = 0
    net_salary = gross_salary - PF - tax
elif gross_salary > 250000 and gross_salary <= 500000:
    tax = 0.05 * gross_salary
    net_salary = gross_salary - PF - tax
elif gross_salary > 500000 and gross_salary <= 750000:
    tax = 0.1 * gross_salary
    net_salary = gross_salary - PF - tax
elif gross_salary > 750000 and gross_salary <= 1000000:
    tax = 0.2 * gross_salary
    net_salary = gross_salary  - tax
elif gross_salary > 100000:
    tax = 0.3 * gross_salary
    net_salary = gross_salary - PF - tax
else:
    print("Not Applicable")

print()
print("****************************************************")
print("Employee Details")
print("****************************************************")
print()
print(" NAME OF EMPLOYEE : ",name)
print(" DA : ",DA)
print(" HRA : ",HRA)
print(" TA : ",TA)
print(" PF : ",PF)
print()
print(" BASIC SALARY : ",basic_salary)
print(" GROSS SALARY : ",gross_salary)
print(" NET SALARY: ",net_salary)
