import random

alpha_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

new_alphabet = ""

for i in range(len(alpha_alphabet)):
    letter = random.choice(alpha_alphabet)
    new_alphabet += letter
    alpha_alphabet.remove(letter)

print(new_alphabet)