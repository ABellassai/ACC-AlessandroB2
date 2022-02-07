#Write a recursive function to sum the first n natural numbers. Where n is a value input by the user
# n = int(input('type the number of numbers you want to add: '))
# def recursive(n):
#     if n == 1:
#         return n
#     else:
#         return n + recursive(n - 1)
# print(recursive(n))

#Write a recursive function to print a string in reverse order
word = str(input('type something: '))
def recursive2(word):
    new_Word = word[-1:len(word)]
    if new_Word == len(word):
        return new_Word
    else:
    return new_Word
print(recursive2(new_Word))

#Write a recursive function to check if a string is a Given a string a palindrome. The string length can
#be >= 0.