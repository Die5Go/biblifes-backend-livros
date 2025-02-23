from dataclasses import dataclass
from typing import Optional


@dataclass
class Usuario:
    id: Optional[int] = None
    matricula: Optional[str]= None
    senha: Optional[str] = None