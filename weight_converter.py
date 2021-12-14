#This program converts kg (kilograms) to lbs (pounds) and lbs to kg.

print("Enter K for Kilograms")
print("Or enter L for Pounds\n")

while True:

    weight = float(input("Enter weight : "))
    unit = str(input("(K)g or (L)bs? : ")) #user should enter either K or L

    if unit == "K":
        convert = weight / 0.45
        print("Weight in lbs: " + str(convert) + "\n")

    elif unit == "L":
        convert = weight * 0.45
        print("Weight in kg = " + str(convert) + "\n")

    else:
        print("Error. Use 'K' for Kg and 'L' for lbs")