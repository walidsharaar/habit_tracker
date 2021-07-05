
#NUTRITIONIX API
import requests
import  datetime

APP_ID="556100f8"
API_KEY="ad751b7cbd87d4473e63406e2de5d1e3—"
EXERCISE_END_POINT= "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_END_POINT="https://api.sheety.co/0a9f127e197081af144d45ebf7e54d3e/workoutsTracking/workouts"
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

#----------------- insert data into sheet-------------#


today_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%d%m%Y")

for exercise in result["exercises"]:
    sheet_inputs={
        "workout":{
            "date": today_date,
            "time":now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }
    sheet_response= requests.post(SHEET_END_POINT,json=sheet_inputs)
    print(sheet_response.text)

# Authentication

sheet_response = requests.post(
    SHEET_END_POINT,
    json=sheet_inputs,
    auth=(
        "mytestusername",
        "mytestpassword"
         )
)

# Bearer Token Authentication

bearer_headers={
    "Authorization":"Bearer This is a sample token"
}

sheet_response = requests.post(
    SHEET_END_POINT,
    json=sheet_inputs,
    headers=bearer_headers
)