import random

#computador
number = random.randint(0,10)
print(number)

#usuário
number2 = int(input("Qual o número de 0 a 10? "))

while number2 != number:
    print("Você errou! Tente novamente :D")
    number2 = int(input("Qual o número de 0 a 10? "))

print("Parabéns, você acertou!!!")