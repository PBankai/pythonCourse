from platform import machine
import random
from tkinter import image_names
import My_module
""" love_score= random.randint(0,1)
if love_score<1:
    print("Head")
else:
    print("Tails") """
""" name_string=input("Give me the names separated by commna. ")
name=name_string.split(",")
print(f"The one who pays is {name[random.randint(0,(len(name)-1))]}") """

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images_game= [scissors, rock, paper]
print(" Going to play scissors, rocks or paper")
machine_value=random.randint(1,3)
value=int(input("What do you chose: 1 for scissors, 2 for rock and 3 for paper: "))
print(images_game[value-1]+images_game[machine_value-1])
if machine_value == 1 and value == 2:
    print("You win")
elif machine_value == 2 and value == 3:
    print("You win")
elif machine_value == 3 and value == 1:
    print("You win")
elif machine_value == value:
    print("It's a draw")
else:
    print("You lose")
