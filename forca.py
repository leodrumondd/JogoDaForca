import random 
lista_nomes = ['leonardo', 'gabriel', 'victor',
      'jeferson', 'caroline','leci',
     'luca', 'vinicius', 'gabriela',
    'isabella', 'fernando', 'bruna',
    'laura', 'julio', 'nicoli', 'barbara',
      'patrick', 'jean', 'leci', 'leticia']
lista_profissão = ['administrador', 'piloto', 'mecanico', 'caminhoneiro',
 'lutador', 'programador', 'jornalista', 'professor',
 'vigilante', 'analista', 'diretor', 'gerente',
 'motorista']

nomes = random.choice(lista_nomes)
acertos = ''
flag = True
erros = 0
tentadas = ''
tentativas = 0
print('Começando o jogo, boa sorte.')
print('----- DICA : É UM NOME -----')

while flag:
    
    
    descobertas = ''
    tent = input('Digite uma letra: ')
    if len(tent) > 1:
        print('Digite apenas uma letra')
        continue
    tentativas += 1

    if tent in tentadas and tent not in nomes:
        print('Você já digitou essa letra.')
        erros -= 1
    
    elif tent in tentadas:
        print('Você já digitou essa letra.')

    if tent in nomes:
        acertos += tent
        tentadas += tent
    
    else:
        tentadas += tent
        erros += 1

     
    if erros == 1:
        print("|----- ")
        print("|     | ")
        print("|     O ")
    elif erros == 2:
        print("|----- ")
        print("|     | ")
        print("|     O ")
        print("|     | ")
    elif erros == 3:
        print("|----- ")
        print("|     | ")
        print("|     O ")
        print("|    /| ")
    elif erros == 4:
        print("|----- ")
        print("|     | ")
        print("|     O ")
        print("|    /|\ ")
    elif erros == 5:
        print("|----- ")
        print("|     | ")
        print("|     O ")
        print("|    /|\ ")
        print("|    /  ")
    elif erros == 6:
        print("|----- ")
        print("|     | ")
        print("|     O ")
        print("|    /|\ ")
        print("|    / \ ")
        print('Você foi enforcado!!!')
        print(f'O nome era : {nomes.upper()}')
        break
          
    for letra in nomes:
        if letra in acertos:
            descobertas += letra
        else:
            descobertas += '*'
            
           
    print(descobertas.upper())
        
    if descobertas == nomes:
        print('Sucesso, você ganhou.')
        break
    
    if tentativas >= 6:
        tent_certa = input('Se você já souber a palavra, digite aqui, senão, tecle (n) : ')
        if tent_certa == nomes:
            print(descobertas.upper())
        elif tent_certa == 'n':
            continue
        else:
            print("|----- ")
            print("|     | ")
            print("|     O ")
            print("|    /|\ ")
            print("|    / \ ")
            print('Você foi enforcado!!!')
            print(f'O nome era : {nomes.upper()}')
            break
        
   
 