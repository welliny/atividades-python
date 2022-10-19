import random
number = random.randint(0,5)
print(number)

number2 = int(input("Qual o número de 0 a 5? "))

if(number == number2):
    print("Você adivinhou, o número é ", number)
else:
    print("Tente novamente")
