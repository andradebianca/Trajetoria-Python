import os

def limpar_tela(): ## snake_case
    input ("\nPressione qualquer tecla para voltar...")
    os.system('clear')


while True:
    print("===== CONVERSOR DE TEMPERATURA =====")

    try: 
        tempEntrada = float(input("Temperatura a ser convertida: "))
    except ValueError:
        print("Digite apenas números.")
        limpar_tela()
        continue

    grandeza = input("Grandeza da temperatura a ser convertida (c/f/k): ").lower() ## a função .lower() converte tudo em letra minúscula.
        
    if grandeza == "c":
        Cxkelvin = tempEntrada + 273.15
        Cxfahrenheit = (tempEntrada * 1.8) + 32
        print("----- Conversão de Celsius -----")
        print(f"|Celsius:", round(tempEntrada,2))
        print(f"|Fahrenheit:", round(Cxfahrenheit, 2) )
        print(f"|Kelvin:", round(Cxkelvin,2) )
        limpar_tela()

    elif grandeza == "f":
        FxCelsius = (tempEntrada - 32) / 1.8
        FxKelvin = FxCelsius + 273.15
        print("----- Conversão de Fahrenheit -----")
        print(f"|Fahrenheit:", round(tempEntrada,2))
        print(f"|Celsius:", round(FxCelsius, 2) )
        print(f"|Kelvin:", round(FxKelvin,2) )
        limpar_tela()

    elif grandeza == "k":
        KxCelsius= tempEntrada - 273.15
        Kxfahrenheit = KxCelsius * 1.8 + 32     
        print("----- Conversão de Kelvin ------")
        print(f"|Kelvin:", round(tempEntrada,2))
        print(f"|Celsius:", round(KxCelsius, 2) )
        print(f"|Fahrenheit:", round(Kxfahrenheit,2) )
        limpar_tela()
    
    else:
        print("====================")
        print("ESCALA INVÁLIDA!\nEscreva uma escala de temperatura entre: ")
        print("Celsius (Cº) | Fahrenheit (Fº) | Kelvin (K)")
        print("====================")
        limpar_tela()