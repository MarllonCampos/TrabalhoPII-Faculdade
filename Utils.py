from time import sleep
def imprimeInterface():
    print('-'*70)
    print('{:^80}'.format('\033[1;32mPrograma de Equalização de Vetores\033[m'))
    print('{:^78}'.format('Pressione \033[31mE\033[m para sair do programa'))
    print('-'*70)
    
def verificaSaida(valorInserido):
    print(valorInserido)
    if valorInserido.upper() == 'E':
        print(f'\033[33mSaindo... Reinicie o Programa\033[m')
        sleep(2)
        return True
    else:
        return False
    
def carregaBiblioteca(vetorInicial,qtdPixels):
    L = 1
    lib = {
    'intervalo': [],
    'qtdElemento': [],
    'somaComAnteriores': [],
    'Pk': [],
    'kLinha': []
    }
    menorValor = min(vetorInicial)
    maiorValor = max(vetorInicial)

    for i in range(menorValor, maiorValor):
        L += 1



    for i in range(menorValor, maiorValor + 1):
        lib['intervalo'].append(i)

    for i in lib['intervalo']:
        lib['qtdElemento'].append(vetorInicial.count(i))


    for index, elem in enumerate(lib['qtdElemento']):
        if index == 0:
            lib['somaComAnteriores'].append(elem)
        else:
            lib['somaComAnteriores'].append(lib['somaComAnteriores'][index - 1] +
                                            elem)

    for index, elem in enumerate(lib['somaComAnteriores']):
        lib['Pk'].append(elem / qtdPixels)


    for index, elem in enumerate(lib['Pk']):
        lib['kLinha'].append(round(elem * (len(lib['intervalo']) - 1)))
    
    return lib

    

def geraNovoVetor(k,kLinha,vetorInicial,vetorDeControle):
    vetorFinal = vetorInicial.copy()    
    for index, elem in enumerate(k):
        for i, e in enumerate(vetorFinal):
            if e == elem and vetorDeControle[i] == 0:
                vetorFinal[i] = kLinha[index]
                vetorDeControle[i]=1

    return vetorFinal

# def verificaNumericoInteiro(qtdPixels):
#     try:
#         qtdPixels=int(qtdPixels)
#         return qtdPixels
#     except:
#         pass   
def verificaNumericoInteiro (num):
    try:
        num = int(num)
    except ValueError:
        return False
    return num
    
    
a = verificaNumericoInteiro(str('5'))
print(a)