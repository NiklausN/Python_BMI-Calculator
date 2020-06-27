# Provide a Menu
print("Make a selection from the options below.")
print("+--------------------+")
print("|    1 = Standard    |")
print("|    2 = Metric      |")
print("|    3 = Exit        |")
print("+--------------------+")

# Retrieve Input from the User
sel1 = int(input("User: "))

# Execute the Users Selections
if sel1 == 1:

    # Retrieve the Height from the User
    height = float(input("Enter the Height in Feet: "))

    # Error Checking
    if 1 <= height <= 12:

        # Retrieve the Weight from the User
        weight = float(input("Enter the Weight in Pounds: "))

        # Error Checking
        if 1 <= weight <= 1000:

            # Calculate the BMI
            bmi = round(703 * weight / (height * 12) ** 2, 2)

            # Format the Upcoming Result for Weight
            if weight == 1:

                # Assign a Value
                a1 = "pound"

            else:

                # Assign a Value
                a1 = "pounds"

            # Format the Upcoming Result for Height
            if height == 1:

                # Assign a Value
                a2 = "foot"

            else:

                # Assign a Value
                a2 = "feet"

            # Display the Results
            print(f'The BMI of the individual will be {bmi} if the weight is {weight} {a1} and the height is {height} {a2}.')

        else:

            # Provide an Error Message
            print("Error: An invalid input has been made for weight! Please rerun the program and try again.")


    else:

        # Provide an Error Message
        print("Error: An invalid input has been made for height! Please rerun the program and try again.")

elif sel1 == 2:

    # Retrieve the Height from the User
    height = float(input("Enter the Height in Centimeters: "))

    # Error Checking
    if 1 <= height <= 365:

        # Retrieve the Weight from the User
        weight = float(input("Enter the Weight in Kilograms: "))

        # Error Checking
        if 1 <= weight <= 450:

            # Calculate the BMI
            bmi = round(weight / (height / 100)**2, 2)

            # Format the Upcoming Result for Weight
            if weight == 1:

                # Assign a Value
                b1 = "kilogram"

            else:

                # Assign a Value
                b1 = "kilograms"

            # Format the Upcoming Result for Height
            if height == 1:

                # Assign a Value
                b2 = "meter"

            else:

                # Assign a Value
                b2 = "meters"

            # Display the Results
            print(f'The BMI of the individual will be {bmi} if the weight is {weight} {b1} and the height is {height} {b2}')

        else:

            # Provide an Error Message
            print("Error: An invalid input has been made for weight! Please rerun the program and try again.")

    else:

        # Provide an Error Message
        print("Error: An invalid input has been made for height! Please rerun the program and try again.")

elif sel1 == 3:

    # Say Some Last Words
    print("Goodbye! Please come again.")

    # Terminate the Program
    exit(0)

else:

    # Provide an Error Message
    print("Error: An invalid selection has been made! Please rerun the program and try again.")
