# 🤖 AKIRA - Personal AI Voice Assistant

## Overview

AKIRA is a Python-based AI Voice Assistant designed to automate everyday laptop tasks using voice commands. It combines speech recognition, desktop automation, system monitoring, and AI-powered conversations into a single assistant.

The assistant continuously listens for the wake word **"Akira"** and executes commands such as opening applications, controlling system settings, taking screenshots, searching the web, and answering questions using a local AI model.

---

## Features

### Voice Interaction

* Wake Word Detection ("Akira")
* Speech Recognition
* Text-to-Speech Responses

### Application Control

* Open Applications
* Close Current Application
* Open File Explorer
* Open Command Prompt

### Web Automation

* Open Google
* Open YouTube
* Open GitHub
* Open LinkedIn
* Open ChatGPT
* Google Search
* YouTube Search

### System Monitoring

* Battery Status
* CPU Usage
* RAM Usage
* WiFi Status
* Time and Date Information

### System Control

* Lock Laptop
* Sleep Laptop
* Volume Control
* Brightness Control

### Productivity Features

* Screenshot Capture
* Open Downloads Folder
* Open Documents Folder
* Open Desktop Folder

### Media Controls

* Play Music
* Pause Music
* Next Track
* Previous Track

### AI Integration

* Local AI Chat using Ollama
* Natural Language Question Answering
* Offline AI Processing

---

## Technologies Used

### Programming Language

* Python 3.10

### Libraries

* SpeechRecognition
* Pyttsx3
* PyAutoGUI
* Psutil
* Keyboard
* Screen Brightness Control
* Pathlib
* Socket
* Datetime
* OS

### AI Technologies

* Ollama
* Llama 3.2 Model

---

## Project Structure

AKIRA/

├── jarvis.py

├── ai_chat.py

├── unlock_greeting.py

├── .env

├── dist/

├── screenshots/

├── logs/

├── AKIRA_NOTES.md

├── AKIRA_SOURCE_DOCUMENTATION.md

└── AKIRA_INTERVIEW_PREPARATION.md

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd AKIRA
```

### Install Dependencies

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install pyautogui
pip install psutil
pip install keyboard
pip install screen-brightness-control
pip install python-dotenv
pip install ollama
```

### Install Ollama

Download and install Ollama from:

https://ollama.com

Pull the model:

```bash
ollama pull llama3.2:3b
```

---

## Running AKIRA

### Python Mode

```bash
python jarvis.py
```

### Executable Mode

```bash
pyinstaller --onefile jarvis.py
```

Run:

```bash
dist/jarvis.exe
```

---

## Example Commands

### Applications

* Open Spotify
* Open Notepad
* Open Calculator
* Open Paint
* Open VS Code
* Close Application

### Websites

* Open Google
* Open YouTube
* Open GitHub
* Open LinkedIn

### System

* Battery Status
* CPU Status
* RAM Status
* Lock Laptop
* Sleep Laptop

### AI

* What is Machine Learning?
* Explain Artificial Intelligence
* Tell me about Python

---

## Workflow

User Voice

↓

Speech Recognition

↓

Command Processing

↓

System Action / AI Response

↓

Text-To-Speech Output

---

## Challenges Faced

* Microphone Detection
* Startup Automation
* AI API Quota Issues
* Offline AI Integration
* Screenshot Path Management
* Background Execution

---

## Future Improvements

* GUI Dashboard
* Offline Speech Recognition
* Smart Reminders
* Personal Memory System
* Advanced Desktop Automation
* Mobile Integration

---

## Author

Akhil Kumar

Personal AI Assistant Project - AKIRA V1.0
