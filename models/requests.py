from pydantic import BaseModel

class TTSRequest(BaseModel):
    text: str
    language: str = 'en'
    slow: bool = False
