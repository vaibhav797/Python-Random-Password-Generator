import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the Random Password Generator!")
n_letters = int(input("How many letters would you like in your password?\n"))
n_numbers = int(input("How many numbers would you like?\n"))
n_symbols = int(input("How many symbols would you like?\n"))

password_list = []
password = ""


for char in range(1,n_letters+1):
    password_list += random.choice(letters)


for char in range(1,n_numbers+1):
    password_list += random.choice(numbers)

for char in range(1,n_symbols + 1):
    password_list += random.choice(symbols)

random.shuffle(password_list)


for char in password_list:
    password += char

print("Your password can be: ", password)