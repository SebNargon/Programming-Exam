import random # 
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

#Beginning of own code
print(random_numbers) # Check what the original list is to later compare
iterations = 0 # Initialize the counter for the number of iterations, we need this to go through each element of the list until we hit the end. 
while iterations < len(random_numbers): # While we haven't gone through the entire list
    number = random_numbers[iterations] # Get the number at the current iteration
    if number > 80: # If the number is greater than 80
        random_numbers[iterations] = number * - 1 # Change the number to its negative
        iterations += 1 # Move to the next number
    elif number < 40: # If the number is less than 40. Following code could be simplified as it is only going to be 2 digits max, but this is a better generic solutions that could be used for more conditions with higher numbers. 
        number = str(number) # Change the number to a string
        sumdigit = 0 # Initialize the sum of the digits
        digits = [] # Initialize the list of digits
        for digit in number: # For each digit in the number
            digits.append(digit) # Add the digit to the list
        for digit in digits: # For each digit in the list
            sumdigit += int(digit) # Add the digit to the sum of the digits
        random_numbers[iterations] = sumdigit # Change the number to the sum of the digits
        iterations += 1 # Move to the next number
    else: # If the number is between 40 and 80
        iterations += 1 # Move to the next number
        
print(random_numbers) # Print the new list to check if the changes were made correctly

            