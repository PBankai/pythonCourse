import os
from tkinter.messagebox import QUESTION
from turtle import clear


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bid_continues=True
people_bids={}
while bid_continues:
    name=input("Enter your name: ")
    bid=int(input("Enter the amount: $"))
    people_bids[name]=bid
    answer=input("Do you want to continue Yes/No: ")
    if answer=="No":
        os.system("CLS")
        bid_continues=False
    elif answer=="Yes":
        os.system("CLS")
        bid_continues=True
best_bid=0
best_bidPerson=""
for entry in people_bids:
    if people_bids[entry]>best_bid:
        best_bid=people_bids[entry]
        best_bidPerson=entry
print(best_bidPerson+" the amount was "+ str(best_bid))
