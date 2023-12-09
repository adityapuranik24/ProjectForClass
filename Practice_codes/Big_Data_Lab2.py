# name = input("Enter your Name= ")
# age = input("Enter your Age=")
# print("Hello ", name)

# length = float(input("Enter room length in meters="))
# width = float(input("Enter room length in meters="))
# print("Area in meters is = ", length*width,"meters")

# length = float(input("Enter farm length in feet="))
# width = float(input("Enter room width in feet="))
# Area = length*width
# Acre = 43560
# print("Area in acres = ", Area/Acre,"Acres")


# bot1= input("Enter number of bottles of 1L or less  = ")
# bot2= input("Enter number of bottles of 1L or more  = ")
# amount1= float(float(bot1)*(.10))
# amount2= float(float(bot2)*(.25))
# total= amount1 + amount2
# print("Total amount is $",total)

meal= float(input("Enter meal amount = "))
tax = float(0.13)
tip = float(0.18)
tax_on_meal = meal*tax
total_tip = meal*tip
total_amount = meal+tax_on_meal+total_tip
print("Total amount =","$",round(total_amount, 2))
print("Total tax =","$",round(tax_on_meal, 2))
print("Total tip =","$",round(total_tip, 2))