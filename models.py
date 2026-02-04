from pydantic import BaseModel
from typing import Optional, Dict

class ScamRequest(BaseModel):
    conversation_id: str
    message: str

class ScamResponse(BaseModel):
    is_scam: bool
    extracted_data: Dict[str, Optional[str]]
    action: str
