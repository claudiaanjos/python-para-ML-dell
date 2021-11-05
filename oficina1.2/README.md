# Oficina 1.2 - Funções da biblioteca padrão

### 📚  Descrição

Geralmente, os logs são configurados para registrar as mensagens de maior gravidade. Em contrapartida, o modo debug é utilizado somente quando o programa apresenta falhas e é necessário fazer uma auditoria para encontrar o problema.

A seguir, considere o caso descrito para resolver a questão.

Imagine que você é o cientista de dados de uma grande empresa e, como um bom colaborador, decidiu analisar os dados de log de um programa essencial da empresa, com o intuito de avaliar como o programa se comportou durante um ano de funcionamento.

Ao receber o arquivo de log, você percebeu que há dados de pelo menos um ano inteiro e que o arquivo possui 4 Gigabytes de tamanho. Então, você decidiu utilizar expressão regular para avaliar aquele comportamento.

Para isso, você precisou construir um código que informasse a quantidade de erros ocorridos e quais os horários em que mais ocorrem erro. Estas informações serão uteis para lhe ajudar a investigar a causa do problema.

Sabendo que o log possui uma formatação clara (Dia-Mês-Ano Hora:Minuto:Segundo:Milesimos_de_segundos | Nivel_de_gravidade -> Mensagem), utilize a string a seguir como exemplo para fazer o seu código. Ao final, envie seu código em Python, ou seja, um arquivo com a extensão ‘py’, para avaliarmos como você resolveu esse problema.


- 2020-05-10 20:42:54,687 | INFO -> O programa foi iniciado
- 2020-05-11 00:09:52,532 | ERROR -> Erro não esperado
- 2020-05-11 09:01:10,812 | INFO -> O usuário utilizou o sistema
- 2020-05-11 19:06:13,609 | INFO -> O usuário utilizou o sistema
- 2020-05-11 20:46:35,271 | ERROR -> Erro não esperado
- 2020-05-12 08:14:59,895 | ERROR -> Erro não esperado
- 2020-05-12 11:33:59,700 | INFO -> O usuário utilizou o sistema
- 2020-05-13 10:20:14,673 | INFO -> O usuário utilizou o sistema
- 2020-05-13 16:58:10,298 | WARNING -> O usuário tentou fazer uma operação invalida
- 2020-05-14 03:55:25,383 | INFO -> O usuário utilizou o sistema
- 2020-05-15 02:59:29,002 | INFO -> O usuário utilizou o sistema
- 2020-05-15 08:40:33,776 | ERROR -> Erro não esperado
- 2020-05-15 13:45:29,089 | WARNING -> O usuário tentou fazer uma operação invalida