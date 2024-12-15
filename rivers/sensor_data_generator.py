import random
import json
from datetime import datetime

def generate_sensor_data():
    """Генерує випадкові показники сенсора у заданому діапазоні."""
    data = {
        "oxygen": round(random.uniform(4.0, 8.0), 2),  # кисень (mg/L)
        "biological_index": round(random.uniform(1.0, 3.0), 2),  # біологічний індекс
        "pollutant_concentration": round(random.uniform(10.0, 30.0), 2),  # концентрація забруднень
        "temperature": round(random.uniform(5.0, 25.0), 2),  # температура води (°C)
        "turbidity": round(random.uniform(0.5, 5.0), 2),  # каламутність (NTU)
        "timestamp": datetime.now().isoformat()  # поточний час
    }
    return data

def save_to_json_file(data, filename="sensor_data.json"):
    """Зберігає дані сенсора у JSON-файл."""
    try:
        with open(filename, "r") as file:
            all_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        all_data = []

    all_data.append(data)

    with open(filename, "w") as file:
        json.dump(all_data, file, indent=4)

if __name__ == "__main__":
    # Тест генерації даних
    for _ in range(10):  # Генеруємо 10 записів для прикладу
        data = generate_sensor_data()
        save_to_json_file(data)
        print(data)
