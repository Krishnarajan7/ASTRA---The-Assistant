import pyttsx3
import speech_recognition as sr
import json
import time
import speech
import tasks
import wakewords
import scheduler

def load_config():
    """Load configuration from JSON file."""
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Config file not found.")
        return {}
    except json.JSONDecodeError:
        print("Error decoding the config file.")
        return {}

def set_female_voice(tts_engine):
    """Set the text-to-speech engine to use a female voice."""
    try:
        voices = tts_engine.getProperty('voices')
        for voice in voices:
            if 'female' in voice.name.lower() or 'zira' in voice.name.lower() or 'female' in voice.id.lower():
                tts_engine.setProperty('voice', voice.id)
                # print(f"Female voice set to: {voice.name}")
                return
        print("No female voice found. Using the default voice.")
    except Exception as e:
        print(f"An error occurred while setting the voice: {e}")

def authenticate():
    """Authenticate the user for critical tasks."""
    try:
        # Prompt the user to enter their password
        password = input("Enter password: ")
        
        # Replace this with a more secure authentication system
        # For demonstration, we're using a hardcoded password (not recommended for production)
        if password == "sample_pass":
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred during authentication: {e}")
        return False

def handle_command(command, tts_engine, wake_word_detector):
    """Handle the received command."""
    if wake_word_detector.detect(command):
        try:
            speech.speak("Hello, how can I help you?", tts_engine)
            command = speech.listen(tts_engine)
            print(f"Command after wake word: {command}")

            # Authentication (for critical actions)
            if "shutdown" in command or "restart" in command:
                if not authenticate():
                    speech.speak("Authentication failed.", tts_engine)
                    return
            
            # Task execution based on the command
            tasks.perform_task(command, tts_engine)
        except Exception as e:
            print(f"An error occurred while handling the command: {e}")

def main():
    """Main function to run ASTRA."""
    # Load settings from config file
    config = load_config()

    # Initialize text-to-speech engine
    tts_engine = pyttsx3.init()

    # Set the engine to use a female voice
    set_female_voice(tts_engine)
    

    # Greet the user
    try:
        speech.greet_user(tts_engine)
    except Exception as e:
        print(f"An error occurred while greeting the user: {e}")

    # Set up wake word detection
    wake_word_detector = wakewords.WakeWord(config.get('wake_words', []), tts_engine)

    while True:
        try:
            command = speech.listen(tts_engine)
            print(f"Command received: {command}")
            handle_command(command, tts_engine, wake_word_detector)
        except Exception as e:
            print(f"An error occurred: {e}")
        
        time.sleep(1)

if __name__ == "__main__":
    main()