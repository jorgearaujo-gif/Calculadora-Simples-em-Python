def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        raise ValueError("Impossível dividir por zero")
    return a / b

def potencia(a, b):
    return a ** b

def raizquadrada(a):
    if a < 0:
        raise ValueError("Impossível calcular raiz quadrada de um valor negativo")
    return a ** 0.5


operacoes = {
    "1": (soma, "Soma"),
    "2": (subtracao, "Subtracao"),
    "3": (multiplicacao, "Multiplicacao"),
    "4": (divisao, "Divisao"),
    "5": (potencia, "Potencia"),
    "6": (raizquadrada, "Raiz Quadrada"),
}

while True:
    print("\nCALCULADORA BÁSICA")
    for codigo, (_, nome) in operacoes.items():
        print(f"{codigo} - {nome}")
    print("0 - Sair")

    escolha = input("Escolha uma das opções: ").strip()

    if escolha == "0":
        print("Saindo da Calculadora")
        break

    if escolha not in operacoes:
        print("Operação inválida")
        continue

    try:
        numero_1 = float(input("Escolha o primeiro valor: "))
        funcao, nome = operacoes[escolha]

        if escolha == "6": # Na ocasião de raiz quadrada, apenas um valor será atribuído e calculado, essa função esclarece isso
            resultado = funcao(numero_1)
        else:
            numero_2 = float(input("Escolha o segundo valor: "))
            resultado = funcao(numero_1, numero_2)

        print(f"O resultado final é: {nome}: {resultado:g}")
    except ValueError as e:
        print(f"Erro: {e}")
    except OverflowError:
        print("Erro: resultado numérico muito grande")
