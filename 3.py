import matplotlib.pyplot as plt
import numpy as np

# Создаём данные для графика в полярных координатах
theta = np.linspace(0, 2*np.pi, 1000)

# Для эллиптической кривой y² = x³ + 7 преобразуем в полярные координаты
# x = r*cos(θ), y = r*sin(θ)
# Тогда: (r*sin(θ))² = (r*cos(θ))³ + 7
# r²*sin²(θ) = r³*cos³(θ) + 7
# r³*cos³(θ) - r²*sin²(θ) + 7 = 0

# Решим это уравнение для r при каждом θ
r_values = []

for t in theta:
    # Коэффициенты кубического уравнения: a*r³ + b*r² + c = 0
    a = np.cos(t)**3
    b = -np.sin(t)**2
    c = 7
    
    # Найдем корни уравнения
    coefficients = [a, b, 0, c]
    roots = np.roots(coefficients)
    
    # Выберем действительные положительные корни
    real_roots = [r for r in roots if np.isreal(r) and r > 0]
    
    if real_roots:
        r_values.append(min(real_roots))  # берем наименьший положительный корень
    else:
        r_values.append(np.nan)

# Создаём полярный график
plt.figure(figsize=(10, 8))
ax = plt.subplot(111, projection='polar')

# Рисуем кривую
ax.plot(theta, r_values, 'b-', linewidth=2, label='y² = x³ + 7 в полярных координатах')

# Добавляем сетку и подписи
ax.grid(True)
ax.set_title('Эллиптическая кривая secp256k1\nв полярных координатах', fontsize=14, pad=20)
ax.legend(loc='upper right')

plt.show()
