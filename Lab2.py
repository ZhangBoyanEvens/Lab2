def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    # Calculate BMI
    bmi = weight / (height * height)
    print("Your BMI is: " + str(round(bmi, 2)))

    # Classify BMI result
    if bmi < 18.5:
        print("Weight classification: Under Weight")
    elif bmi <= 25.0:
        print("Weight classification: Normal Weight")
    else:
        print("Weight classification: Over Weight")

# Run the function
calculate_bmi(weight=57, height=1.73)
