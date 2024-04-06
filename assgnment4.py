def calculate_room_cost(room_type, num_people, is_company_enrolled, is_over_60):

    base_cost_deluxe = 2500
    base_cost_executive = 5000

    # Pricing policy
    pricing_policy = {
        'deluxe': {2: base_cost_deluxe, 3: 3500, 4: 4500},
        'executive': {2: base_cost_executive, 3: 5500, 4: 6500}
    }

    additional_cost_per_person = 1000

    # Calculate the cost based on room type and number of people
    if num_people in pricing_policy[room_type]:
        cost = pricing_policy[room_type][num_people]
    else:
        cost = pricing_policy[room_type][4] + (num_people - 4) * additional_cost_per_person

    # Apply discounts
    if is_company_enrolled:
        cost *= 0.8  # 20% discount for company-enrolled customers

    if is_over_60:
        cost *= 0.85  # 15% discount for customers over 60

    return cost


def print_room_cost():
    print("1. Calculate Room Cost")
    print("2. Quit")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        room_type = input("Enter room type (deluxe or executive): ")
        num_people = int(input("Enter number of people: "))
        is_company_enrolled = input("Is the company enrolled with the hotel? (yes or no): ").lower() == 'yes'
        is_over_60 = input("Is the customer over 60 years old? (yes or no): ").lower() == 'yes'

        cost = calculate_room_cost(room_type, num_people, is_company_enrolled, is_over_60)
        print("Room Cost: {} RS".format(cost))
    elif choice == '2':
        print("Thank you for using the program!")
    else:
        print("Invalid choice! Please try again.")
        print_room_cost()


# Main program
print("Welcome to the Hotel SHREE")

while True:
    print()
    print_room_cost()

    if input("Do you want to calculate another room cost? (yes or no): ").lower() != 'yes':
        break
