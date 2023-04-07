from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

"""
セクション4:FastAPI超入門
27~
"""
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

# インスタンス化
app = FastAPI()

@app.post("/item/")
async def create_item(item: Item):
    return {"message": f"{item.name}は、税込価格{int(item.price*item.tax)}円です。"}




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