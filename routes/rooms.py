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
from models.data_charts import Average_Price_by_Region, combined_data_rentFee, combined_data_deposit
collection_charts = Database(Average_Price_by_Region)
collection_charts_rentfee = Database(combined_data_rentFee)
collection_charts_deposit = Database(combined_data_deposit)


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
    region_list = ['region']
    rent_list = ['rentFee']
    deposit_list = ['deposit']
    type_list = ['type']

    for i in list(data_charts):
        
        region_list.append(i.region)
        rent_list.append(i.rentFee)
        deposit_list.append(i.deposit)
        type_list.append(i.type)
        
    get_list = [region_list, rent_list, type_list, deposit_list]


    data_charts_rentfee = await collection_charts_rentfee.get_all()
    rentfee_col_0_list = ['col_0']
    rentfee_col_1_list = ['col_1']
    rentfee_describe_list = ['describe']
    rentfee_type_list = ['type']

    for i in list(data_charts_rentfee):
        
        rentfee_col_0_list.append(i.col_0)
        rentfee_col_1_list.append(i.col_1)
        rentfee_describe_list.append(i.describe)
        rentfee_type_list.append(i.type)
        
    get_list_rentfee = [rentfee_col_0_list, rentfee_col_1_list, rentfee_describe_list, rentfee_type_list]


    data_charts_deposit = await collection_charts_deposit.get_all()
    deposit_col_0_list = ['col_0']
    deposit_col_1_list = ['col_1']
    deposit_describe_list = ['describe']
    deposit_type_list = ['type']

    for i in list(data_charts_deposit):
        
        deposit_col_0_list.append(i.col_0)
        deposit_col_1_list.append(i.col_1)
        deposit_describe_list.append(i.describe)
        deposit_type_list.append(i.type)
        
    get_list_deposit = [deposit_col_0_list, deposit_col_1_list, deposit_describe_list, deposit_type_list]


    return templates.TemplateResponse(name="room/Counterproposal.html", context={'request':request,
                                                                                 'data_charts':get_list,
                                                                                 'data_charts_rentfee':get_list_rentfee,
                                                                                 'data_charts_deposit':get_list_deposit})
