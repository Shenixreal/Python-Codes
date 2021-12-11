import random

symbols = ["!", "@", "#", "$", "%"]
random_symbol = random.choice(symbols)

symbols2 = ["^", "&", "*", "-", "_"]
random_symbol2 = random.choice(symbols2)

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
random_number = random.choice(numbers)

print("")
print("---Password Generator---")
print("")
print("- Use both capital and simple letters to further strengthen your password.")
print("- Enter a number with at least 4 digits.")
print("")

#User inputs
word = str(input("Enter a word of your choice: "))
word2 = str(input("Enter another word of your choice: "))
num = int(input("Enter a number of 4 digits or more: "))

password = str(word) + str(random_number) + str(random_number) + str(random_symbol) + str(word2) + str(random_symbol2) + str(num)

print("\n")
print("Password: " + password)
print("Password length: " + str(len(password))) #Prints the length of the password

#Check if the password is weak or strong based on the number of characters
if len(password) <= 8:
    print("Strength: Weak")
elif len(password) > 8 and len(password) < 12:
    print("Strength: Medium")
elif len(password) > 12 and len(password) < 20:
    print("Strength: Strong")
else:
    print("Strength: Very Strong")

print("")