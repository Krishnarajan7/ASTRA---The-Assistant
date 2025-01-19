import pyttsx3
import speech_recognition as sr

def speak(text, engine):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen(engine):
    """Listen for voice commands and return the transcribed text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.", engine)
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.", engine)
            return ""

def greet_user(engine):
    """Greet the user based on the time of day."""
    import datetime
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        speak("Good morning!", engine)
    elif 12 <= current_hour < 18:
        speak("Good afternoon!", engine)
    else:
        speak("Good evening!", engine)

if __name__ == "__main__":
    engine = pyttsx3.init()
    greet_user(engine)
    while True:
        command = listen(engine)
        if 'exit' in command:
            speak("Goodbye!", engine)
            break
        # Add more command handling here