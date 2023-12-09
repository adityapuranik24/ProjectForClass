# Initialize an empty list to store unique words
word_list = []

# Input loop
print()
while True:

    # USER will enter word here
    word = input("Enter a Word: ").strip()

    # Check for a blank line to exit the loop
    if word == "":
        if word_list:
            break
        else:
            print("\nPlease enter any Word...\n")
            continue

    # Check if the word is not already in the list and add it if unique
    if word not in word_list:
        word_list.append(word)

# Display unique words in the order they were entered
print("\nEntered Words are:-\n")
for word in word_list:
    print(word)