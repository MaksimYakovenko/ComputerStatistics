import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


mean = 0 # середнє значення
std_dev = 1 # стандартне відхилення

# -----------------------------------------------------------------------------

"""Генерування вибірки з 1000 елементів."""
sample_size = 1000
data_sample = np.random.normal(mean, std_dev, sample_size)

# print(data_sample[:20]) # перевірка на вивід перших 20 елементів вибірки

# -----------------------------------------------------------------------------

sample_mean = np.mean(data_sample) # оцінка середнього значення
sample_dispersion = np.var(data_sample) # оцінка дисперсії
sample_std_dev = np.std(data_sample) # оцінка стандартного відхилення

# -----------------------------------------------------------------------------

# print(sample_mean)
# print(sample_dispersion)

# -----------------------------------------------------------------------------

# Створення теоретичної функції
x_theoretical = np.linspace(-4, 4, 1000) # Діапазон значень для теоретичної ф-ї
t = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-((x_theoretical - mean) ** 2) / (2 * std_dev ** 2))

# -----------------------------------------------------------------------------

# Створення емпіричної функції
sorted_data = np.sort(data_sample)
e = np.arange(1, len(sorted_data) + 1) / len(sorted_data)

# -----------------------------------------------------------------------------

# Створення нормальної функції розподілу
cdf_estimated = norm.cdf(x_theoretical, loc=sample_mean, scale=sample_std_dev)

# -----------------------------------------------------------------------------

# Створення графіків

plt.figure(figsize=(10, 5))
plt.plot(x_theoretical, t, label="Теоретична функція розподілу")
plt.step(sorted_data, e, label="Емпірична функція розподілу")
plt.plot(x_theoretical, cdf_estimated, label='Нормальна функція розподілу', linestyle='--')
plt.xlabel("Значення")
plt.ylabel("Ймовірність")
plt.legend()
plt.title("Теоретична, емпірична та нормальна функція розподілу")
plt.grid(True)
plt.show()

# -----------------------------------------------------------------------------

# Обчислення стандартного відхилення

squared_diff_sum = np.sum((data_sample - mean) ** 2)
std = np.sqrt(squared_diff_sum / sample_size)
print("Оцінка середнього відхилення", std)
