times = ('Botafogo','Flamengo','Fluminense','Palmeiras','Bragantino','Grêmio','Athletico-PR','Cuiabá','São Paulo','Atlético-MG','Cruzeiro','Internacional','Fortaleza','Cortinas','Goiás','Bahia','Santos','Coritiba','Vascao','América-MG')
print('=-'*40)
print(f'Os 5 primeiro colocados são {times[0:5]}')
print('=-'*40)
print(f'Os 4 ultimos colocados são {times[-4:]}')
print('=-'*40)
print(sorted(times[1:]))
print('=-'*40)
cortinas_position = (times.index('Cortinas'))+ 1
print(f'Cortinas está na {cortinas_position}ª posição')