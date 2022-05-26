"""
Complete a seguinte função para que a mesma devolva todos os possíveis números de 4 dígitos, 
        onde cada um seja menor ou igual a<maxDigit>, e a soma dos dígitos de cada número gerado seja 21
        Exemplo maxDigit=6: 3666, 4566...
"""

maxDigit = 6
matchs = []
list = range(1000,6666)

for number in list:
    sumNum = sum(int(value) for value in str(number))
    result = [int(valor) for valor in str(number)]
    checkMaxDigit = max(result)
   
    if sumNum == 21 and checkMaxDigit <= maxDigit:
        matchs.append(number)
        
print(matchs)