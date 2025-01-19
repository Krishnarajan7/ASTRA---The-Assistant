import pyttsx3
import speech_recognition as sr

def greet_user(tts_engine):
    """Greet the user."""
    speak("Hello dude, I know you will be here.", tts_engine)

def speak(text, tts_engine):
    """Convert text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen(tts_engine):
    """Listen for a command."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.", tts_engine)
        return ""
    except sr.RequestError:
        speak("Could not request results; check your network connection.", tts_engine)
        return ""