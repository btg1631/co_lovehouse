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

class combined_data_rentFee(Document):
    col_0: Optional[float] = None
    col_1: Optional[float] = None
    describe: Optional[str] = None
    type: Optional[str] = None
  
    class Settings:
        name = "combined_data_rentFee"

class combined_data_deposit(Document):
    col_0: Optional[float] = None
    col_1: Optional[float] = None
    describe: Optional[str] = None
    type: Optional[str] = None
  
    class Settings:
        name = "combined_data_deposit"

