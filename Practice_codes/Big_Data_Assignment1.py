#1
# # Enter number of Widget & Gizmo
# widget = int(input("Enter the number of widgets= "))
# gizmo = int(input("Enter the number of gizmo= "))
# # Default weight of widget & gizmo
# widget_weight = 75
# gizmo_weight = 112
# # Total weight
# total_weight = (widget*widget_weight) + (gizmo*gizmo_weight)
# print("Total Weight of orders = ",total_weight)


#2

# initial_bal = float(input("Enter the balance in customer account = "))
# # Interest per year
# interest = 0.04
# # Calculating interest in consecutive years
# bal_after_1year = initial_bal + (initial_bal * interest)
# bal_after_2year = bal_after_1year + (bal_after_1year * interest)
# bal_after_3year = bal_after_2year + (bal_after_2year * interest)
# print("Balance after 1st Year = $",round(bal_after_1year, 2))
# print("Balance after 2nd Year = $",round(bal_after_2year, 2))
# print("Balance after 3rd Year = $",round(bal_after_3year, 2))


#3
# # Taking height as input from user
# height_feet = int(input("Enter height in feet = "))
# height_inches = int(input("Enter height in inches = "))
# # Calculating and converting height into cm
# total_inches = (height_feet*12) + height_inches
# height_centi = total_inches*2.54
# print("Height in centimeters = ", round(height_centi, 2))

#4

# cents = int(input("Enter the amount in cents= "))
# # $2 coins or toonies can be given
# toonies = int(cents/200)
# cents = (cents%200)
# # $1 coins or loonies can be given
# loonies = int(cents/100)
# cents = (cents%100)
# # 25 cents coins or quarters can be given
# quarters = int(cents/25)
# cents = (cents%25)
# # 10 cents coins or dimes can be given
# dimes = int(cents/10)
# cents = (cents%10)
# # 5 cents coin or nickles can be given
# nickles = int(cents/5)
# cents = (cents%5)
# #No of remaining cents are equal to pennies
# pennies = cents
# print("Toonies = ", toonies)
# print("Loonies = ", loonies)
# print("Quarters = ", quarters)
# print("Dimes = ", dimes)
# print("Nickles = ", nickles)
# print("Pennies = ", pennies)
#
