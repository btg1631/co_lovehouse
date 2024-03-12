from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from beanie import init_beanie

router = APIRouter()

templates = Jinja2Templates(directory="templates/")
from databases.connections import Database
from models.rooms import ROOM_DATA
collection_rooms = Database(ROOM_DATA)
from models.data_charts import Average_Price_by_Region
collection_charts = Database(Average_Price_by_Region)


# 방 찾기
@router.get("/find_rooms", response_class=HTMLResponse)
async def find_rooms(request:Request):
    search_dict = {'room_brand': 'none', 'room_type': 'none', 'search': ''}
    room_list = await collection_rooms.get_all()
    return templates.TemplateResponse(name="room/find_rooms.html", context={'request':request,
                                                                            'search_dict':search_dict,
                                                                            'rooms':room_list})
import re
# 방 찾기 (selcet 태그로 검색하기 추가)
@router.post("/find_rooms")
async def find_rooms(request:Request):
    search_dict = dict(await request.form())
    conditions = {}
    if search_dict['search'] != '':
        regex_pattern = re.compile(search_dict['search'], re.IGNORECASE)
        conditions['$or'] = [
            {'room_brand': {'$regex': regex_pattern}},
            {'room_local': {'$regex': regex_pattern}},
            {'room_title': {'$regex': regex_pattern}}
        ]

    room_list = await collection_rooms.getsbyconditions(conditions)

    message = "일치하는 검색 결과가 없습니다."

    return templates.TemplateResponse(name="room/find_rooms.html", context={'request':request,
                                                                            'search_dict':search_dict,
                                                                            'rooms':room_list,
                                                                            'message': message})

from beanie import PydanticObjectId
# 방 세부내용
@router.get("/room_details/{object_id}")
async def room_detail(request:Request, object_id:PydanticObjectId):
    search_dict = dict(await request.form())
    room_list = await collection_rooms.get(object_id)
    print(room_list)
    return templates.TemplateResponse(name="room/room_details.html", context={'request':request,
                                                                            'search_dict':search_dict,
                                                                            'rooms':room_list})


# 운명의 방 찾기
@router.get("/ML_find_rooms")
async def ML_find_rooms(request:Request):
    return templates.TemplateResponse(name="room/ML_find_rooms.html", context={'request':request})


# 구글 차트
@router.get("/data_chart")
async def Counterproposal(request:Request):
    data_charts = await collection_charts.get_all()

    return templates.TemplateResponse(name="room/Counterproposal.html", context={'request':request,
                                                                                 'data_charts':data_charts})


