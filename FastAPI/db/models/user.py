# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=20480

### User model ###

from pydantic import BaseModel  #BaseModel transforma el objeto User en un Json
from typing import Optional


class User(BaseModel):
    id: Optional[str]
    username: str
    email: str
