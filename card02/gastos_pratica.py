from functools import reduce # reduce precisa ser importado

# Categorias
CATEGORIAS = ("Alimentação", "Transporte", "Moradia", "Lazer", "Estudos", "Outros")

# Classe Gasto
class Gasto:
    total_criados = 0 # Atributo da classe, conta todos os gastos

    def __init__(self, descricao, valor, categoria="Outros", dia=1): # Construtor
        self.descricao = descricao
        self.valor = valor # Passa pelo setter
        self.categoria = categoria if categoria in CATEGORIAS else "Outros"
        self.dia = dia
        Gasto.contar()

    @property
    def valor(self): # Lê como atributo
        return self.__valor

    @valor.setter
    def valor(self, novo): # Não aceita valor zero ou negativo
        if novo <= 0:
            raise ValueError("O valor precisa ser maior que zero.")
        self.__valor = float(novo)

    @classmethod
    def contar(cls): # Usa a classe
        cls.total_criados += 1

    @staticmethod
    def moeda(valor): # Não usa classe nem objeto
        return f"R$ {valor:.2f}".replace(".", ",")

    def __str__(self): # Como o gasto aparece no print
        return f"dia {self.dia:02d} | {self.categoria:<12} | {self.descricao:<15} | {Gasto.moeda(self.valor)}"

# Classe Carteira
class Carteira:
    def __init__(self, dono, orcamento):
        self.dono = dono
        self.orcamento = orcamento
        self.gastos = [] # Lista de gastos

    def adicionar(self, *gastos): # *args, recebe um ou vários gastos
        self.gastos.extend(gastos)

    def adicionar_rapido(self, **dados): # **kwargs, cria o gasto pelos nomes
        self.adicionar(Gasto(**dados))

    def total(self):
        return reduce(lambda soma, g: soma + g.valor, self.gastos, 0)

    def situacao(self): # Condicionais
        uso = self.total() / self.orcamento * 100
        if uso > 100:
            return f"Estourou o orçamento ({uso:.0f}%)"
        elif uso >= 80:
            return f"Atenção: {uso:.0f}% do orçamento usado"
        return f"Tranquilo: {uso:.0f}% do orçamento usado"

    def por_categoria(self): # Dicionário com o total de cada categoria
        totais = {}
        for g in self.gastos:
            totais[g.categoria] = totais.get(g.categoria, 0) + g.valor
        return totais

    def categorias_usadas(self): # Conjunto
        return {g.categoria for g in self.gastos}

    def acima_de(self, limite): # filter mantém os maiores que o limite
        return list(filter(lambda g: g.valor > limite, self.gastos))

    def simular_reducao(self, percentual): # map aplica a redução em cada valor
        return list(map(lambda g: round(g.valor * (1 - percentual / 100), 2), self.gastos))

# Funções do menu
def ler_numero(mensagem, tipo=float): # Repete até digitar um número válido
    while True:
        try:
            return tipo(input(mensagem).replace(",", "."))
        except ValueError:
            print("Valor inválido, tente de novo.")

def menu():
    print("\n=== Controle de Gastos ===")
    print("1 - Registrar gasto")
    print("2 - Listar gastos")
    print("3 - Resumo por categoria")
    print("4 - Gastos acima de um valor")
    print("5 - Simular redução")
    print("6 - Situação do orçamento")
    print("0 - Sair")
    return input("Opção: ").strip()

# Programa principal
def main():
    carteira = Carteira(input("Seu nome: ").strip() or "Usuário",
                        ler_numero("Orçamento do mês (R$): "))

    while True:
        opcao = menu()

        if opcao == "0":
            print(f"Até mais, {carteira.dono}! Gastos registrados: {Gasto.total_criados}")
            break

        if opcao not in ("1", "2", "3", "4", "5", "6"):
            print("Opção inválida.")
            continue

        if opcao == "1":
            descricao = input("Descrição: ").strip()
            valor = ler_numero("Valor (R$): ")
            if valor <= 0:
                print("O valor precisa ser maior que zero.")
                continue
            for numero, nome in enumerate(CATEGORIAS, start=1):
                print(f"  {numero} - {nome}")
            escolha = ler_numero("Categoria: ", int)
            categoria = CATEGORIAS[escolha - 1] if 1 <= escolha <= len(CATEGORIAS) else "Outros"
            dia = ler_numero("Dia do mês: ", int)
            carteira.adicionar_rapido(descricao=descricao, valor=valor,categoria=categoria, dia=dia)
            print("Gasto registrado!")

        elif not carteira.gastos:
            print("Nenhum gasto registrado ainda.")

        elif opcao == "2":
            for gasto in carteira.gastos:
                print(gasto)

        elif opcao == "3":
            linhas = [f"  {cat:<12} {Gasto.moeda(v)}" for cat, v in carteira.por_categoria().items()] # List comprehension
            print("\n".join(linhas))
            sem_gasto = set(CATEGORIAS) - carteira.categorias_usadas() # Diferença de conjuntos
            print("Sem gastos:", ", ".join(sorted(sem_gasto)) or "nenhuma")

        elif opcao == "4":
            limite = ler_numero("Acima de (R$): ")
            for gasto in carteira.acima_de(limite):
                print(gasto)

        elif opcao == "5":
            percentual = ler_numero("Reduzir quanto (%)? ")
            novos = carteira.simular_reducao(percentual)
            print("Valores simulados:", [Gasto.moeda(v) for v in novos])
            print("Economia:", Gasto.moeda(carteira.total() - sum(novos)))

        elif opcao == "6":
            print("Total gasto:", Gasto.moeda(carteira.total()))
            print("Saldo:", Gasto.moeda(carteira.orcamento - carteira.total()))
            print(carteira.situacao()) # Exemplo de saída: Tranquilo: 50% do orçamento usado

if __name__ == "__main__":
    main()
