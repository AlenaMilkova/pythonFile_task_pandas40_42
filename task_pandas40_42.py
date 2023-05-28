# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

import pandas as pd

fd = pd.read_csv('california_housing_train.csv')
# print(fd.head())

# Загрузка данных из файла
data = pd.read_csv('california_housing_train.csv')

# Отбор строк, где количество людей от 0 до 500
filtered_data = data[(data['population'] >= 0) & (data['population'] <= 500)]

# Вычисление средней стоимости дома
average_house_value = filtered_data['median_house_value'].mean()

# Вывод результата
print(f"Средняя стоимость дома для количества людей от 0 до 500: ${average_house_value}")


# Задача 42: Узнать какая максимальная households в зоне минимального значения population

min_population = data['population'].min()

# Отбор строк, где население равно минимальному значению
filtered_data = data[data['population'] == min_population]

# Нахождение максимального количества households
max_households = filtered_data['households'].max()

# Вывод результата
print(f"Максимальное количество households в зоне с минимальным населением ({min_population}): {max_households}")




