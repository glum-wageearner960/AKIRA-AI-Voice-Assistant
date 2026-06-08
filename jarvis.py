import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime
import psutil
import pyautogui
import keyboard
import screen_brightness_control as sbc
import socket
import pygetwindow as gw
from pathlib import Path
from ai_chat import ask_ai


# =========================
# INITIALIZATION
# =========================

recognizer = sr.Recognizer()
engine = pyttsx3.init()

SCREENSHOT_FOLDER = Path.home() / "Pictures" / "AKIRA Screenshots"

SCREENSHOT_FOLDER.mkdir(
    parents=True,
    exist_ok=True
)

OPENED_APPS = {
    "spotify": "spotify.exe",
    "notepad": "notepad.exe",
    "calculator": "CalculatorApp.exe",
    "paint": "mspaint.exe",
    "edge": "msedge.exe",
    "chrome": "chrome.exe",
    "whatsapp": "WhatsApp.exe",
    "vs code": "Code.exe"
}

#Close current app

def close_current_app():

    try:

        active_window = gw.getActiveWindow()

        if active_window:

            active_window.close()

            speak("Application closed")

        else:

            speak("No active application found")

    except Exception as e:

        print(e)

        speak("Unable to close application")

# =========================
# SPEAK
# =========================

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# =========================
# LISTEN
# =========================

def listen():

    with sr.Microphone(device_index=1) as source:

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(
            source,
            timeout=5,
            phrase_time_limit=5
        )

    text = recognizer.recognize_google(audio)

    return text.lower()

# =========================
# OPEN APP
# =========================

def open_app(app_name):

    print("Opening:", app_name)

    os.system(app_name)

# =========================
# OPEN WEBSITE
# =========================

def open_website(url):

    print("Opening Website")

    webbrowser.open(url)

# =========================
# SCREENSHOT
# =========================

def take_screenshot():

    filename = datetime.datetime.now().strftime(
        "%Y%m%d_%H%M%S.png"
    )

    filepath = SCREENSHOT_FOLDER / filename

    screenshot = pyautogui.screenshot()

    screenshot.save(filepath)

    print("Saved to:", filepath)

    speak("Screenshot saved")


# =========================
# WIFI STATUS
# =========================

def wifi_status():

    try:

        socket.create_connection(
            ("8.8.8.8", 53),
            timeout=3
        )

        speak("Internet is connected")

    except:

        speak("Internet is disconnected")

# =========================
# SYSTEM INFO
# =========================

def battery_status():

    battery = psutil.sensors_battery()

    if battery:

        speak(
            f"Battery is {battery.percent} percent"
        )

def cpu_status():

    cpu = psutil.cpu_percent()

    speak(
        f"CPU usage is {cpu} percent"
    )

def ram_status():

    ram = psutil.virtual_memory().percent

    speak(
        f"RAM usage is {ram} percent"
    )

# =========================
# VOLUME
# =========================

def volume_up():

    for _ in range(5):
        keyboard.press_and_release(
            "volume up"
        )

def volume_down():

    for _ in range(5):
        keyboard.press_and_release(
            "volume down"
        )

def mute_volume():

    keyboard.press_and_release(
        "volume mute"
    )

# =========================
# BRIGHTNESS
# =========================

def brightness_up():

    current = sbc.get_brightness()[0]

    sbc.set_brightness(
        min(current + 10, 100)
    )

def brightness_down():

    current = sbc.get_brightness()[0]

    sbc.set_brightness(
        max(current - 10, 0)
    )

# =========================
# MUSIC CONTROL
# =========================

def play_music():

    keyboard.press_and_release(
        "play/pause media"
    )

def pause_music():

    keyboard.press_and_release(
        "play/pause media"
    )

def next_song():

    keyboard.press_and_release(
        "next track"
    )

def previous_song():

    keyboard.press_and_release(
        "previous track"
    )

# =========================
# FOLDERS
# =========================

def open_downloads():

    path = os.path.join(
        os.path.expanduser("~"),
        "Downloads"
    )

    os.startfile(path)

def open_documents():

    path = os.path.join(
        os.path.expanduser("~"),
        "Documents"
    )

    os.startfile(path)

def open_desktop():

    path = os.path.join(
        os.path.expanduser("~"),
        "Desktop"
    )

    os.startfile(path)

# =========================
# MAIN
# =========================

print("AKIRA started...")

wake_words = [
    "akira",
    "akira boss",
    "hey akira"
]

while True:

    try:

        wake_word = listen()

        print("You said:", wake_word)

        if any(word in wake_word for word in wake_words):

            speak("Yes Boss")

            command = listen()

            print("Command:", command)

            # APPS

            if "vs code" in command:
                open_app("code")

            elif "spotify" in command:
                open_app("spotify")

            elif "notepad" in command:
                open_app("notepad")

            elif "calculator" in command:
                open_app("calc")

            elif "paint" in command:
                open_app("mspaint")

            elif "file explorer" in command:
                open_app("explorer")

            elif "command prompt" in command or "cmd" in command:
                open_app("cmd")

            # WEBSITES

            elif "google" == command or "open google" in command:
                open_website("https://www.google.com")

            elif "youtube" == command or "open youtube" in command:
                open_website("https://www.youtube.com")

            elif "github" in command:
                open_website("https://github.com")

            elif "linkedin" in command:
                open_website("https://linkedin.com")

            elif "facebook" in command:
                open_website("https://facebook.com")

            elif "instagram" in command:
                open_website("https://instagram.com")

            elif "chatgpt" in command:
                open_website("https://chatgpt.com")

            # SEARCH

            elif "search" in command and "google" in command:

                query = command.replace(
                    "search", ""
                )

                query = query.replace(
                    "on google", ""
                )

                query = query.strip()

                open_website(
                    f"https://www.google.com/search?q={query}"
                )

            elif "search" in command and "youtube" in command:

                query = command.replace(
                    "search", ""
                )

                query = query.replace(
                    "on youtube", ""
                )

                query = query.strip()

                open_website(
                    f"https://www.youtube.com/results?search_query={query}"
                )

            # FOLDERS

            elif "downloads" in command:
                open_downloads()

            elif "documents" in command:
                open_documents()

            elif "desktop" in command:
                open_desktop()

            # TIME & DATE

            elif "time" in command:

                current_time = datetime.datetime.now().strftime(
                    "%I:%M %p"
                )

                speak(
                    f"The time is {current_time}"
                )

            elif "date" in command:

                today = datetime.datetime.now().strftime(
                    "%d %B %Y"
                )

                speak(
                    f"Today is {today}"
                )

            # SYSTEM INFO

            elif "battery" in command:
                battery_status()

            elif "cpu" in command:
                cpu_status()

            elif "ram" in command:
                ram_status()

            elif "wifi" in command:
                wifi_status()

            # SCREENSHOT

            elif "screenshot" in command:
                take_screenshot()

            # VOLUME

            elif "volume up" in command:
                volume_up()

            elif "volume down" in command:
                volume_down()

            elif "mute" in command:
                mute_volume()

            # BRIGHTNESS

            elif "brightness up" in command:
                brightness_up()

            elif "brightness down" in command:
                brightness_down()

            # MUSIC

            elif "play music" in command:
                play_music()

            elif "pause music" in command:
                pause_music()

            elif "next song" in command:
                next_song()

            elif "previous song" in command:
                previous_song()

            # LOCK LAPTOP

            elif "lock laptop" in command:

                os.system(
                    "rundll32.exe user32.dll,LockWorkStation"
                )
                
            # SLEEP PC

            elif "sleep pc" in command or "sleep laptop" in command:

                speak("Putting computer to sleep")

                os.system(
                    "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
                )
                
            #AI mode
            elif "ai mode" in command:

               speak("AI mode activated")

               while True:

                try:

                   question = listen().lower()

                   print("AI Question:", question)

                   if not question:
                    continue

                except:
                    continue

                if "exit ai mode" in question:
                   speak("Exiting AI mode")
                   break

                answer = ask_ai(question)

                print(answer)

                print(answer)
                speak("Answer generated. Check terminal for full response.")

            # CONVERSATION

            elif "how are you" in command:

                speak(
                    "I am doing well Boss"
                )

            elif "who are you" in command:

                speak(
                    "I am AKIRA your personal assistant"
                )

            elif "what is your name" in command:

                speak(
                    "My name is AKIRA"
                )

            elif "thank you" in command:

                speak(
                    "Always happy to help Boss"
                )
                
            elif "close" in command:

                   app_name = command.replace("close", "").strip()

                   if app_name in OPENED_APPS:

                      os.system(
                      f'taskkill /f /im "{OPENED_APPS[app_name]}"'
                    )

                   speak(f"{app_name} closed")
            elif "close application" in command or \
                "close current application" in command or \
                "close app" in command:

                 close_current_app()

            else:

                    speak("Application not found")

        else:

                answer = ask_ai(command)

                print("\nAI Answer:\n")
                print(answer)

                short_answer = answer[:400]

                speak(short_answer)
            

    except sr.WaitTimeoutError:
        pass

    except sr.UnknownValueError:
        pass

    except Exception as e:
        print("Error:", e)