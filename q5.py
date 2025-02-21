def patternrecognition(text):
    """Accepts a text and checks how many WORDS begin with the letter C and end with the letters jeb. The function returns the number of such words.

    Args:
        text string: The full text to be checked.

    Returns:
        counter int: The number of words that begin with the letter C and end with the letters jeb.
    """
    start = 0 # Tells the code where to start searching, begin at 0, the first character
    counter = 0 # Counts how many times we find the pattern, beginning at 0 since we haven't found any yet
    while True: # Loop forever until we tell it to break. Could also be done by splitting the text at each space and checking each word.
        start = text.find("C", start) # Finds the first time it sees C, starting from start variable. In the first iteration, it is 0
        if start == -1: #If it doesn't find C, end the code, returning counter as 0
            break # End the loop
        end = text.find(" ",start) # Find the first space after the C, starting from the start variable
        if end == -1: # If it doesn't find a space, it means the C is the last word in the text
            word = text[start:] # Word is then the entire thing from the first C to the end of the text
            if word[-3:] == "jeb": # If the last 3 characters of the word are jeb, add 1 to the counter
                counter += 1 # Add one to the counter
                break # End the loop
        word = text[start:end] # Word is the text from the C to the space
        if word[-3:] == "jeb": # If the last 3 characters of the word are jeb, add 1 to the counter
            counter += 1 # Add one to the counter
        start = end # Start is now the space, so the next iteration will start from the next word
    return counter # Return the counter
text = "Cjheevjeb dshfjdshf Cejhehjeb" # Example text, should return 2

print(patternrecognition(text)) # Call the function and print what it returns to check the answer

