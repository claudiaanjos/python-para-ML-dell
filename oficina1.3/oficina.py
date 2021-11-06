from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, '')

aniversarios = [
	'01/02/1990', 
	'22 de Maio de 1991', 
	'04/Abr/1995', 
	'1995-Outubro-10', 
	'12 Julho 1989', 
	'16 de Junho de 1987', 
	'04/07/1990'
]

padrao_data = [
	"%d/%m/%Y",
	"%d de %B de %Y",
	"%d/%m/%Y",
	"%Y-%B-%d",
	"%d %B %Y",
	"%d de %B de %Y",
	"%d/%m/%Y"
]
		      
conversao = [datetime.strptime(date, pattern) for date, pattern in zip(aniversarios, padrao_data)]
print(conversao)

ordenacao = sorted(conversao, key=lambda data: (data.month, data.day))
print(ordenacao)

print(f"{'Hoje é seu aniversário' if datetime.today in conversao else 'Não tem aniversariantes hoje'}")