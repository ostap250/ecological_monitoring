import json
import os
import django
import sys
import pytz
from datetime import datetime

# Налаштування Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecological_monitoring.settings")
django.setup()

# Імпорт моделей після налаштування Django
from rivers.models import SensorData

def load_data_from_json(filename):
    print(f"Завантажую дані з {filename}...")
    with open(filename, "r") as file:
        data = json.load(file)
    return data

def save_data_to_db(data):
    print("Зберігаю дані у базу...")
    timezone = pytz.timezone("Europe/Kiev")  # Вкажіть ваш часовий пояс
    for entry in data:
        # Перетворення naive datetime на aware datetime
        naive_timestamp = datetime.fromisoformat(entry["timestamp"])
        aware_timestamp = timezone.localize(naive_timestamp)

        sensor_data = SensorData(
            oxygen=entry["oxygen"],
            biological_index=entry["biological_index"],
            pollutant_concentration=entry["pollutant_concentration"],
            temperature=entry["temperature"],
            turbidity=entry["turbidity"],
            timestamp=aware_timestamp
        )
        sensor_data.save()
    print("Усі дані успішно збережено!")

if __name__ == "__main__":
    data = load_data_from_json("sensor_data.json")
    save_data_to_db(data)





# копілот
# import json
# from rivers.models import SensorData  # Переконайтесь, що у вас є відповідна модель у models.py
# import sys
# import os

# # Додати кореневу директорію проекту до sys.path
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecological_monitoring.settings')

# import django
# django.setup()


# # Функція для завантаження даних з JSON-файлу
# def load_data_from_json(filename):
#     with open(filename, "r") as file:
#         data = json.load(file)
#     return data

# # Функція для збереження даних у базу
# def save_data_to_db(data):
#     for entry in data:
#         sensor_data = SensorData(
#             oxygen=entry["oxygen"],
#             biological_index=entry["biological_index"],
#             pollutant_concentration=entry["pollutant_concentration"],
#             temperature=entry["temperature"],
#             turbidity=entry["turbidity"],
#             timestamp=entry["timestamp"]
#         )
#         sensor_data.save()

# # Основна частина
# if __name__ == "__main__":
#     # Завантажуємо дані з JSON-файлу
#     data = load_data_from_json("sensor_data.json")
#     # Зберігаємо дані у базу
#     save_data_to_db(data)
#     print("Дані збережено у базу")
