def gerar_tabuada(num):
    print(f'tabuada do {num}')
    for i in range(1, 11):
        resultado = num * i
        print(f'{num} x {i} = {resultado}')
        
num = int(input('Digite um numero para gerarmos a tabuada: '))

gerar_tabuada(num)