import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables
pollution = ctrl.Antecedent(np.arange(0, 101, 1), 'pollution')
ph_level = ctrl.Antecedent(np.arange(0, 14.1, 0.1), 'ph_level')
temperature = ctrl.Antecedent(np.arange(0, 51, 1), 'temperature')
water_quality = ctrl.Consequent(np.arange(0, 101, 1), 'water_quality')

# Define membership functions for pollution
pollution['low'] = fuzz.trimf(pollution.universe, [0, 0, 50])
pollution['medium'] = fuzz.trimf(pollution.universe, [30, 50, 70])
pollution['high'] = fuzz.trimf(pollution.universe, [50, 100, 100])

# Define membership functions for pH level
ph_level['acidic'] = fuzz.trimf(ph_level.universe, [0, 0, 6.5])
ph_level['neutral'] = fuzz.trimf(ph_level.universe, [6, 7, 8])
ph_level['alkaline'] = fuzz.trimf(ph_level.universe, [7.5, 14, 14])

# Define membership functions for temperature
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 15])
temperature['moderate'] = fuzz.trimf(temperature.universe, [10, 20, 30])
temperature['hot'] = fuzz.trimf(temperature.universe, [25, 50, 50])

# Define membership functions for water quality
water_quality['poor'] = fuzz.trimf(water_quality.universe, [0, 0, 50])
water_quality['average'] = fuzz.trimf(water_quality.universe, [30, 50, 70])
water_quality['good'] = fuzz.trimf(water_quality.universe, [50, 100, 100])

# Define fuzzy rules
rule1 = ctrl.Rule(pollution['low'] & ph_level['neutral'] & temperature['moderate'], water_quality['good'])
rule2 = ctrl.Rule(pollution['medium'] | ph_level['acidic'] | temperature['hot'], water_quality['average'])
rule3 = ctrl.Rule(pollution['high'] | ph_level['alkaline'] | temperature['cold'], water_quality['poor'])

# Create control system
water_quality_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
water_quality_sim = ctrl.ControlSystemSimulation(water_quality_ctrl)

# Function to calculate water quality using fuzzy logic
def calculate_water_quality(pollution_level, ph, temp):
    water_quality_sim.input['pollution'] = pollution_level
    water_quality_sim.input['ph_level'] = ph
    water_quality_sim.input['temperature'] = temp
    water_quality_sim.compute()
    
    quality_score = water_quality_sim.output['water_quality']

    # Convert numeric quality score to textual description
    if quality_score <= 50:
        quality_description = "Poor"
    elif 50 < quality_score <= 70:
        quality_description = "Average"
    else:
        quality_description = "Good"

    return {
        "score": round(quality_score, 2),
        "description": quality_description
    }
