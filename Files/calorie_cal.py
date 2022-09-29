# Title: Calorie Calculator
# Date 9/16/2022
from Files.temperature import Temperature

# For men, BMR = 66.47 + (13.75 x weight in kg) + (5.003 x height in cm) - (6.755 x age in years)


class CalorieCalculator:
    def __init__(self, weight_lbs, height_cm, age, temperature):
        self.weight_lbs = weight_lbs
        self.height_cm = height_cm
        self.age = age
        self.temperature = temperature

    def Calculate(self):
        self.kg = self.weight_lbs / 2.205 # convert lbs to KG for below formula to work
        result = 10 * self.kg + 6.5 * self.height_cm + 5 - self.temperature * 10
        return round(result, 2)




# create a Temperature class to retrive locations current temperature

if __name__ == "__main__":
    state = input("What state are you in?")
    city = input("What city are you in?")
    temperature = Temperature(state + " ", city + " ").Get()
    calorie = CalorieCalculator(weight_lbs=170, height_cm=175, age=39, temperature=temperature)
    print(f"You would need to consume {calorie.Calculate()} calories today.")

