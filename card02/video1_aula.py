# Módulos
print(__name__)

import math

from math import sqrt
print(math.pi, sqrt(16))

# Variáveis e tipos
a = 3 # int
b = 4.4 # float
texto = "Sua idade é" # string
idade = 23
print(a + b)
print(f"{texto} {idade}")
print(type(a), type(b), type(texto), type(True))

print("Bom dia " * 3) # Saída: Bom dia Bom dia Bom dia

PI = 3.14 # Constante só por convenção
raio = 10
print("Área:", PI * raio ** 2)

# Coleções
nums = [1, 2, 3] # Lista
nums.append(3)
nums[0] = 100
print(nums, len(nums)) # Saída: [100, 2, 3, 3] 4

nomes = ("Ana", "Bia", "Gui", "Ana") # Tupla
print("Bia" in nomes, nomes.count("Ana")) # Saída: True 2

conjunto = {1, 2, 3, 3} # Conjunto
print(conjunto) # Saída: {1, 2, 3}

aluno = {"nome": "Pedro", "nota": 9.2} # Dicionário
aluno["ativo"] = True
print(aluno["nome"], aluno.get("curso", "Engenharia de Computação")) # Saída: Pedro Engenharia de Computação

# Operadores
x = 3
print(-x, not True) # Saída: -3 False
print(10 + 3, 10 / 3, 10 // 3, 10 % 3, 10 ** 2) # Saída: 13 3.3333333333333335 3 1 100
print(34 % 2 == 0) # Saída: False
print(3 > 4, 3 != 2, 3 == "3") # Saída: False True False

resultado = 2
resultado += 3
print(resultado) # Saída: 5

print(True and False, True or False) # Saída: False True

chuva = False
print("Em casa" if chuva else "Na rua") # Saída: Na rua

# Condicionais
# Em Python os blocos são definidos por identação
nota = 7.5
if nota >= 9:
    print("Quadro de honra")
elif nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# Laços de repetição
for i in range(1, 10, 2): # for contador in (início, fim, passo)
    print(i, end=" ")
print()

produto = {"nome": "Caneta", "preco": 8.80}
for chave, valor in produto.items():
    print(chave, valor) # Saída: nome Caneta preco 8.8

contador = 3
while contador > 0: # Repete enquanto for verdadeiro
    print(contador)
    contador -= 1

for i in [1, 2, 3]:
    pass # não faz nada

for i in range(1, 11):
    if i % 2 == 1:
        continue # Pula os ímpares
    if i == 8:
        break # Sai do laço no 8
    print("par:", i) # Saída: par: 2 par: 4 par: 6
