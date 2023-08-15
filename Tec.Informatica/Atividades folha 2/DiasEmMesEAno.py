ano = int(input("Digite o ano: "))
mes = int(input("Digite o número do mês [entre 1 e 12]: "))

if mes < 1 or mes > 12:
    print("Escreve direito carai, o mês deve estar entre 1 e 12.")
else:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        leap_year = True
    else:
        leap_year = False
    
    if mes == 2:
        if leap_year:
            num_days = 29
        else:
            num_days = 28
    elif mes in [4, 6, 9, 11]:
        num_days = 30
    else:
        num_days = 31
    
    print(f"O mês {mes} do ano {ano} possui {num_days} dias.")