import random

# Initialize
food_list = []
print("Enter your desired dishes: ")

# Prompt for a dish until the user has no more
while True:
    current_line = len(food_list) + 1
    food_string = input("%d]\t" % current_line)

    # Break if user input is (None or ;) and at least two dishes are added
    if (not food_string) or (food_string == ";"):
        if len(food_list) < 2:
            print("Please add at least two dishes.")
        break

    # Add input to the list of dishes
    food_list.append(food_string)

# Select dish
food = random.choice(food_list)

# Print selected dish
print("You should eat %s." % food)
