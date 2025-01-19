import json

class WakeWord:
    def __init__(self, wake_words, tts_engine):
        self.wake_words = wake_words
        self.tts_engine = tts_engine

    def detect(self, command):
        """Detect if a wake word is present in the command."""
        for word in self.wake_words:
            if word.lower() in command:
                return True
        return False
