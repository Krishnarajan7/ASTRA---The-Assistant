import os
import webbrowser
import pyttsx3
import time

def speak(text, engine):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def open_application(app_name):
    """Open the specified application."""
    try:
        applications = {
            "notepad": "notepad",
            "calculator": "calc",
            "wordpad": "write",
            "paint": "mspaint"
            # Add more applications as needed
        }
        
        if app_name in applications:
            os.system(applications[app_name])
        else:
            speak("Application not supported.", engine)
    except Exception as e:
        speak(f"Error opening {app_name}: {e}", engine)

def close_application(app_name):
    """Close the specified application."""
    try:
        applications = {
            "notepad": "notepad.exe",
            "calculator": "calculator.exe",
            "wordpad": "wordpad.exe",
            "paint": "mspaint.exe"
            # Add more applications as needed
        }
        
        if app_name in applications:
            os.system(f"taskkill /f /im {applications[app_name]}")
        else:
            speak("Application not supported.", engine)
    except Exception as e:
        speak(f"Error closing {app_name}: {e}", engine)

def perform_task(command, engine):
    """Perform tasks based on the voice command."""
    if "open" in command:
        app_name = command.split("open ")[1]
        speak(f"Opening {app_name}", engine)
        open_application(app_name)
    elif "close" in command:
        app_name = command.split("close ")[1]
        speak(f"Closing {app_name}", engine)
        close_application(app_name)
    elif "shutdown" in command:
        speak("Shutting down the system", engine)
        os.system("shutdown /s /t 1")
    elif "restart" in command:
        speak("Restarting the system", engine)
        os.system("shutdown /r /t 1")
    elif "open google" in command:
        speak("Opening Google", engine)
        webbrowser.open("https://www.google.com")
    else:
        speak("Sorry, I can't help with that yet.", engine)

if __name__ == "__main__":
    engine = pyttsx3.init()
    # Example commands to test the perform_task function
    commands = ["open notepad", "close notepad", "open calculator", "close calculator", "open wordpad", "close wordpad", "open paint", "close paint", "shutdown", "restart", "open google"]
    for command in commands:
        perform_task(command, engine)
        time.sleep(2)  # Adding a delay for demonstration purposes