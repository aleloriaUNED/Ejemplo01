import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


x = 1

while x <= 5:
    print(x)
    x = x + 1

clear()

lista = ['Hola', 'Carro', 'Python', 'UNED', 'e']

for pos in lista:
    print(pos)

for i in range(10):
    print(i)

# for(int = i; i<10; i++)
