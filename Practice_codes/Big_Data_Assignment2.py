# # Get the name of the month from the user
# month = input("Enter the name of a month: ")
# # Define a dictionary to map month names to the number of days
# month_days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31,
#     'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31
# }
#
# # Check if February has 28 or 29 days (leap year)
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     month_days['February'] = 29
#
# # Display the number of days in the entered month
# if month in month_days:
#     print(month, "has", month_days[month], "days.")
# else:
#     print("Invalid month name. Please enter a valid month.")

#Get the sound level from the user
sound_level = int(input("Enter the level of noise= "))
noise_levels = {'jackhammer': 130, 'Gas lawnmower': 106, 'Alarm clock': 70, 'Quiet room': 40
}
#Check for the sound level match in the dict
for noise, level in noise_levels.items():
    if sound_level == level:
        print("The sound level is similar to", noise)
#Display the msg according to the sound level
if sound_level<40:
    print("The sound level is quieter than a quiet room")
elif sound_level> 130:
    print("The sound level is noiser than a jackhammer")
elif 106<sound_level<130:
    print("The sound level is between jackhammer and gas lawnower")
elif 70<sound_level<106:
    print("The sound level is between alarm clock and gas lawnower")
elif 40<sound_level<70:
    print("The sound level is between quit room and alarm clock ")