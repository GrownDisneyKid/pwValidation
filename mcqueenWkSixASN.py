#  Created by Justin McQueen
#  CMIS 102:6981
#  24 July 2022
#  This program prompts a user for their password.  It must be between 10 and 20 characters will no spaces
#  There must be at least one digit and one letter.  The program will display errors for the user to correct.


#  function receives the pw and checks that it's between 10 and 20 characters
def pwLenCheck(proposedPW):
    pwLEN = int(len(proposedPW))
    if pwLEN < 10:
        print('ERROR: Your password is less than 10 characters long.')
        return False
    elif pwLEN > 20:
        print('ERROR: Your password is more than 20 characters long.')
        return False
    elif pwLEN <= 20 and pwLEN >= 10:
        print('Your password meets the length requirements.')
        return True


#  function counts the alpha and digits in the pw and ensures minimum requirements are met
def charCheck(proposedPW):
    numCount = 0
    charCount = 0
    for letter in proposedPW:
        if letter.isalpha():
            charCount += 1
    for digit in proposedPW:
        if digit.isdigit():
            numCount += 1
    if numCount < 1:
        print('ERROR: Your password does not contain at least one digit.')
        return False
    elif charCount < 1:
        print('ERROR: Your password does not contain at least one character.')
        return False
    elif numCount >= 1 and charCount >= 1:
        print('Your password meets the character requirements.')
        return True


#  function checks for any spaces in the variable pw.  it checks each position in the string.
def spaceCheck(proposedPW):
    spacesFound = 0
    for position in proposedPW:
        if position == ' ':
            spacesFound += 1
    if spacesFound >= 1:
        print('ERROR: Your password contains spaces.')
        return False
    elif spacesFound == 0:
        print('Your password passes the space check.')
        return True
    elif spacesFound < 0:
        print('ERROR: Something is off on the space check.  Please try again.', spacesFound)
        return False, spacesFound


#  prompts the user to enter a pw and states the requirements.
proposedPW = input('What is the password that you would like to check?  The password must be at least ten character'
                   's long and no more than 15 characters long.  Your password must contain a litter (a-Z and at '
                   'least one number.\n')
#  runs each function
len_check = pwLenCheck(proposedPW)
char_check = charCheck(proposedPW)
space_check = spaceCheck(proposedPW)
#  checks to see if each function returned true
if len_check is True and char_check is True and space_check is True:
    # returns the final results of the password check
    print('Your password is good to go!')
else:
    print('Your password is not sufficient.  Please see the error above and try again.')








