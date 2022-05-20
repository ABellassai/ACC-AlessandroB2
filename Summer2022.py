# Prompt the user to enter a password and store the ...
# value entered in the variable password
password = input("Enter a password: ")
print('Password:', password)

# A variable to store all the lowercase letters in the alphabet
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_CASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# The variables lowercase and uppercase indicate the presence or ...
# absence of lowercase and uppercase characters in the password
lowercase = False # True if password contains a lowercase letter
uppercase = False # True if password contains an uppercase letter
digits = False # True if password contains a digit

# Loop through each character in the password and ...
# check the password for specific characters
for character in password:
    if character in LOWER_CASE_LETTERS:
        lowercase = True
    if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        uppercase = True

# Calculate the score based on the rules

score = 0  #Initialite score 

# Rule 1
if len(password) > 7:
    score = score + 5
elif len(password) < 7 and len(password) > 4:
    score = score + 5
elif len(password) < 4:
    score = score - 2

# Rule 2
if lowercase:
    score = score + 1

# Rule 3
if lowercase and uppercase:
    score = score + 5

# Rule 4
if password.islower() == False:
    score = score + 2

# Rule 5
if password.isalpha() == False:
    score = score + 5

# Rule 6
if password[0].isdigit() == True:
    score = score + 1
if password[-1].isdigit() == True:
    score = score + 1
if password[0].isdigit() == True and password[-1].isdigit() == True :
    score = score + 2
    
# Rule 7
if password.isdigit() == True:
    score = score - 10  
    
# Display the score
print('Score:', score)
