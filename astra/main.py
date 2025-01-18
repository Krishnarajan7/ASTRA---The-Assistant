import pyttsx3
import speech_recognition as sr
from astra import speech, tasks, authentication, wake_words, scheduler
import json
import time

def load_config():
    """Load configuration from JSON file."""
    with open('config.json', 'r') as f:
        return json.load(f)

def main():
    """Main function to run ASTRA."""
    # Load settings from config file
    config = load_config()

    # Initialize text-to-speech engine
    tts_engine = pyttsx3.init()

    # Greet the user
    speech.greet_user(tts_engine)

    # Set up wake word detection
    wake_word_detector = wake_words.WakeWord(config['wake_words'], tts_engine)

    while True:
        command = speech.listen()
        
        if wake_word_detector.detect(command):
            speech.speak("Hello, how can I help you?", tts_engine)
            command = speech.listen()

            # Authentication (for critical actions)
            if "shutdown" in command or "restart" in command:
                if not authentication.authenticate():
                    speech.speak("Authentication failed.", tts_engine)
                    continue
            
            # Task execution based on the command
            tasks.perform_task(command, tts_engine)
        
        time.sleep(1)

if __name__ == "__main__":
    main()
