vetorInicial = []

qtdPixels = int(input('Quantos pixels você ira inserir? '))
for i in range(qtdPixels):
    vetorInicial.append(int(input('Qual o valor do pixel? ')))
    
menorValor = min(vetorInicial)
maiorValor = max(vetorInicial)


lib = {
    "0" : vetorInicial.count(0),
    "1" : vetorInicial.count(1),
    "2" : vetorInicial.count(2),
    "3" : vetorInicial.count(3),
    "4" : vetorInicial.count(4),
    "5" : vetorInicial.count(5),
    "6" : vetorInicial.count(6),
    "7" : vetorInicial.count(7),
    "8" : vetorInicial.count(8),
    "9" : vetorInicial.count(9),  
}



for i in range(lib):
    print(i)