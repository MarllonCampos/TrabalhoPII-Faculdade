vetorInicial = [0, 0, 4, 6, 8, 8, 4, 7, 8, 9, 9, 4, 3, 2, 3, 8, 2, 2, 1, 0]

qtdPixels = 20
# qtdPixels = int(input('Quantos pixels você ira inserir? '))
# for i in range(qtdPixels):
#     vetorInicial.append(int(input('Qual o valor do pixel? ')))

menorValor = min(vetorInicial)
maiorValor = max(vetorInicial)
diferençaMaiorMenor = maiorValor - menorValor

lib = {
    'intervalo': [],
    'qtdElemento': [],
    'somaComAnteriores': [],
    'Pk': [],
    'kLinha': [1, 2, 3, 4, 5, 5, 6, 6, 8, 9]
}

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

# for index,elem in enumerate(lib['Pk']):
#     lib['kLinha'].append(ceil(elem * len(lib['intervalo']) -1))


vetorFinal = vetorInicial.copy()
vetorDeControle = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for index, elem in enumerate(lib['intervalo']):
    for i,e in enumerate(vetorFinal):
        if e==elem and vetorDeControle[i]==0:
           vetorFinal[i]=lib['kLinha'][index]
           vetorDeControle[i]=1
                    
                    
print(vetorFinal)

