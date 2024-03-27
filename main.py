
import requests,datetime,os

APP_ID=os.environ["NT_APP_ID"]
API_KEY=os.environ["NT_API_KEY"]
SHEET_ENDPOINT=os.environ["SHEET_ENDPOINT"]
EXERCISE_ENDPOINT=os.environ["EXERCISE_ENDPOINT"]

exercise=input("Tell me which exercises you did: ")

parameters={
    'query':exercise
}

headers={
    'x-app-id':APP_ID,
    'x-app-key':API_KEY
}

response=requests.post(url=EXERCISE_ENDPOINT,headers=headers,json=parameters)
response.raise_for_status()
result=response.json()

exercises=result['exercises']
today=datetime.datetime.now()

for exercise in result['exercises']:

    sheet_inputs={
        "workout":{
            "time":today.strftime("%X"),
            "date":today.strftime("%d/%m/%Y"),
            "calories":exercise['nf_calories'],
            "duration":exercise['duration_min'],
            "exercise":exercise['name'].title()
        }
    }
    
    sheet_response=requests.post(url=SHEET_ENDPOINT,json=sheet_inputs)
    sheet_response.raise_for_status()
