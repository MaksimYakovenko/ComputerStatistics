import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import norm
import numpy as np

# task 1
data = pd.read_csv('Height_Survey.csv', delimiter=';')
data.head(4)
# print(data)

# task 2
height_f = data[(data['Height_cm'] > 0) & (data['Sex'] == 'F')]
height_m = data[(data['Height_cm'] > 0) & (data['Sex'] == 'M')]
# print(height_m)
# print(height_f)

# task 3
mean_value_f = height_f['Height_cm'].mean()
mean_value_m = height_m['Height_cm'].mean()
print(f'Вибіркове середнє значення росту для жінок: {mean_value_f:.2f} см.')
print(f'Вибіркове середнє значення росту для чоловіків: {mean_value_m:.2f} см.')

median_f = height_f['Height_cm'].median()
median_m = height_m['Height_cm'].median()
print(f'Медіана росту жінок: {median_f} см.')
print(f'Медіана росту чоловіків: {median_m} см.')

variance_f = height_f['Height_cm'].var()
variance_m = height_m['Height_cm'].var()
print(f'Дисперсія для жіночої статі: {variance_f:.2f} см.')
print(f'Дисперсія для чоловічої статі: {variance_m:.2f} см.')

std_f = height_f['Height_cm'].std()
std_m = height_m['Height_cm'].std()
print(f'Середньоквадратичне відхилення для жіночої статі: {std_f:.2f}')
print(f'Середньоквадратичне відхилення для чоловічої статі: {std_m:.2f}')

quantile1_f = height_f['Height_cm'].quantile(.25)
quantile1_m = height_m['Height_cm'].quantile(.25)
print(f'Квантиль Q1 для жіночої статі: {quantile1_f} см.')
print(f'Квантиль Q1 для чоловічої статі: {quantile1_m} см.')

quantile3_f = height_f['Height_cm'].quantile(.75)
quantile3_m = height_m['Height_cm'].quantile(.75)
print(f'Квантиль Q3 для жіночої статі: {quantile3_f} см.')
print(f'Квантиль Q3 для чоловічої статі: {quantile3_m} см.')

interquartile_range_f = quantile3_f - quantile1_f
interquartile_range_m = quantile3_m - quantile1_m
print(f'Інтерквантильний розмах для жіночої статі: {interquartile_range_f} см.')
print(f'Інтерквантильний розмах для чоловічої статі: {interquartile_range_m} см.')

swing_f = height_f['Height_cm'].max() - height_f['Height_cm'].min()
swing_m = height_m['Height_cm'].max() - height_m['Height_cm'].min()
print(f'Розмах зросту для жіночої статі: {swing_f} см.')
print(f'Розмах зросту для чоловічої статі: {swing_m} см.')

# task 4
plt.figure(figsize=(10, 6))
plt.title('Гістограма зросту для жінок')
plt.xlabel('Зріст (см)')
plt.ylabel('Кількість')
plt.hist(height_f['Height_cm'], bins=20, color='red')
plt.show()

plt.figure(figsize=(10, 6))
plt.title('Гістограма зросту для чоловіків')
plt.xlabel('Зріст (см)')
plt.ylabel('Кількість')
plt.hist(height_m['Height_cm'], bins=20, color='blue')
plt.show()

# task 5
plt.figure(figsize=(10, 6))
plt.title('Boxplot зросту залежно від статі')
plt.ylabel('Зріст (см)')
plt.boxplot([height_f['Height_cm'], height_m['Height_cm']], labels=['Жінки','Чоловіки'])
plt.show()

# task 6
count_women = len(height_f)
total_count = len(data)
women_proportion = count_women / total_count
print(f'Вибіркова оцінка частки жінок в вибірці {women_proportion:.3f}')

# task 7
confidence_levels = [0.95, 0.99]
confidence_intervals = []
for confidence_level in confidence_levels:
    alpha = 1 - confidence_level
    z_critical = stats.norm.ppf(1 - alpha / 2)
    std_error = women_proportion * np.sqrt((1 - women_proportion) / total_count)
    margin_of_error = z_critical * std_error
    confidence_interval = (women_proportion - margin_of_error, women_proportion + margin_of_error)
    confidence_intervals.append(confidence_interval)

for i, confidence_level in enumerate(confidence_levels):
    print(f'Довірчий інтервал для частки жінок в популяції {confidence_level * 100}%: {confidence_intervals[i]}')

# task 8
height_mean_m = mean_value_m
print(f'Оцінка для середнього зросту чоловіків в генеральній сукупності'
      f' {height_mean_m:.2f}')

count_men = len(height_m)
confidence_level_95 = 0.95
t_critical = stats.t.ppf((1 + confidence_level) / 2, df=count_men - 1)
standard_error = std_m / np.sqrt(count_men)
margin_error = t_critical * standard_error
confidence_interval_lower = mean_value_m - margin_error
confidence_interval_upper = mean_value_m + margin_of_error
print(f'Довірчий інтервал {confidence_level_95 * 100}% для середнього зросту '
      f'чоловіків:'
      f'({confidence_interval_lower}, {confidence_interval_upper})')

# task 9
'''Для моделювання зросту (для кожної статі окремо) можна використати 
нормальний розподіл '''

mean_male = mean_value_m
std_dev_male = std_m
print("Оцінка параметрів нормального розподілу для зросту чоловіків:")
print("Середнє значення:", mean_male)
print("Стандартне відхилення:", std_dev_male)

mean_women = mean_value_f
std_dev_women = std_f
print("Оцінка параметрів нормального розподілу для зросту чоловіків:")
print("Середнє значення:", mean_women)
print("Стандартне відхилення:", std_dev_women)
