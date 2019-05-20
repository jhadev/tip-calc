print("Hello, welcome to the tip calculator")

start_msg = input("Type help for more info or type start to calculate ")

divider = ('=========================================================')

name_list = []


def get_tips():
    total_diners = int(input("How many people are in your party? "))
    tax = float(input("What is the tax rate at the restaurant? "))

    if total_diners > 0:
        for person in range(total_diners):
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
        each_tax_total = bill_amount * (tax / 100)
        full_bill = bill_amount + each_tax_total + each_tip
        print(f'\n {person_name} has to tip ${each_tip:.2f}')
        print(
            f"\n {person_name}'s total including tax and tip is ${full_bill:.2f}")

    tax_total = subtotal * (tax / 100)
    actual_total = tax_total + subtotal + total_tips
    tip_perc_of_subtotal = (total_tips / subtotal) * 100

    print(f'\n The subtotal is ${subtotal:.2f}')
    print(
        f'\n The tip total is ${total_tips:.2f} at a rate of {tip_perc_of_subtotal:.2f}% ')
    print(f'\n Total tax amount is ${tax_total:.2f}')
    print(
        f'\n The total of your bill including tax and tip is ${actual_total:.2f}')


def help():
    # don't forget to finish this.
    help_msg = input(
        f'\n This tool will help you calculate the tips amounts for each diner in your party. \n Each diner can tip at a specific percentage for their meal and the result will show what they have to pay including tax. \n It will also display the full bill total including tax and tip along with the combined tip percentage. \n Type start to begin. ')
    if help_msg == 'start':
        get_tips()
    else:
        print('Goodbye')
        exit()


if start_msg == 'help':
    help()
elif start_msg == 'start':
    get_tips()
else:
    print('Goodbye')
    exit()
