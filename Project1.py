# Все данные взяты за 2018 год

k = 146300000
n0 = int(input())
migr = 3078114/365      # Сколько мигрантов приезжают в день
migr1 = 2976847/365     # Сколько эммигрантов в день
child = 1604344/365     # Сколько детей рождаются в день
death = 1828910/365     # Сколько человек умирает в день

n = (n0-2015)*365       # количество дней
N = k+(migr+child)*n-(migr1+death)*n
if n0 > 2015:
    print('В {0} году предположительно численность населения будет равна {1} человек.'.format(n0,N))
else:
    print('Программа прогнозирует, введите год после 2015')
