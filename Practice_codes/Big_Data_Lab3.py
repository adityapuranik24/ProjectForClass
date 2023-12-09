qty = int(input("Enter any value: "))
if qty > 200:
    print("Welcome to first condition")
    print("Value > 200")
    print("You get 75% discount")


    if qty > 100:
        print("Value > 100")
        print("You get 50% discount")

    elif qty>50:
        print("Value > 50")
        print("You get 20% discount")

else:
    print("Thankyou for shopping")