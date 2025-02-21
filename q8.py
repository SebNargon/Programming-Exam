def checkwebsite(website): # Function to check if the website is valid
    """Accepts a website as parameter, and checks if it would be a valid url or not

    Args:
        website (str): the website to be checked 

    Returns:
        bool: if the website is valid or not
    """
    if website.startswith("https://"): # If the website starts with https://
        if website[8] == "w" and website[9] == "w" and website[10] == "w": # If the url includes www. then it will have at least two dots in the url
            return website.count('.') >= 2 and " " not in website # Count the number of dots in the url, and check if there are any spaces
        elif website[8] != "w" or website[9] != "w" or website[10] != "w": # Doesn't have www, so at least one dot must be in the url
            return website.count('.') >= 1 and " " not in website  # Count the number of dots in the url, and check if there are any spaces
        if " " in website or website.count('.') < 1: # If there are spaces in the url, or there are no dots
            return False # Return False
    elif website.startswith("http://"): # If the website starts with http://
        if website[7] == "w" and website[8] == "w" and website[9] == "w": # If the url includes www. then it will have at least two dots in the url
            return website.count('.') >= 2 and " " not in website # Count the number of dots in the url, and check if there are any spaces
        elif website[7] != "w" or website[8] != "w" or website[9] != "w": # Doesn't have www, so at least one dot must be in the url
            return website.count('.') >= 1 and " " not in website # Count the number of dots in the url, and check if there are any spaces
        if " " in website or website.count('.') < 1:    # If there are spaces in the url, or there are no dots
            return False # Return False
    else: # If the website doesn't start with either http:// or https://
        return False # Return False
# Test cases
url = "https://www.google.com"
print(checkwebsite(url)) # True
url = "http://www.google.com"
print(checkwebsite(url)) # True
url = "http://google.com"
print(checkwebsite(url)) # True
url = "https://google.com"
print(checkwebsite(url)) # True
url = "https://www.googlecom"
print(checkwebsite(url)) # False, only one dot with www
url = "htt//www.google.com"
print(checkwebsite(url)) # False no p colon
url = "http://googlecom"
print(checkwebsite(url)) # False no dot
