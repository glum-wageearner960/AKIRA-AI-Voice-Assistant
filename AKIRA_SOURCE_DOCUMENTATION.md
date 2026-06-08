# AKIRA v1.0 Source Code Documentation

# Import Section

## import speech_recognition as sr

Definition:
Imports Speech Recognition library.

Purpose:
Converts voice into text.

---

## import pyttsx3

Definition:
Imports Text-to-Speech engine.

Purpose:
Makes AKIRA speak.

---

## import os

Definition:
Imports Operating System module.

Purpose:
Launch applications and execute system commands.

---

## import webbrowser

Definition:
Imports browser control module.

Purpose:
Open websites.

---

## import datetime

Definition:
Imports date and time module.

Purpose:
Time and Date features.

---

## import psutil

Definition:
Imports system monitoring library.

Purpose:
Battery, CPU and RAM monitoring.

---

## import pyautogui

Definition:
Imports automation library.

Purpose:
Screenshots.

---

## import keyboard

Definition:
Imports keyboard simulation library.

Purpose:
Volume and media control.

---

## import screen_brightness_control as sbc

Definition:
Imports brightness controller.

Purpose:
Brightness adjustment.

---

## import socket

Definition:
Imports networking module.

Purpose:
Internet connectivity checks.

---

## from pathlib import Path

Definition:
Imports path management system.

Purpose:
Folder and file handling.

---

## from ai_chat import ask_ai

Definition:
Imports AI communication function.

Purpose:
Connect AKIRA to Ollama AI.

---

# Initialization

## recognizer = sr.Recognizer()

Definition:
Creates Speech Recognition object.

Purpose:
Recognize voice commands.

---

## engine = pyttsx3.init()

Definition:
Creates Text-to-Speech engine.

Purpose:
Speak responses.

---

## SCREENSHOT_FOLDER

Definition:
Screenshot storage directory.

Purpose:
Store captured images.

Code:

Path("screenshots")

---

# Function: speak()

Code:

def speak(text):
print(text)
engine.say(text)
engine.runAndWait()

Definition:
Converts text into speech.

Purpose:
Allows AKIRA to talk.

---

## print(text)

Definition:
Displays text on terminal.

Purpose:
Debugging.

---

## engine.say(text)

Definition:
Adds speech to queue.

Purpose:
Prepare speech.

---

## engine.runAndWait()

Definition:
Executes speech queue.

Purpose:
Actually speak.

---

# Function: listen()

Definition:
Captures voice input.

Purpose:
Understand user commands.

---

## sr.Microphone(device_index=1)

Definition:
Select microphone.

Purpose:
Receive audio.

---

## adjust_for_ambient_noise()

Definition:
Measures background noise.

Purpose:
Improve accuracy.

---

## recognizer.listen()

Definition:
Records voice.

Purpose:
Capture command.

Parameters:

timeout=5

phrase_time_limit=5

---

## recognizer.recognize_google()

Definition:
Converts speech to text.

Purpose:
Understand spoken words.

---

## text.lower()

Definition:
Converts text to lowercase.

Purpose:
Easy command matching.

---

# Function: open_app()

Code:

os.system(app_name)

Definition:
Executes application.

Purpose:
Launch programs.

Examples:

code

spotify

notepad

calc

---

# Function: open_website()

Code:

webbrowser.open(url)

Definition:
Open URL in browser.

Purpose:
Access websites.

---

# Function: take_screenshot()

Definition:
Capture current screen.

Purpose:
Store screenshots.

---

## datetime.now()

Definition:
Current date and time.

Purpose:
Unique filename.

---

## pyautogui.screenshot()

Definition:
Capture screen image.

Purpose:
Screenshot creation.

---

## screenshot.save()

Definition:
Store screenshot file.

Purpose:
Save image.

---

# Function: wifi_status()

Definition:
Checks internet availability.

Purpose:
Network monitoring.

---

## socket.create_connection()

Definition:
Attempts internet connection.

Purpose:
Verify connectivity.

---

# Function: battery_status()

Definition:
Returns battery percentage.

Purpose:
Battery monitoring.

---

## psutil.sensors_battery()

Definition:
Reads battery information.

Purpose:
Battery status.

---

# Function: cpu_status()

Definition:
Returns CPU utilization.

Purpose:
Performance monitoring.

---

## psutil.cpu_percent()

Definition:
CPU usage percentage.

Purpose:
Performance tracking.

---

# Function: ram_status()

Definition:
Returns RAM utilization.

Purpose:
Memory monitoring.

---

## psutil.virtual_memory()

Definition:
Reads memory information.

Purpose:
RAM statistics.

---

# Function: volume_up()

Definition:
Increase volume.

Purpose:
Audio control.

---

## keyboard.press_and_release("volume up")

Definition:
Simulates keyboard volume key.

Purpose:
Increase sound.

---

# Function: volume_down()

Definition:
Decrease volume.

Purpose:
Audio control.

---

# Function: mute_volume()

Definition:
Mute audio.

Purpose:
Silence sound.

---

# Function: brightness_up()

Definition:
Increase screen brightness.

Purpose:
Display control.

---

## sbc.get_brightness()

Definition:
Current brightness.

Purpose:
Brightness calculation.

---

## sbc.set_brightness()

Definition:
Set brightness value.

Purpose:
Adjust brightness.

---

# Function: brightness_down()

Definition:
Decrease brightness.

Purpose:
Display control.

---

# Function: play_music()

Definition:
Play or pause media.

Purpose:
Media control.

---

## play/pause media

Definition:
Multimedia key.

Purpose:
Control playback.

---

# Function: next_song()

Definition:
Skip to next track.

Purpose:
Music control.

---

# Function: previous_song()

Definition:
Go to previous track.

Purpose:
Music control.

---

# Function: open_downloads()

Definition:
Open Downloads folder.

Purpose:
Quick access.

---

# Function: open_documents()

Definition:
Open Documents folder.

Purpose:
Quick access.

---

# Function: open_desktop()

Definition:
Open Desktop folder.

Purpose:
Quick access.

---

# Wake Word Logic

Code:

if any(word in wake_word for word in wake_words)

Definition:
Checks wake words.

Purpose:
Activate AKIRA.

Supported:

akira

akira boss

hey akira

---

# Command Processing

Definition:
Matches command against conditions.

Purpose:
Execute correct action.

Method:

if

elif

else

---

# AI Integration

Definition:
Connects AKIRA with Llama 3.2.

Function:

ask_ai()

Purpose:
Generate intelligent responses.

---

# Ollama

Definition:
Local AI runtime.

Purpose:
Run AI without cloud APIs.

Command:

ollama run llama3.2:3b

---

# Llama 3.2

Definition:
Large Language Model.

Purpose:
Question answering.

---

# Automatic AI Fallback

Code:

else:

```
answer = ask_ai(command)
```

Definition:
Unknown commands sent to AI.

Purpose:
Natural assistant behavior.

---

# Project Architecture

User Voice
↓

Speech Recognition
↓

Command Text
↓

Command Processor

↓

Known Command
→ Execute Function

OR

Unknown Command
↓

Llama 3.2 AI
↓

Answer
↓

Text To Speech
↓

Voice Output

---

# AKIRA v1.0 Final Result

Voice Assistant:
Completed

System Controls:
Completed

AI Integration:
Completed

Offline Operation:
Completed

Testing:
Completed

Status:
SUCCESSFULLY COMPLETED
