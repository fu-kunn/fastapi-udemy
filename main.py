from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel

"""
セクション4:FastAPI超入門
27~
"""
class ShopInfo(BaseModel):
    name: str
    location: str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

# ShopInfoとItemをベースにクラスを作成している
class Data(BaseModel):
    shop_info: Optional[ShopInfo] = None
    items: List[Item]

# インスタンス化
app = FastAPI()

@app.post("/")
async def index(data: Data):
    return {"data": data}




# ルートにアクセスがあったら実行する
# async→非同期処理
"""
セクション4:FastAPI超入門
22~26

クエリパラメータ
?country_name=America&country_no=10

パスパラメータとクエリパラメータ
america?city_name=newyork
"""
# @app.get("/countries/")
# async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
#     return {
#         "country_name": country_name,
#         "country_no": country_no
#     }

# @app.get("/countries/japan")
# async def country():
#     return {"message": "This is Japan"}