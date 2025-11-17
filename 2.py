import matplotlib.pyplot as plt

# Упрощенная визуализация для конечного поля (маленькие числа)
p_small = 67  # маленькое простое число для демонстрации

# Вычисляем все точки на эллиптической кривой по модулю p_small
points = []
for x in range(p_small):
    y_squared = (x**3 + 7) % p_small
    for y in range(p_small):
        if (y*y) % p_small == y_squared:
            points.append((x, y))

# Рисуем точки конечного поля
plt.figure(figsize=(10, 10))
x_vals = [p[0] for p in points]
y_vals = [p[1] for p in points]

plt.scatter(x_vals, y_vals, color='blue', s=50)
plt.grid(True, alpha=0.3)
plt.title(f'Эллиптическая кривая y² = x³ + 7 по модулю {p_small}\n(Упрощенная модель secp256k1)')
plt.xlabel('x')
plt.ylabel('y')

# Показываем график
plt.show()
