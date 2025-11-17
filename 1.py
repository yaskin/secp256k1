import matplotlib.pyplot as plt
import numpy as np

# Создаём данные для графика
x = np.linspace(-2, 5, 1000)
y_squared = x**3 + 7

# Берем только действительные значения (где y² >= 0)
real_indices = y_squared >= 0
x_real = x[real_indices]
y_squared_real = y_squared[real_indices]

y_positive = np.sqrt(y_squared_real)
y_negative = -np.sqrt(y_squared_real)

# Базовая точка G на кривой
G_x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
G_y = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

# Масштабируем для отображения (реальные числа слишком большие!)
scale_factor = 1e76
G_x_scaled = G_x / scale_factor
G_y_scaled = G_y / scale_factor

# Создаём график
plt.figure(figsize=(12, 8))

# Рисуем кривую
plt.plot(x_real, y_positive, 'b-', linewidth=2, label='y² = x³ + 7')
plt.plot(x_real, y_negative, 'b-', linewidth=2)

# Отмечаем базовую точку G
plt.plot(G_x_scaled, G_y_scaled, 'ro', markersize=8, label=f'Базовая точка G')

# Добавляем стрелку от начала координат к точке G
plt.arrow(0, 0, G_x_scaled*0.9, G_y_scaled*0.9, head_width=0.1, head_length=0.1, 
          fc='r', ec='r', linestyle='--', alpha=0.7)

# Настраиваем график
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Эллиптическая кривая secp256k1: y² = x³ + 7\n(Математическая основа Биткойна)', fontsize=14)
plt.legend()
plt.axis('equal')

# Показываем график
plt.show()
