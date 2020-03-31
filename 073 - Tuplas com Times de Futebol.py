#   Exercício Python 073 - Tuplas com Times de Futebol
#   Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
#   na ordem de colocação. Depois mostre:
#       a) Os 5 primeiros times.
#       b) Os últimos 4 colocados.
#       c) Times em ordem alfabética.
#       d) Em que posição está o time da Chapecoense.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapeco', 'Atletico-MG',
         'Botafogo', 'Atletico-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport', 'Vitoria', 'Coritiba', 'Avaí',
         'Ponte Preta', 'Atletico-GO')
print('-=' * 28)
print(f'Os cincos primeiros colocados do Brasileirão 2017 são: {times[:5]}')
print('-=' * 28)
print(f'Os quatros ultimos colocados do Brasileirão 2017 são: {times[-4:]}')
print('-=' * 28)
print(f'Os times em ordem alfabetica do Brasileirão de 2017 são: {sorted(times)}')
print('-=' * 28)
print(f'O chapecoense está na {times.index("Chapeco") + 1} posição')
