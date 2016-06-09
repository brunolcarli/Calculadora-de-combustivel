#coding-utf8;-*

"""
Autor: Bruno Luvizotto Carli
e-mail: brunolcarli@gmail.com
"""


def kml(): #Define func que calcula os Km/l
    a = True
    while a == True:
        print('###############################')
        print('#    Insira a quantidade      #')
        print('#       de Km rodados         #')
        print('###############################')

        try: # trata a exceção caso o usuario entre com input invalido
            rodado = int(input('>> '))
            a = False #desliga o loop
        except:
            print('###############################')
            print('#   Você inseriu um digito    #')
            print('#         incorreto           #')
            print('###############################')
    a = True #religa o loop
    while a == True:

        print('###############################')
        print('#    Insira a quantidade      #')
        print('#  de combustível em litros   #')
        print('###############################')
        try:
            lt = float(input('>> '))
            a = False
        except:
            print('###############################')
            print('#   Você inseriu um digito    #')
            print('#         incorreto           #')
            print('###############################')

    kl = rodado / lt

    print('###############################')
    print('#                             #')
    print('#     Seu automovel está      #')
    print('#    realizando %.2f Km/l     #' % kl)
    print('#                             #')
    print('###############################')
    return(kl)

def qtlt(): #Define func que mede quantos litros serao abastecidos
    b = True
    while b == True:
        print('###############################')
        print('#      Insira o valor         #')
        print('#      do combustível         #')
        print('###############################')
        try:
            valor =float(input('>> '))
            b = False
        except:
            print('###############################')
            print('#   Você inseriu um digito    #')
            print('#         incorreto           #')
            print('# Dica: Nao utilize ,(virgula)#')
            print('#       utilize . (ponto)     #')
            print('###############################')
    b = True
    while b == True:
       print('###############################')
       print('#       Insira o valor        #')
       print('#     a ser  abastecido       #')
       print('###############################')
       try:
           comb =float(input('>> '))
           b = False
       except:
           print('###############################')
           print('#   Você inseriu um digito    #')
           print('#         incorreto           #')
           print('# Dica: Nao utilize ,(virgula)#')
           print('#       utilize . (ponto)     #')
           print('###############################')

    litros = comb / valor
    print('###############################')
    print('#                             #')
    print('# Sera depositado %.2f litros #' % litros)
    print('#   de combustível no seu     #')
    print('#        automóvel!           #')
    print('#                             #')
    print('###############################')

def bye(): #escreve Encerrando na tela
    print('###############################')
    print('#                             #')
    print('#        Encerrando!          #')
    print('#                             #')
    print('###############################')
# INICIO
y = True
while y == True: # loop principal do programa

    print('###############################')
    print('#    Programa que calcula     #')
    print('#   quantidae de combustível  #')
    print('###############################')
    print('#       insira o digito       #')
    print('#  correspondente a operação  #')
    print('#                             #')
    print('# [1] Calcular litros         #')
    print('# [2] calcular Km/l           #')
    print('# [3] Sair                    #')
    print('#                             #')
    print('###############################')

    x = input('>> ')
    while x != 1 or x != 2 or x != 3: # loop secundario. verifica a operação desejada
        if x == '1':
            qtlt()
            break
        elif x == '2':
            kml()
            break
        elif x == '3':
            bye()
            exit()
        else:
            print('###############################')
            print('#       Você inseriu um       #')
            print('#       digito inválido       #')
            print('###############################')
            break
        #fim do loop secundario
    print('###############################')
    print('#        Deseja realizar      #')
    print('#        outra operação?      #')
    print('#                             #')
    print('#           [1] Sim           #')
    print('#           [2] Não           #')
    print('#                             #')
    print('###############################')
    z = input('>> ')
    #verificação do loop primário
    if z == '2':
        y = False
    elif z == '1':
        y == True
    else:
        print('###############################')
        print('#     Você inseriu um         #')
        print('#     digito inválido         #')
        print('###############################')
# fim do loop primario

bye()

#fim do programa