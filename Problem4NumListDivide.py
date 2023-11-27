#Enxhi Merkaj 11/26/2023

counter = 0  # Initialize the counter
tens = []  # Initialize the list to store values divisible by 10

while counter <= 50:
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1

print("Values in the 'tens' list:", tens)
