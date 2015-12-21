import random

# Initialize
food_list = []
print("Enter your desired dishes: ")

# Prompt for a dish until the user has no more
while True:
    food_string = input("\t")

    # Break if user input is None
    if not food_string:
        break

    # Add input to the list of dishes
    food_list.append(food_string)

# Select dish
food = random.choice(food_list)

# Print selected dish
print("You should eat %s." % food)
