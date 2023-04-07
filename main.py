from fastapi import FastAPI
from typing import Optional

# インスタンス化
app = FastAPI()

# ルートにアクセスがあったら実行する
# async→非同期処理
"""
クエリパラメータ
?country_name=America&country_no=10

パスパラメータとクエリパラメータ
america?city_name=newyork
"""
@app.get("/countries/")
async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
    return {
        "country_name": country_name,
        "country_no": country_no
    }

# @app.get("/countries/japan")
# async def country():
#     return {"message": "This is Japan"}