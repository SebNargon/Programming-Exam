birthd = "26-12-2004" # Example birthday, my own
def daycounter(birthday):
    elements = birthday.split("-") # Isolate the parts of my birthday
    year = int(elements[2]) # Isolate the year
    currenty  = 2025 # Establish current year, can't import so assume 2025
    difference = ((currenty-1) - (year+1)) * 365 # Calculate the difference in days between the two years
    for y in range(year+1, currenty): # For each year between my birth year and the current year
        if y % 4 == 0: # account for leap years
            difference += 1
        if y % 100 == 0: # Account for exception to the leap years
            difference -= 1
            if y % 400 == 0: # Account for the exception to the exception (https://www.rmg.co.uk/stories/topics/which-years-are-leap-years-can-you-have-leap-seconds#:~:text=What%20is%20a%20leap%20year,year%2C%20although%201900%20was%20not.)
                difference += 1
    return difference # Return the difference
print(daycounter(birthd)) # Call the function and print the result to check if it is correct