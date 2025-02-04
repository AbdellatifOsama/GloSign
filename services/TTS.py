from gtts import gTTS
import os
import uuid
from fastapi import HTTPException
from fastapi.responses import FileResponse

def generate_speech_file(text: str, language: str = 'en', slow: bool = False):
    """
    Generate speech file from text
    """
    try:
        # Generate a unique filename
        filename = f"{uuid.uuid4()}.mp3"
        filepath = os.path.join("speech_outputs", filename)
        
        # Ensure output directory exists
        os.makedirs("speech_outputs", exist_ok=True)
        
        # Create TTS object
        tts = gTTS(text=text, lang=language, slow=slow)
        
        # Save the audio file
        tts.save(filepath)
        
        return filepath, filename
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))