import speech_recognition as sr

class SpeechRecognitionApp:
    def recognize_speech_from_file(self, file_path):
        recognizer = sr.Recognizer()
        try:
            with sr.AudioFile(file_path) as source:
                audio = recognizer.record(source)
                transcript = recognizer.recognize_google(audio)
            return transcript
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            raise Exception(f"Speech recognition request failed: {e}")
