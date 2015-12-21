import random

# Initialize
food_list = []
running = True


# Tries to stop running. offset is used when the program will receive another input
def stop_running(offset):
    global running

    # Stop running if the user has input two or more dishes
    if (len(food_list) + offset) > 1:
        running = False
    else:
        print("Please input at least two dishes.")

# Program start

print("Enter your desired dishes: ")

# Prompt for a dish until the user has no more
while running:
    current_line = len(food_list) + 1
    food_string = input("%d]\t" % current_line)

    # Verify the string and stop the program if conditions are met
    if len(food_string) > 0:

        # Exit the program when the user inputs a period (.)
        if food_string == ".":
            raise SystemExit("Stopping program.")

        # Stop program when the user enters a semicolon (;)
        if food_string[-1] == ";":

            # Add the value when the user has input text
            if len(food_string) > 1:
                food_string = food_string[:-1]
                stop_running(1)
            else:
                stop_running(0)
                continue
    else:
        stop_running(0)
        continue

    # Add input to the list of dishes
    food_list.append(food_string)

# Select dish
food = random.choice(food_list)

# Print selected dish
print("You should eat %s." % food)
