import random

# Initialize
food_list = []
print("Enter your desired dishes: ")

# Prompt for a dish until the user has no more
while True:
    food_string = input("\t")

    # Break if user input is None and at least two dishes are added
    if not food_string:
        if len(food_list) > 2:
            break
        else:
            print("Please add at least two dishes.")

    # Add input to the list of dishes
    food_list.append(food_string)

# Select dish
food = random.choice(food_list)

# Print selected dish
print("You should eat %s." % food)
