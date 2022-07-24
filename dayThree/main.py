print("Welcome to the RollerCoster")
height= int(input("How tall are you"))

if height>=120:
    bill=0
    print("You can ride the RollerCoster")
    age=int(input("What's your age: "))
    if age>=18:
        bill=12
    elif age<18 and age>=12:
        bill=10
    else:
        bill=7
    wants_photo=input(" Do you want a photo taken Y or N")
    if wants_photo=="Y":
        bill+=3
    print(f"Your total is {bill}")
else:
    print("Sorry,you can't take the ride right")