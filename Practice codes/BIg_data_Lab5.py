# for i in range(5,100):
#     if i%7==0 and i % 5 != 0:
#         print(i)

total_people = int(input("Enter total no of people ="))
age = []
total_cost = 0
for j in range(total_people):
    ind_age = int(input("Enter the age of each individual ="))
    age.append(ind_age)
print(age)

for i in age:
    if i<=2:
        cost = 0.00
    elif 3<=i<=12:
        cost= 14.00
    elif 65<=i<=100:
        cost = 18.00
    else:
        cost = 23.00
    print(total_cost)
    total_cost += cost
    print(total_cost)
print("Total Cost =", round(total_cost, 2))