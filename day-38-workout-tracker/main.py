import requests
from datetime import datetime

APP_ID = "b4a9c1c3"
API_KEY = "23b0297139fff95875b771691072c352"

GENDER = "Male"
WEIGHT_KG = 71
HEIGHT_CM = 176
AGE = 28

today = datetime.now()
today_date = today.strftime("%Y/%m/%d")
today_time = today.strftime("%H:%M")

exercize_text = input("Tell me which exercises you did: ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

exercise_info = {
    "query": exercize_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=exercise_info, headers=headers)
workout_result = response.json()
print(workout_result["exercises"][0])

exercise_type = workout_result["exercises"][0]['name']
exercise_duration_min = workout_result["exercises"][0]['duration_min']
exercise_consumed_calories = workout_result['exercises'][0]['nf_calories']

sheety_add_row_endpoint = "https://api.sheety.co/8a1193a659d279e3e48a595d51597e2e/myWorkouts/workouts"
formatted_info = {
    "workout":
        {"date": today_date,
         "time": today_time,
         "exercise": exercise_type,
         "duration": exercise_duration_min,
         "calories": exercise_consumed_calories}
}

headers = {
    "Content-Type": "application/json"
}

response_sheety = requests.post(url=sheety_add_row_endpoint, json=formatted_info, headers=headers)
result_sheety = response_sheety.json()
print(result_sheety)