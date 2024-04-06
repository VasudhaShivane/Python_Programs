n = 30
guess = 5
while guess >= 0:
    print("moves left equal to", guess)

    number = int(input("enter no "))
    if number < 30:
        print("you guess too low")
        guess = guess - 1

    elif number > 30:
        print("you guess too high")
        guess = guess - 1
    else:
        print("no is 30")
        print("congrats you win")
        break

    if guess == 0:
        print("out of moves")
        break
