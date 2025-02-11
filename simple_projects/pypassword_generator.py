# This is a simple python script that was made in 100 Days Of Code Couse on day 5
import random
lista_az_minusculas = [chr(letra) for letra in range(ord('a'), ord('z') + 1)]
lista_az_maiuscula = [chr(letra) for letra in range(ord('A'), ord('Z') + 1)]
letters = lista_az_maiuscula + lista_az_minusculas
symbols = ['!','#','$','%','&','(',')','*','+']

numbers = []
for i in range (0,10):
    numbers.append(f"{i}")

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_letters = random.choices(letters, k=nr_letters)
random_symbols = random.choices(symbols, k=nr_symbols)
random_numbers = random.choices(numbers, k=nr_numbers)
password_list = random_letters+random_numbers+random_symbols
random.shuffle(password_list)

random_password = ''
for i in range(len(password_list)):
    random_password += password_list[i]
print(random_password)
