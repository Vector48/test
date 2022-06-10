number = input('Введите число: ')
print()

size = 2
width = size + 2
height = size * 2 + 3
v0 = ' ' + ' ' * size + ' '
v1 = ' ' + '-' * size + ' '
v2 = '|' + ' ' * size + ' '
v3 = ' ' + ' ' * size + '|'
v4 = '|' + ' ' * size + '|'

d0 = [v1, v4, v4, v0, v4, v4, v1]
d1 = [v0, v3, v3, v0, v3, v3, v0]
d2 = [v1, v3, v3, v1, v2, v2, v1]
d3 = [v1, v3, v3, v1, v3, v3, v1]
d4 = [v0, v4, v4, v1, v3, v3, v0]
d5 = [v1, v2, v2, v1, v3, v3, v1]
d6 = [v1, v2, v2, v1, v4, v4, v1]
d7 = [v1, v3, v3, v0, v3, v3, v0]
d8 = [v1, v4, v4, v1, v4, v4, v1]
d9 = [v1, v4, v4, v1, v3, v3, v1]
digits = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9]

print('x' + '-' * ((width + 1) * len(number) - 1) + 'x')
for i in range(height):
    print('|', end= '')
    print(*[(digits[int(j)][i]) for j in number], end= '')
    print('|')
print('x' + '-' * ((width + 1) * len(number) - 1) + 'x')
input()