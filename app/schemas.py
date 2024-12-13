from pydantic import BaseModel
from typing import List

class EmailRequest(BaseModel):
    recipient: str
    content: str

class BulkEmailRequest(BaseModel):
    recipients: List[str]
    content: str
