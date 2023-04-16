# Greetings
print("Welcome to the TIP CALCULATOR")
# Get bill amount
billTotal = int(input("What was the total bill amount?\n"))
# Get percentage
percentTip = int(input("What percentage would you like to tip?\n"))
# Get number of people
numPeople = int(input("How many people are splitting the bill?\n"))
# Get percentage to actual percent
percentage = percentTip / 100
# Calculate tip amount
tipAmount = billTotal * percentage
# Get bill total with tip
billTotalWithTip = billTotal + tipAmount
# Bill per person
billPerPerson = billTotalWithTip / numPeople
# Round total amount
finalAmount = "{:.2f}".format(billPerPerson)
# Display amount
print(f"Each person should pay: ${finalAmount}")