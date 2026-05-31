## Projeto calculadora simples no terminal.
##No python, a variável já assume o tipo automaticamente. Só é necessário declarar tipagem quando precisa converter o que o usuário digitou.
## INPUT sempre irá retornar String.
from functools import reduce 
import operator
import os ## Por uma questõ de estética, importei para conseguir limpar a tela do programa.

## Para treinar funções, gerei uma para limpar o terminal.
def limpar_tela(): ## snake_case
    input ("\nPressione qualquer tecla para voltar...")
    os.system('clear')

operacoes = { ## Utilizando um dicionário para estética.
    1: "ADIÇÃO",
    2: "SUBTRAÇÃO",
    3: "MULTIPLICAÇÃO",
    4: "DIVISÃO"
}

while True: 
    print("===== CALCULADORA EM PYTHON =====")
    print("Escolha sua ação:")
    print("(1) Adição \n(2) Subtração \n(3) Multiplicação \n(4) Divisão \n(5) Sair")
    try:
        resposta = int(input())
    except ValueError:
        os.system('clear')
        print("INVÁLIDO!")
        print("Escolha uma das opções digitando um número de 1-5.")
        limpar_tela()
        continue

    os.system('clear') ## Não utilizei a função limpar_tela() pois quero que a limpeza seja automatica, sem precisar que o usuário solicite.

    numeros = [] #Criação de uma lista para guardar os números a serem calculados.
    if resposta == 5:
        print("Saindo da calculadora...")
        break
        

    else: 
        try:
            print(f"===== {operacoes[resposta]} =====") ## O f no início é uma outra forma de concatenação de Strings.
        except KeyError:
            os.system('clear')
            print("INVÁLIDO!")
            print("Escolha uma das opções digitando um número de 1-5.")
            limpar_tela()
            continue

        while True:
            entrada = input("Digite um número ou escreva 'xis' para finalizar: ")

            if entrada == "xis":
                if len(numeros) < 2: ## len é uma função para contar valores.
                    print("Digite dois ou mais números antes de finalizar.")
                else:
                    print("----- > Calculando números... ")
                    break
            else:
                try: ## Try é um tratamento de exceçõees, sem ele, o cóigo iria quebrar se entrasse valores não numerais.
                    numeros.append(float(entrada))  ## Para adcionar valores em uma lista utiliz-se | nomelista.append(valor) |.
                except ValueError:
                    print("Digite apenas números.")


        match resposta:
            case 1:
                print("Resultado da soma: " + str(sum(numeros)))
                limpar_tela()
            
            case 2:
                print("Resultado da subtração: " + str(reduce(operator.sub, numeros))) ## O Python não possui uma função como sum() para as outras operações matemáticas, logo, importei essa função de outra biblioteca.
                limpar_tela()
            case 3:
                print("Resultado do produto: " + str(reduce(operator.mul, numeros)))
                limpar_tela()
            case 4:
                try:
                    print("Resultado da divisão: " + str(reduce(operator.truediv, numeros))) ## Trativa para o código não quebrar se o usuário tentar dividir por zero.
                    limpar_tela()
                except ZeroDivisionError:
                    print("Não é possível dividir por zero.")
                    limpar_tela()