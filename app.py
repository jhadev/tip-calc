print("Hello, welcome to the tip calculator")

total_eaters = int(input("How many people are in your party? "))
tax = float(input("What is the tax rate at the restaurant? "))
divider = ('=========================================================')

# total_eaters = int(total_eaters)
name_list = []


def get_tips():
    if total_eaters > 0:
        for person in range(total_eaters):
            print(f'{divider} \n')
            name = input(f'What is the name of person {person + 1}? ')
            total_spent = input(f"How much was {name}'s meal? ")
            tip_percentage = input(f'What % would {name} like to tip? ')
            values = name, float(total_spent), float(tip_percentage)
            name_list.append(values)
    else:
        print('Nobody ate :(')

    print(f'{divider} \n')
    subtotal = 0
    total_tips = 0

    for tipper in name_list:
        person_name, bill_amount, tip_perc = tipper
        subtotal += bill_amount
        each_tip = bill_amount * (tip_perc / 100)
        total_tips += each_tip
        print(f'\n {person_name} has to tip ${each_tip:.2f}')

    tax_total = subtotal * (tax / 100)
    actual_total = tax_total + subtotal + total_tips
    tip_perc_of_subtotal = (total_tips / subtotal) * 100

    print(f'\n The subtotal is ${subtotal:.2f}')
    print(
        f'\n The tip total is ${total_tips:.2f} at a rate of {tip_perc_of_subtotal:.2f}% ')
    print(f'\n Total tax amount is ${tax_total:.2f}')
    print(f'\n Your total bill including tax is ${actual_total:.2f}')


get_tips()
