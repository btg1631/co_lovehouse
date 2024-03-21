from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from typing import Union

# 개발자 실수로 들어가는 field 제한
class ROOM_DATA(Document):
    title: Optional[str] = None
    roomName: Optional[str] = None    
    gender: Optional[str] = None
    roomType: Optional[str] = None
    py: Optional[Union[int, float]] = None
    deposit: Optional[int] = None
    rentFee: Optional[int] = None
    region : Optional[str] = None
    brandType : Optional[str] = None
    roomOption : Optional[str] = None
    url : Optional[str] = None
    imgUrl : Optional[str] = None
  
    class Settings:
        name = "ROOM_DATA"



