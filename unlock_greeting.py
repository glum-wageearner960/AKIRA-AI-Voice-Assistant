import pyttsx3
import datetime

engine = pyttsx3.init()

now = datetime.datetime.now()

current_time = now.strftime("%I:%M %p")
current_day = now.strftime("%A")
current_date = now.strftime("%d %B %Y")

message = (
    f"Welcome back Boss. "
    f"Today is {current_day}. "
    f"The date is {current_date}. "
    f"The time is {current_time}"
)

engine.say(message)
engine.runAndWait()