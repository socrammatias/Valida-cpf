def tratar_primeiro_digito(cpf):
    mult = 10
    x = 0
    soma = 0
    while x < 9:
        soma += int(cpf[x]) * mult
        x += 1
        mult -= 1
    valida = ((soma * 10) % 11)
    if valida == 10: # caso o calculo do primeiro digito seja 10, ele deve ser 0
        return 0
    else:
        return ((soma * 10) % 11)

def tratar_segundo_digito(cpf):
    mult = 11
    x = 0
    soma = 0
    while mult > 1:
        soma += int(cpf[x]) * mult
        x += 1
        mult -= 1
    valida = ((soma * 10) % 11)
    if valida == 10: # caso o calculo do segundo digito seja 10, ele deve ser 0
        return 0
    else:
        return valida

def valida(cpf):
    lista_invalidos = ['000000000000''11111111111', '22222222222', 
                        '33333333333', '44444444444', '55555555555',
                        '66666666666', '77777777777', '88888888888', 
                        '99999999999']
    if len(cpf) > 11:
        print('CPF inválido')
        return False
    elif cpf in lista_invalidos:
        print('CPF inválido')
        return False
    else:
        return True

def main():
    print('''
  ___ _ __  / _|   ___| |__   ___  ___| | _____ _ __ 
 / __| '_ \| |_   / __| '_ \ / _ \/ __| |/ / _ \ '__|
| (__| |_) |  _| | (__| | | |  __/ (__|   <  __/ |   
 \___| .__/|_|    \___|_| |_|\___|\___|_|\_\___|_|   
     |_|  ''')
    cpf = input('Insira o cpf: ').replace('-', '').replace('.', '')
    if valida(cpf):
        primeiro = tratar_primeiro_digito(cpf)
        segundo = tratar_segundo_digito(cpf)
        if primeiro == int(cpf[-2]) and segundo == int(cpf[-1]):
            print('CPF válido')
        else:
            print('CPF inválido')
main()
