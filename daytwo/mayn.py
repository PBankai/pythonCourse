bill_total=float(input("What was the total of the Bill: "))
number_of_people=int(input("What's the number of persons: "))
tip_percentage=float(input("Enter Tip, percentage 10,12,15: "))
payment_per_person=(bill_total*(1+tip_percentage/100))/number_of_people
final_amount= "{:.2f}".format(payment_per_person)
print(f"Each of you needs to pay $"+final_amount)
