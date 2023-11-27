#Enxhi Merkaj 11/26/2023

numbers = []  # Initialize an empty list to store entered numbers
total_sum = 0  # Initialize the total sum variable

while total_sum <= 100:
    user_input = float(input("Enter a number: "))  # Prompt the user to enter a number
    numbers.append(user_input)  # Append the entered number to the list
    total_sum = sum(numbers)  # Calculate the sum of the numbers in the list

print("Entered Numbers:", numbers)
print("Total Sum:", total_sum)
