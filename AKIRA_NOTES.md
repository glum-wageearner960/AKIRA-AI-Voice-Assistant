# AKIRA v1.0 Notes

## Project Name

AKIRA (AI Voice Assistant)

---

# What is AKIRA?

Definition:

AKIRA is an offline AI voice assistant developed using Python that can listen to voice commands, control the computer, open applications, access websites, provide system information, and answer questions using a local AI model.

Purpose:

To automate computer tasks using voice commands and provide AI-powered assistance.

---

# Project Workflow

User Voice
↓
Speech Recognition
↓
Text Command
↓
Command Processing
↓
System Action / AI Response
↓
Text To Speech
↓
Voice Output

---

# Python

Definition:

Python is a high-level programming language.

Purpose:

Used to build the entire AKIRA project.

---

# Library: speech_recognition

Definition:

A Python library that converts speech into text.

Purpose:

Used to understand user voice commands.

Import:

import speech_recognition as sr

---

# Library: pyttsx3

Definition:

Offline text-to-speech engine.

Purpose:

Used to make AKIRA speak.

Import:

import pyttsx3

---

# Library: os

Definition:

Provides operating system interaction.

Purpose:

Used to launch applications and execute system commands.

Import:

import os

---

# Library: webbrowser

Definition:

Controls the default web browser.

Purpose:

Used to open websites.

Import:

import webbrowser

---

# Library: datetime

Definition:

Provides date and time operations.

Purpose:

Used for Time and Date commands.

Import:

import datetime

---

# Library: psutil

Definition:

Provides system and hardware information.

Purpose:

Battery Monitoring

CPU Monitoring

RAM Monitoring

Import:

import psutil

---

# Library: pyautogui

Definition:

Automation library for screenshots, keyboard and mouse control.

Purpose:

Used for screenshot functionality.

Import:

import pyautogui

---

# Library: keyboard

Definition:

Allows simulation of keyboard keys.

Purpose:

Volume control

Media control

Import:

import keyboard

---

# Library: screen_brightness_control

Definition:

Controls display brightness.

Purpose:

Brightness management.

Import:

import screen_brightness_control as sbc

---

# Library: socket

Definition:

Provides network communication features.

Purpose:

Checks internet connectivity.

Import:

import socket

---

# Library: pathlib

Definition:

Modern file and folder path management.

Purpose:

Managing screenshot folder.

Import:

from pathlib import Path

---

# Library: requests

Definition:

Sends HTTP requests.

Purpose:

Communicates with Ollama AI server.

Import:

import requests

---

# Speech Recognition

Definition:

Converting spoken language into text.

Purpose:

Allows AKIRA to understand voice commands.

---

# Text To Speech

Definition:

Converting text into spoken audio.

Purpose:

Allows AKIRA to speak back to the user.

---

# Wake Word

Definition:

A trigger phrase that activates the assistant.

Supported Wake Words:

Akira

Akira Boss

Hey Akira

Purpose:

Prevents AKIRA from responding continuously.

---

# AI

Definition:

Artificial Intelligence.

Purpose:

Allows AKIRA to answer user questions.

---

# Ollama

Definition:

Local AI runtime platform.

Purpose:

Runs AI models directly on the laptop.

Benefits:

No API cost

No internet required

No usage limits

---

# Llama 3.2 3B

Definition:

Large Language Model developed by Meta.

Purpose:

Provides AI responses for AKIRA.

Command:

ollama run llama3.2:3b

---

# Screenshot System

Definition:

Captures the current screen image.

Purpose:

Save important visual information.

Storage:

screenshots folder

---

# Battery Monitoring

Definition:

Checks battery percentage.

Purpose:

Provides battery information to the user.

---

# CPU Monitoring

Definition:

Checks processor usage.

Purpose:

Monitor system performance.

---

# RAM Monitoring

Definition:

Checks memory usage.

Purpose:

Monitor system resources.

---

# WiFi Monitoring

Definition:

Checks internet connectivity.

Purpose:

Know whether the device is online.

---

# Volume Control

Definition:

Adjusts system audio level.

Commands:

Volume Up

Volume Down

Mute

---

# Brightness Control

Definition:

Adjusts display brightness.

Commands:

Brightness Up

Brightness Down

---

# Music Control

Definition:

Controls media playback.

Commands:

Play Music

Pause Music

Next Song

Previous Song

---

# Search System

Definition:

Searches information online.

Supported:

Google Search

YouTube Search

---

# Folder Access

Definition:

Opens important user folders.

Supported:

Downloads

Documents

Desktop

---

# Application Launcher

Definition:

Opens installed applications.

Supported:

VS Code

Spotify

Notepad

Calculator

Paint

File Explorer

Command Prompt

---

# Website Launcher

Definition:

Opens websites directly.

Supported:

Google

YouTube

GitHub

LinkedIn

Facebook

Instagram

ChatGPT

---

# Lock Laptop

Definition:

Locks the Windows session.

Purpose:

Security.

---

# AI Mode

Definition:

Dedicated conversation mode with AI.

Purpose:

Allows continuous interaction with Llama AI.

Command:

AI Mode

Exit AI Mode

---

# Automatic AI Mode

Definition:

Unknown commands are automatically sent to AI.

Purpose:

Provides a natural assistant experience.

---

# AKIRA v1.0 Features

Voice Recognition

Wake Word Detection

Text To Speech

Application Launcher

Website Launcher

Google Search

YouTube Search

Folder Access

Screenshot Capture

Battery Monitoring

CPU Monitoring

RAM Monitoring

WiFi Status

Volume Control

Brightness Control

Media Control

Laptop Lock

Offline AI

Local LLM Integration

---

# AKIRA v1.0 Status

Status:

Completed Successfully

Version:

1.0

Type:

Offline AI Voice Assistant

Result:

Project Successfully Built and Tested
