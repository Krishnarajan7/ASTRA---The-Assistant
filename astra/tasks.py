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
        if "notepad" in app_name:
            os.system("notepad")
        elif "calculator" in app_name:
            os.system("calc")
        else:
            print("Application not supported.")
    except Exception as e:
        print(f"Error opening {app_name}: {e}")

def perform_task(command, engine):
    """Perform tasks based on the voice command."""
    if "open notepad" in command:
        speak("Opening Notepad", engine)
        open_application("notepad")
    elif "open calculator" in command:
        speak("Opening Calculator", engine)
        open_application("calculator")
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
    commands = ["open notepad", "open calculator", "shutdown", "restart", "open google"]
    for command in commands:
        perform_task(command, engine)
        time.sleep(2)  # Adding a delay for demonstration purposes