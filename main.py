from fastapi import FastAPI

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
@app.get("/countries/{country_name}")
async def country(country_name: str = "japan", city_name: str = "tokyo"):
    return {
        "country_name": country_name,
        "city_name": city_name
    }

# @app.get("/countries/japan")
# async def country():
#     return {"message": "This is Japan"}