# Write a Python program to count the number of vowels in a given string.
# Ask the user to input a string

type_text = input("Enter a Text: ")

count = 0

for character in type_text:
    if character in "aAeEiIoOuU":
        count += 1

print("Vowel counts:", count)
