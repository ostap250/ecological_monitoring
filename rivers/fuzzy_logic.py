import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Визначення входів (input variables)
oxygen = ctrl.Antecedent(np.arange(0, 15, 0.1), 'oxygen')
biological_index = ctrl.Antecedent(np.arange(0, 10, 0.1), 'biological_index')
pollutant_concentration = ctrl.Antecedent(np.arange(0, 100, 1), 'pollutant_concentration')

# Визначення виходу (output variable)
environmental_rating = ctrl.Consequent(np.arange(0, 101, 1), 'environmental_rating')

# Фаззифікація входів
oxygen['low'] = fuzz.trapmf(oxygen.universe, [0, 0, 4, 6])
oxygen['medium'] = fuzz.trimf(oxygen.universe, [4, 7, 10])
oxygen['high'] = fuzz.trapmf(oxygen.universe, [8, 12, 15, 15])

biological_index['poor'] = fuzz.trapmf(biological_index.universe, [0, 0, 3, 5])
biological_index['average'] = fuzz.trimf(biological_index.universe, [3, 5, 7])
biological_index['good'] = fuzz.trapmf(biological_index.universe, [6, 8, 10, 10])

pollutant_concentration['low'] = fuzz.trapmf(pollutant_concentration.universe, [0, 0, 20, 40])
pollutant_concentration['medium'] = fuzz.trimf(pollutant_concentration.universe, [20, 50, 80])
pollutant_concentration['high'] = fuzz.trapmf(pollutant_concentration.universe, [60, 80, 100, 100])

# Фаззифікація виходу
environmental_rating['poor'] = fuzz.trapmf(environmental_rating.universe, [0, 0, 30, 50])
environmental_rating['average'] = fuzz.trimf(environmental_rating.universe, [30, 50, 70])
environmental_rating['good'] = fuzz.trapmf(environmental_rating.universe, [60, 80, 100, 100])

# Правила нечіткої логіки
rule1 = ctrl.Rule(oxygen['low'] & biological_index['poor'] & pollutant_concentration['high'], environmental_rating['poor'])
rule2 = ctrl.Rule(oxygen['low'] & biological_index['poor'] & pollutant_concentration['medium'], environmental_rating['poor'])
rule3 = ctrl.Rule(oxygen['medium'] & biological_index['average'] & pollutant_concentration['medium'], environmental_rating['average'])
rule4 = ctrl.Rule(oxygen['high'] & biological_index['good'] & pollutant_concentration['low'], environmental_rating['good'])
rule5 = ctrl.Rule(oxygen['medium'] & biological_index['good'] & pollutant_concentration['low'], environmental_rating['good'])
rule6 = ctrl.Rule(oxygen['low'] & biological_index['average'] & pollutant_concentration['high'], environmental_rating['poor'])
rule7 = ctrl.Rule(oxygen['high'] & biological_index['poor'] & pollutant_concentration['medium'], environmental_rating['average'])
rule8 = ctrl.Rule(oxygen['medium'] & biological_index['average'] & pollutant_concentration['low'], environmental_rating['good'])
rule9 = ctrl.Rule(oxygen['low'] & biological_index['good'] & pollutant_concentration['medium'], environmental_rating['average'])
rule10 = ctrl.Rule(oxygen['high'] & biological_index['good'] & pollutant_concentration['high'], environmental_rating['average'])

# Додаткові правила
rule11 = ctrl.Rule(oxygen['medium'] & biological_index['poor'] & pollutant_concentration['high'], environmental_rating['poor'])
rule12 = ctrl.Rule(oxygen['medium'] & biological_index['good'] & pollutant_concentration['medium'], environmental_rating['good'])
rule13 = ctrl.Rule(oxygen['high'] & biological_index['average'] & pollutant_concentration['low'], environmental_rating['good'])
rule14 = ctrl.Rule(oxygen['low'] & biological_index['average'] & pollutant_concentration['medium'], environmental_rating['average'])
rule15 = ctrl.Rule(oxygen['medium'] & biological_index['average'] & pollutant_concentration['high'], environmental_rating['average'])
rule16 = ctrl.Rule(oxygen['high'] & biological_index['poor'] & pollutant_concentration['low'], environmental_rating['average'])
rule17 = ctrl.Rule(oxygen['low'] & biological_index['good'] & pollutant_concentration['high'], environmental_rating['average'])
rule18 = ctrl.Rule(oxygen['high'] & biological_index['average'] & pollutant_concentration['medium'], environmental_rating['good'])
rule19 = ctrl.Rule(oxygen['medium'] & biological_index['poor'] & pollutant_concentration['low'], environmental_rating['average'])
rule20 = ctrl.Rule(oxygen['low'] & biological_index['poor'] & pollutant_concentration['low'], environmental_rating['poor'])

# Контролер
rating_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
    rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20
])

rating_simulation = ctrl.ControlSystemSimulation(rating_ctrl)

# Функція для отримання рекомендацій
def calculate_rating_and_recommendation(oxygen, biological_index, pollutant_concentration):
    # Передаємо значення до системи
    rating_simulation.input['oxygen'] = oxygen
    rating_simulation.input['biological_index'] = biological_index
    rating_simulation.input['pollutant_concentration'] = pollutant_concentration

    # Обчислюємо рейтинг
    rating_simulation.compute()
    rating = rating_simulation.output['environmental_rating']

    # Генеруємо рекомендацію
    if rating < 30:
        recommendation = "Необхідно терміново провести очищення водойми."
    elif 30 <= rating < 60:
        recommendation = "Потрібно моніторити стан та поступово вживати заходів."
    else:
        recommendation = "Стан водойми задовільний. Рекомендується підтримувати контроль."
        return rating, recommendation


# Тестування
rating_simulation.input['oxygen'] = 5
rating_simulation.input['biological_index'] = 4
rating_simulation.input['pollutant_concentration'] = 70

rating_simulation.compute()
rating = rating_simulation.output['environmental_rating']
# print(f"Екологічний рейтинг: {rating:.2f}")
# print(calculate_rating_and_recommendation(rating))

