days = int(input("Enter days"))

year = days // 365
days = days % 365

month = days // 30
days = days % 30

print("YEAR =", year)
print("MONTH =", month)
print("DAYS =", days)
