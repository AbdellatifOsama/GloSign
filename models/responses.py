from pydantic import BaseModel

class STTResponse(BaseModel):
    transcription: str
    def __init__(self, transcription: str):
            super().__init__(transcription=transcription)