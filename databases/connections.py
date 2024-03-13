from typing import Any, List, Optional
from beanie import init_beanie, PydanticObjectId
from models.users import USER_DATA
from models.rooms import ROOM_DATA
from models.reviews import REVIEW_DATA
from models.enters_users import ENTER_USER_DATA
from models.enters_rooms import ENTER_ROOM_DATA
from models.qnas import QNA
from models.notices import NOTICE_DATA
from motor.motor_asyncio import AsyncIOMotorClient
from models.data_charts import Average_Price_by_Region
from pydantic import BaseModel

# 변경 후 코드
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    CONTAINER_PREFIX : Optional[str] = None
    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(),
                          document_models=[USER_DATA, ROOM_DATA,
                                           REVIEW_DATA,ENTER_USER_DATA,ENTER_ROOM_DATA,
                                           QNA, NOTICE_DATA, Average_Price_by_Region])
    
    class Config:
        env_file = ".env"

from utils.paginations import Paginations
class Database:
    # model = collection
    def __init__(self, model):
        self.model = model
        pass

    # 전체 리스트
    async def get_all(self):
        documents = await self.model.find_all().to_list()   # find({})
        pass
        return documents

    # 상세 보기
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)  # get = find_one
        if doc:
            return doc
        return False
    
    # 저장
    async def save(self, document) -> None:
        await document.create()
        return None
    
    # 삭제
    async def delete_one(self, id: PydanticObjectId) -> bool:
        doc = await self.model.get(id)
        if doc:
            await doc.delete()
            return True
        return False
    
    # 수정
    async def update_one(self, id: PydanticObjectId, update_dict: dict) -> bool:
        doc = await self.model.get(id)
        if doc:
            for key, value in update_dict.items():
                setattr(doc, key, value)
            await doc.save()
            return True
        return False

    
    # column 값으로 여러 Documents 가져오기
    async def getsbyconditions(self, conditions:dict) -> [Any]:
        documents = await self.model.find(conditions).to_list()  # find({})
        if documents:
            return documents
        return False    
    
    async def getsbyconditionswithpagination(self
                                             , conditions:dict, page_number) -> [Any]:
        # find({})
        total = await self.model.find(conditions).count()
        pagination = Paginations(total_records=total, current_page=page_number)
        documents = await self.model.find(conditions).skip(pagination.start_record_number).limit(pagination.records_per_page).to_list()
        if documents:
            return documents, pagination
        return False 
        

    async def fetch_data_to_dataframe():
        collection_instance = Database()  # YourCollectionClass 인스턴스 생성
        documents = await collection_instance.get_all()  # 비동기적으로 데이터 가져오기
        df = pd.DataFrame(documents)  # 데이터프레임으로 변환
        return df
