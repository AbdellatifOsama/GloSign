from models.responses import STTResponse
from models.requests import TTSRequest
from services import TTS, STT
import uuid
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse,JSONResponse
import os
from fastapi import UploadFile, File

app = FastAPI(title="Text-to-Speech and Speech-to-Text API")



@app.post("/generate-speech/")
async def generate_speech(request: TTSRequest):
    """
    Generate an audio file from input text using Google Text-to-Speech
    """
    filepath, filename = TTS.generate_speech_file(
        text=request.text, 
        language=request.language, 
        slow=request.slow
    )
    
    return FileResponse(
        filepath, 
        media_type="audio/mpeg", 
        filename=filename,
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )


    
@app.post("/transcribe-speech/")
async def recognize_speech(file: UploadFile = File(...)):
    # Save the uploaded file to disk temporarily
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(await file.read())

    # Use the class to recognize speech from the file
    speech_recognition_app = STT.SpeechRecognitionApp()
    try:
        transcript = speech_recognition_app.recognize_speech_from_file(temp_file_path)
        os.remove(temp_file_path)  # Clean up temporary file
        if transcript:
            res = STTResponse(transcript)
            return res
        else:
            return JSONResponse(content={"error": "Could not understand audio."}, status_code=400)
    except Exception as e:
        os.remove(temp_file_path)  # Clean up temporary file
        return JSONResponse(content={"error": str(e)}, status_code=500)

    
    


    

