import random

def generate_order():
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    random.shuffle(alphabet)
    return "".join(alphabet)

 print(generate_order())
