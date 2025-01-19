import pyttsx3
import speech_recognition as sr
import speech, tasks, authentication, wakewords, scheduler
import json
import time

def load_config():
    """Load configuration from JSON file."""
    with open('config.json', 'r') as f:
        return json.load(f)

def set_female_voice(tts_engine):
    """Set the text-to-speech engine to use a female voice."""
    voices = tts_engine.getProperty('voices')
    for voice in voices:
        if 'female' in voice.name.lower():
            tts_engine.setProperty('voice', voice.id)
            break

def main():
    """Main function to run ASTRA."""
    # Load settings from config file
    config = load_config()

    # Initialize text-to-speech engine
    tts_engine = pyttsx3.init()

    # Set the engine to use a female voice
    set_female_voice(tts_engine)

    # Greet the user
    speech.greet_user(tts_engine)

    # Set up wake word detection
    wake_word_detector = wakewords.WakeWord(config['wake_words'], tts_engine)

    while True:
        command = speech.listen(tts_engine)
        print(f"Command received: {command}")
        
        if wake_word_detector.detect(command):
            speech.speak("Hello, how can I help you?", tts_engine)
            command = speech.listen(tts_engine)
            print(f"Command after wake word: {command}")

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