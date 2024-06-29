
saldo_conta = float(input('\n Digite o valor hoje em conta: '))
#valor_a_deduzir = float(input('Digite o valor para decair nas parcelas: '))

despesas = [
    {'Nome': 'Notebook', 
    'Parcelas_faltantes': 8, 
    'Valor': 273.98
    },    
    {'Nome': 'Suporte Notebook', 
    'Parcelas_faltantes': 4, 
    'Valor': 273.98
    },
    {'Nome': 'Placa de vídeo', 
    'Parcelas_faltantes': 2, 
    'Valor': 273.98
    }
]

valor_a_deduzir = float(input("Digite o valor a ser deduzido das parcelas: "))

for despesa in despesas:
    nome = despesa['Nome']
    parcelas_faltantes = despesa['Parcelas_faltantes']
    
    if 'Valor' in despesa:        
        despesa['Parcelas_faltantes'] -= valor_a_deduzir
        
        if despesa['Parcelas_faltantes'] <= 0:            
            print(f'Despesa: {nome}, Parcelas faltantes: {despesa["Parcelas_faltantes"]}, Valor por parcela: {despesa["Valor"]:.2f}')
    else:
        print(f'Despesa: {nome}, Parcelas faltantes: {parcelas_faltantes}')

for despesa in despesas:
    if 'Valor' in despesa:
        print(f'\n{despesa["Nome"]}, faltantes: {despesa["Parcelas_faltantes"]}')
    else:
        print(f'Despesa: {despesa["Nome"]}, Parcelas faltantes: {despesa["Parcelas_faltantes"]} \n')
