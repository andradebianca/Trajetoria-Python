import os

def limpar_tela(): ## snake_case
    input ("\nPressione qualquer tecla para voltar...")
    os.system('clear')
    
def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Apenas números inteiros.")
            continue

def calculo_tabuada (numero, quantidade):
    multiplicador = 1

    for i in range(quantidade):
        resultados = numero * multiplicador
        print(multiplicador, "x", numero, "=", resultados)
        multiplicador += 1


while True:
    print("===== TABUADA DOS INTEIROS =====")
    numero = ler_inteiro("Digite um número: ")
    quantidade = ler_inteiro("Quantas vezes?: ")
        
    while True:
        
        calculo_tabuada(numero, quantidade)

        resposta = input("(1) Gera mais 5 valores.\n(2) Trocar o número de cálculo\n(3) Sair do programa\n-> ")

        if resposta == "1":
            quantidade += 5

        elif resposta == "2":
            os.system('clear')
            break
        elif resposta == "3":
            break
        else:
            print("Escolha uma das opções indicadas.")
            limpar_tela()
    
    if resposta == "3":
        break

    
