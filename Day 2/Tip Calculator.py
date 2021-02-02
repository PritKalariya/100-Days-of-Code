print("Welcome to TipCalculator")

bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
num = int(input("How amny people to split the bill? "))

tip_percentage = tip / 100
total_tip_amount = bill * tip_percentage
total_bill_amount = bill + total_tip_amount
bill_per_person = total_bill_amount / num
# final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")