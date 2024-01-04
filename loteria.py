import random
def loteria_numeros():
    return random.randint(1, 60)

#armazenar 6 variaveis com cada numero:

num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0

for i in range(1):
    num1 = random.randint(1, 60)
    num2 = random.randint(1, 60)
    num3 = random.randint(1, 60)
    num4 = random.randint(1, 60)
    num5 = random.randint(1, 60)
    num6 = random.randint(1, 60)
    print(f'O primeiro numeros sorteados é: {num1}')
    print(f'O segundoé: {num2}')
    print(f'O terceiro é: {num3}')
    print(f'O quarto é: {num4}')
    print(f'O quinto é: {num5}')
    print(f'O sexto é: {num6}')
    print(f'Esses são os possivéis números da mega by Victor.'
         f'Criei sozinho esse codigo, usando pycharm.')



