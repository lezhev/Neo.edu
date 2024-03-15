import requests
import importlib.util

# Скачиваем код функции с GitHub
url = 'main.py'
response = requests.get(url)
function_code = response.text

# Записываем код функции в файл function.py
with open('function.py', 'w') as file:
    file.write(function_code)

# Импортируем функцию из загруженного файла
spec = importlib.util.spec_from_file_location("function", "function.py")
function_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(function_module)

# Ваши входные данные
data = [1, 2, 3, 4, 5]

# Вызываем функцию с вашими входными данными
result = function_module.calculate_sum(data)
print("Результат выполнения функции:", result)
