print("Hello, welcome to the tip calculator")

bill_total = input("How much was your bill? ")

total_eaters = input("How many people in your party? ")

tip_percentage = input("What percentage would you like to tip? ")

tip_total = int(bill_total) / int(total_eaters) * (int(tip_percentage) / 100)

print(f'You each tip: ${tip_total}')
