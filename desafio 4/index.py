def adicao(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def divisao(x,y):
    return x/y

def calculadora():
    print('Selecione a operacao:')
    
    print('1.Adicao')
    print('2.Subtracao')
    print('3.Multiplicacao')
    print('4.Divisao')
    
    while True:
        escolha = input('Escolha(1/2/3/4):')
        if escolha in ('1','2','3','4'):
            
            x = int(input('Digite o primeiro numero:'))
            y = int(input('Digite o segundo numero:'))
            
            if escolha == '1':
                print('Resultado: ', adicao(x,y))
            
            if escolha == '2':
                print('Resultado: ', sub(x,y))
                
            if escolha == '3':
                print('Resultado: ', mult(x,y))
                
            if escolha == '4':
                if y != 0:
                print('Resultado: ', divisao(x,y))
            else:
                print('Nao é permitido a divisao por zero!')
        
        else: 
            print('Escolha invalida, escolha uma das opcoes listadas')       
        
        continuar = input('Deseja fazer outra operacao? (s/n)')
        if continuar == 'n':
            print('Encerrando calculadora')
            break;
        
    calculadora()