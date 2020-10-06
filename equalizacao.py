import Utils

# vetorInicial = [0, 0, 4, 6, 8, 8, 4, 7, 8, 9, 9, 4, 3, 2, 3, 8, 2, 2, 1, 0]
vetorInicial = []
vetorDeControle = []
mensagemDeInserção = ''
variavelControle = 0


Utils.imprimeInterface() # Informa para o usuário qual tecla sai do programa

while 1 != 0:
    try:
        qtdPixels = 0
        qtdPixels = input('Quantos pixels você ira inserir? ')
        resul=Utils.verificaNumericoInteiro(qtdPixels)
        if resul==False:
            saida=Utils.verificaSaida(qtdPixels)
            if saida == True:
                exit()
        else:
            qtdPixels = resul
            break
    except Exception as errorMesssage:
        print(f'\033[31mERRO!: {errorMesssage}\033[m')
        print(f'\033[1;34mAceitamos apenas numeros, por favor respeite\033[m')
        print(f'\033[4;32mSaindo... Reinicie o Programa\033[m')
        

while 1 != 0:
    if len(vetorInicial) == qtdPixels:
        break
    else:
        try:
            valoresInseridos = 0    
            valoresInseridos = input('Qual o valor do pixel? ')
            saida  = Utils.verificaSaida(valoresInseridos)  
            if saida:
                exit()
            if int(valoresInseridos) < 0 or int(valoresInseridos) > 255:
                raise Exception("Insira um valor entre \033[34m0\033[m e \033[34m255\033[m")
            vetorInicial.append(int(valoresInseridos))
            vetorDeControle.append(0)
            mensagemDeInserção += (f"{valoresInseridos} - ")
            print(f'\033[32mNúmeros ja inserídos: {mensagemDeInserção}\033[m')
            
        except Exception as errorMesssage:
            print(f'\033[31mERRO!: {errorMesssage}\033[m')
            print(
                f'\033[1;34mAceitamos apenas numeros, por favor respeite\033[m')
            print(f'\033[32mNúmeros ja inserídos: {mensagemDeInserção}\033[m')
    variavelControle += 1

ConjuntoDeValores = Utils.carregaBiblioteca(vetorInicial,qtdPixels)

vetorEqualizado = Utils.geraNovoVetor(ConjuntoDeValores['intervalo'],ConjuntoDeValores['kLinha'],vetorInicial,vetorDeControle)

print(f'O vetor de entrada é: \033[33m{vetorInicial}\033[m')
print(f'O resultado do vetor equalizado é: \033[31m{vetorEqualizado}\033[m')


y = y.replace('-')