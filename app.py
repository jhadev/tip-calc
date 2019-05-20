print("Hello, welcome to the tip calculator")

total_eaters = input("How many people in your party? ")
divider = ('=========================================================')

total_eaters = int(total_eaters)
name_list = []


def get_tips():
    if total_eaters > 0:
        for person in range(total_eaters):
            print(divider)
            name = input(f'What is the name of {person + 1}? ')
            total_spent = input(f'What did {name} spend? ')
            tip_percentage = input(f'What % would {name} like to tip? ')
            values = name, float(total_spent), float(tip_percentage)
            name_list.append(values)
    else:
        print('Nobody ate :(')

    print(divider)
    total_bill = 0

    for tips in name_list:
        person_name, bill_amount, tip_perc = tips
        total_bill += bill_amount
        each_tip = bill_amount * (tip_perc / 100)
        print(f'{person_name} has to tip ${each_tip:.2f}')
    print(f'Your bill total is ${total_bill:.2f}')


get_tips()
