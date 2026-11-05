from functools import reduce # reduce precisa ser importado

# Funções
def saudacao(nome="pessoa"): # Parâmetro com valor padrão
    print(f"Olá, {nome}!")

saudacao() # Saída: Olá, pessoa!
saudacao("Ana") # Saída: Olá, Ana!

def soma(a, b):
    return (a + b) # Devolve o valor

print(soma(2, 3)) # Saída: 5

def boa_tarde():
    print("versão 1")

def boa_tarde(): # Não tem sobrecarga, substitui a anterior
    print("versão 2")

boa_tarde() # Saída: versão 2

# *args e **kwargs
def soma_tudo(*nums): # Recebe como tupla
    return sum(nums)

def aluno(**dados): # Recebe como dicionário
    return f"{dados['nome']} tirou {dados['nota']}"

print(soma_tudo(1, 2, 3, 4)) # Saída: 10
print(aluno(nome="Pedro", nota=8)) # Saída: Pedro tirou 8

# Função como objeto
def soma(a, b):
    return a + b

somar = soma # Função guardada em variável
print(somar(2, 3)) # Saída: 5

def operacao(fn, a, b): # Função recebida como parâmetro
    return fn(a, b)

print(operacao(soma, 10, 5)) # Saída: 15

def soma_parcial(a): # Retorna outra função
    def concluir(b):
        return a + b
    return concluir

soma_um = soma_parcial(1)
print(soma_um(2), soma_um(3)) # Saída: 3 4

# Lambda, map, filter e reduce
dobro = lambda x: x * 2 # Função de uma linha
print(dobro(5)) # Saída: 10

notas = [6.4, 7.2, 5.4, 8.4]
print(list(map(lambda n: n + 1, notas))) # Saída: [7.4, 8.2, 6.4, 9.4]
print(list(filter(lambda n: n >= 7, notas))) # Saída: [7.2, 8.4]
print(reduce(lambda a, b: a + b, notas)) # Saída: 27.4

alunos = [{"nome": "Ana", "nota": 7.2}, {"nome": "Breno", "nota": 6.1}]
aprovados = list(filter(lambda a: a["nota"] >= 7, alunos))
print([a["nome"] for a in aprovados]) # Saída: ['Ana']

# List comprehension
print([n + 1 for n in notas if n >= 7]) # Saída: [8.2, 9.4]

# Classes
class Produto:
    def __init__(self, nome, preco, desconto=0): # Construtor
        self.nome = nome # self é o próprio objeto
        self.__preco = preco # __ deixa privado
        self.desconto = desconto

    @property
    def preco(self): # Lê como atributo
        return self.__preco

    @preco.setter
    def preco(self, novo): # Valida a alteração
        if novo > 0:
            self.__preco = novo

    def preco_final(self): # Método
        return self.__preco * (1 - self.desconto)

caneta = Produto("Caneta", 10, 0.1)
caneta.preco = -5 # Ignorado pelo setter
print(caneta.nome, caneta.preco, caneta.preco_final()) # Saída: Caneta 10 9.0

class Carro:
    def __init__(self):
        self.__velocidade = 0

    @property
    def velocidade(self):
        return self.__velocidade

    def acelerar(self): # Aumenta 5
        self.__velocidade += 5
        return self.__velocidade

    def frear(self): # Diminui 5
        self.__velocidade -= 5
        return self.__velocidade

# Herança
class Uno(Carro): # Herda tudo da classe Carro
    pass

class Ferrari(Carro): # Herda e muda o acelerar
    def acelerar(self):
        super().acelerar() # super() chama o método da classe pai
        return super().acelerar()

uno = Uno()
print(uno.acelerar(), uno.acelerar(), uno.frear()) # Saída: 5 10 5

ferrari = Ferrari()
print(ferrari.acelerar(), ferrari.acelerar(), ferrari.frear()) # Saída: 10 20 15

# Membros de classe
class Contador:
    total = 0 # Atributo da classe

    @classmethod
    def incrementar(cls): # Usa a classe
        cls.total += 1
        return cls.total

    @staticmethod
    def mais_um(n): # Não usa classe nem objeto
        return n + 1

print(Contador.incrementar(), Contador.mais_um(99)) # Saída: 1 100
