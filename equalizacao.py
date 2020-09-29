vetorComNumeros = []

qtdPixels = int(input('Quantos pixels você ira inserir? '))
for i in range(qtdPixels):
    vetorComNumeros.append(int(input('Qual o valor do pixel? ')))
    
menorValor = min(vetorComNumeros)
maiorValor = max(vetorComNumeros)

