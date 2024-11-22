import os
import logging
import schedule  
import requests 
import send_email as email
from dotenv import load_dotenv
load_dotenv()
recipient_email = os.getenv("RECIPIENT_EMAIL")
api_key = os.getenv("API_KEY")

def check_weather():
    try:
        sky,temperature = "Rainy","10 C"
        city = "Lahore"

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            sky = data['weather'][0]['description']
        else:
            logging.error(f"Error: {data['message']}")
        sky=sky.upper()
        if sky == "RAINY" or sky == "HAZY" or sky == "SHOWERS":
            subject="Weather reminder!!!"
            body = f"Take a raincoat before leaving the house.\
                Weather condition for today is {sky} and temperature is {temperature} in {city}."
            #send email
            email.send_email(recipient_email,subject,body)
    except Exception as e:
        logging.error(str(e))

#Schedule the weather reminder for particular time everyday.
schedule.every().day.at("20:38").do(check_weather) 
while True: 
    schedule.run_pending() 