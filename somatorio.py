"""
Complete a seguinte função para que a mesma devolva todos os possíveis números de 4 dígitos, 
        onde cada um seja menor ou igual a<maxDigit>, e a soma dos dígitos de cada número gerado seja 21
        Exemplo maxDigit=6: 3666, 4566...
"""
maxDigit = 6
matchs = []
list = range(1000,6666)

for number in list:
    numberStr = str(number)
    sumNum = sum(int(value) for value in numberStr)
    if numberStr == 21:
        matchs.append(numberStr)
        
print(matchs)