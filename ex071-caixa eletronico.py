print('----BEM VINDO AO CAIXA ELETRÔNICO-----')
saque = int(input('Que valor você quer sacar? R$ '))
total = saque
cedula = 50
totcedula = 0
while True:
    if total >= cedula:
        total = total - cedula
        totcedula = totcedula + 1
    else:
        print('Total de {} cédulas de {} reais'.format(totcedula,cedula))
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        if total == 0:
            break
print('=='*20)
print('Obrigado e volte sempre!')




