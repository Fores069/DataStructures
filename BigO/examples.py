# Константные операции, сложность выполнения O(1)
var_a = 10
inf = float('inf')
print(inf)

# Алгоритмы с линейной сложностью, сложность O(n)
lst = [1, 4, 10, -5, 0, 2, 3, 18, 32]
for item in lst:
    print(item)

for item in lst:
    item += 1
    print(item)

# Алгоритм со сложностью O(n)
for item, index in enumerate(lst):
    lst[index] += 1

for item in lst:
    print(item)

# Алгоритм со сложностью O(n + m)
n = 12
for x in range(n):
    print(x)

m = 15
for y in range(m):
    print(y)

for x in range(n):
    for y in range(m):
        print(x, y)

