notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
notas_pop = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]

def categoria(nota):
	if nota <= 1:
		return 'ruim'
	elif 2 <= nota <= 3:
		return 'mediana'
	else:
		return 'boa'

classificacao_rock = list(map(categoria, notas_rock))
classificacao_pop = list(map(categoria, notas_pop))


rock_ruim = list(filter(lambda x: x == 'ruim', classificacao_rock))
rock_mediana = list(filter(lambda x: x == 'mediana', classificacao_rock))
rock_boa = list(filter(lambda x: x == 'boa', classificacao_rock))
print('Quantidade de música de Rock ruim, mediana e boa...')
print('Rock ruim:', len(rock_ruim))
print('Rock mediana:', len(rock_mediana)) 
print('Rock boa:', len(rock_boa))  

print('\n')
pop_ruim = list(filter(lambda x: x == 'ruim', classificacao_pop))
pop_mediana = list(filter(lambda x: x == 'mediana', classificacao_pop))
pop_boa = list(filter(lambda x: x == 'boa', classificacao_pop))
print('Quantidade de música de Pop ruim, mediana e boa...')
print('Pop ruim:', len(pop_ruim))
print('Pop mediana:', len(pop_mediana)) 
print('Pop boa:', len(pop_boa))

rock_mediana_booleano = list(map(lambda x: x == 'mediana', classificacao_rock))
print(any(rock_mediana_booleano)) 

pop_boa_booleano = list(map(lambda x: x == 'boa', classificacao_pop))
print(all(pop_boa_booleano))

len_rock_boa = len(rock_boa)
len_pop_boa = len(pop_boa)

if len_rock_boa > len_pop_boa:
	print ('Rock tem mais músicas boas do que o Pop')
else:
	print ('Pop tem mais músicas boas do que o Rock')