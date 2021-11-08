import random
from time import sleep

print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!\n')
print('\n')

#Primeira parte
def jogada (escolha):
    jogadas = ['Pedra', 'Papel', 'Tesoura']
    return jogadas[escolha-1]

while True:

    print('''\nSuas opções
	[ 1 ] Pedra
	[ 2 ] Papel
	[ 3 ] Tesoura
	[ 4 ] Sair
	''')

    usuario = int(input('\nSua escolha: '))

    while (usuario < 1) or (usuario > 4):
        print('Digite um número válido!')
        usuario = int(input('\nSua escolha: '))
    
    if (usuario == 4):
        break

    pc = random.randint(1, 3)
    
    print('Você jogou {}'.format(jogada(usuario)))
    print('O PC jogou {}'.format(jogada(pc)))

    if (usuario == pc):
        print('Vocês empataram!')
    elif (usuario == 1) and (pc == 3):
        print('Você ganhou! Parabéns!')
    elif (usuario == 2) and (pc == 1):
        print('Você ganhou! Parabéns!')
    elif (usuario == 3) and (pc == 2):
        print('Você ganhou! Parabéns!')
    else:
        print('Você perdeu! Que pena!')

#segunda parte
lista_escolhas_do_usuario = []

while True:

    print('''\nSuas opções
	[ 1 ] Pedra
	[ 2 ] Papel
	[ 3 ] Tesoura
	[ 4 ] Sair
	''')

    usuario = int(input('\nSua escolha: '))

    while (usuario < 1) or (usuario > 4):
        print('Digite um número válido!')
        usuario = int(input('\nSua escolha: '))
    
    if (usuario == 4):
        break

    lista_escolhas_do_usuario.append(usuario)
        
    if len(lista_escolhas_do_usuario) <= 5:
        pc = random.randint(1, 3)
    else:
        quantidade = [lista_escolhas_do_usuario.count(1), lista_escolhas_do_usuario.count(2), lista_escolhas_do_usuario.count(3)]
    	escolha_frequente = quantidade.index(max(quantidade)) + 1
    	if (escolha_frequente == 1):
        	pc = 2
    	elif (escolha_frequente == 2):
        	pc = 3
    	elif (escolha_frequente == 3):
        	pc = 1
    
    print('Você jogou {}'.format(jogada(usuario)))
    print('O PC jogou {}'.format(jogada(pc)))

    if (usuario == pc):
        print('Vocês empataram!')
    elif (usuario == 1) and (pc == 3):
        print('Você ganhou! Parabéns!')
    elif (usuario == 2) and (pc == 1):
        print('Você ganhou! Parabéns!')
    elif (usuario == 3) and (pc == 2):
        print('Você ganhou! Parabéns!')
    else:
        print('Você perdeu! Que pena!')
