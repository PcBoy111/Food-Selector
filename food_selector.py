import random

# Initialize
food_list = []
print("Enter your desired dishes: ")

# Prompt for a dish until the user has no more
while True:
    food_string = input("\t")

    # Add input to list of dishes if available
    if food_string:
        food_list.append(food_string)
    else:
        break

# Select dish
food = random.choice(food_list)

# Print selected dish
print("You should eat %s." % food)
