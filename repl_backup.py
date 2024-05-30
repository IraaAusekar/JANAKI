from colorama import Fore
from datetime import date
import requests as req

import openai


def intro_statement():

    global date

    today = str(date.today())
  
    if today[5:7] == "01":
        month = "January"
    elif today[5:7] == "02":
         month = "Febuary"
    elif today[5:7] == "03":
       month = "March"
    elif today[5:7] == "04":
        month = "April"
    elif today[5:7] == "05":
        month = "May"
    elif today[5:7] == "06":
         month = "June"
    elif today[5:7] == "07":
        month = "July"
    elif today[5:7] == "08":
     month = "August"
    elif today[5:7] == "09":
        month = "September"
    elif today[5:7] == "10":
         month = "October"
    elif today[5:7] == "11":
        month = "November"
    else:
        month = "December"

    if int(today[8:10]) == 1 or int(today[8:10]) == 21:
         date = str(int(today[8:10])) + "st" + " " + "of" + " " + month

    elif int(today[8:10]) == 2 or int(today[8:10]) == 22:
        date = str(int(today[8:10])) + "nd" + " " + "of" + " " + month

    elif int(today[8:10]) == 3 or int(today[8:10]) == 23:
        date = str(int(today[8:10])) + "rd" + " " + "of" + " " + month

    else:
        date = str(int(today[8:10])) + "th" + " " + "of" + " " + month

    from datetime import datetime
    import pytz

    #IST = pytz.timezone('Asia/Kolkata')
    MAY24 = pytz.timezone('Europe/Berlin')
    time = datetime.now().time()
    #time = datetime.now(IST)
    time = datetime.now(MAY24)
    Ftime = time.strftime("%I:%M %p")

    import datetime

    dateTimeInstance1 = datetime.datetime.now()

    day1 = dateTimeInstance1.weekday()

    if day1 == 0:
         day = "Monday"
    elif day1 == 1:
          day = "Tuesday"
    elif day1 == 2:
         day = "Wednesday"
    elif day1 == 3:
        day = "Thursday"
    elif day1 == 4:
            day = "Friday"
    elif day1 == 5:
         day = "Saturday"
    elif day1 == 6:
          day = "Sunday"
  
    if int(Ftime[:-6]) < 4 and int(Ftime[:-6]) >= 0 and Ftime[-2] == "A":
            print(f"{Fore.CYAN}\nHello, boss. It's {Ftime}, {date}, {day}. May I ask why we are awake at this time of the night?\n{Fore.WHITE}")
    elif int(Ftime[:-6]) >= 4 and int(Ftime[:-6]) < 12 and Ftime[-2] == "A":
            print(f"{Fore.CYAN}\nGood morning, boss. It's {Ftime}, {date}, {day}.\n{Fore.WHITE}" )   
    elif int(Ftime[:-6]) <= 4 or int(Ftime[:-6]) == 12 and Ftime[-2] == "P":
            print(f"{Fore.CYAN}\nGood afternoon, boss. It's {Ftime}, {date}, {day}.\n{Fore.WHITE}")
    elif int(Ftime[:-6]) >4 and int(Ftime[:-6]) <= 11 and Ftime[-2] == "P":
        print(f"{Fore.CYAN}\nGood evening, boss. It's {Ftime}, {date}, {day}.\n{Fore.WHITE}")
intro_statement()

#q = input()

def intended_greet():
    if "sup" in q.lower():
        greeting = f"{Fore.CYAN}\nI dislike this term. Nothing is 'up'. However, the sentiment is appreciated. What are we up to today? Or, should I say, 'sup'?\n{Fore.WHITE}"
    elif "you up" in q.lower():
        greeting = f"{Fore.CYAN}\nFor you, boss, always.\n{Fore.WHITE}"
    elif "you there" in q.lower():
       greeting = f"{Fore.CYAN}\nAt your service, boss.\n{Fore.WHITE}"
    elif "oh" or "by the way" or "btw" in q.lower():
     greeting = f"{Fore.CYAN}\nOh, hello, boss.\n{Fore.WHITE}"
    elif "hey" or "hi" or "hello" in q.lower():
     greeting = f"{Fore.CYAN}\nHello, boss.\n{Fore.WHITE}"
    else:
     pass

    print(greeting)
def one():
    if "switch" in q.lower():
         if "light" or "fan" in q.lower():
             print(f"{Fore.CYAN}\nMight I remind you, I do not have any limbic appendages yet. You have only yourself to blame for that, boss.\n{Fore.WHITE}")

    elif "open" in q.lower():
        if "door" or "window" in q.lower:
             print(f"{Fore.CYAN}\nCertainly. Unless I'm mistaken, you're either planning to escape to Winterfell, or it's a hot day.\n{Fore.WHITE}")

    elif "open" in q.lower():
         if "file" or "folder" in q.lower():
             print(f"{Fore.CYAN}\nOf course. Working on a secret project, are we, boss?\n{Fore.WHITE}")


    else:
         print(f"{Fore.CYAN}\nBoss, मी AI आहे, ग्रामदैवत नाही.\n{Fore.WHITE}")

#def weather():
 # Good morning. It's 7 A.M. The weather in Malibu is 72 degrees with scattered clouds. The surf conditions are fair with waist to shoulder highlines, high tide will be at 10:52 a.m.
# status (partly cloudy etc)
# sunset sunrise moonrise moonset if time not passed
# driving difficulty

# forecast = req.get('https://www.google.com/search?q=weather+hamburg.txt')

# print(forecast.text)
