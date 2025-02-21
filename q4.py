def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
    
    
print(palindrome("0974101607733149676776769413377061014790"))
print(palindrome("4257304920394478392772938744930294037524"))
print(palindrome("7798338247658278460338648728567428338977"))
print(palindrome("2704702208931031198668911301398022074072"))