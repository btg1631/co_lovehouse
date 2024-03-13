from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

# 개발자 실수로 들어가는 field 제한
class Average_Price_by_Region(Document):
    region: Optional[str] = None
    deposit: Optional[float] = None
    rentFee: Optional[float] = None
    type: Optional[str] = None
  
    class Settings:
        name = "Average_Price_by_Region"


