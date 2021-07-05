
#NUTRITIONIX API
import requests

APP_ID="556100f8"
API_KEY="ad751b7cbd87d4473e63406e2de5d1e3	—"
EXERCISE_END_POINT= "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "Male"
WEIGHT_KG = "85"
HEIGHT_CM = "187"
AGE = "28"
exercise_text = input("Indicate done exercise: ")

headers={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}

parameters={
    "query":exercise_text,
    "gender":GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(EXERCISE_END_POINT, json=parameters, headers=headers)
result= response.json()
print(result)