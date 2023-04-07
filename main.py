from fastapi import FastAPI

# インスタンス化
app = FastAPI()

# ルートにアクセスがあったら実行する
# async→非同期処理
"""
クエリパラメータ
?country_name=America&country_no=10
"""
@app.get("/countries/")
async def country(country_name: str = "japan", country_no: int = 1):
    return {
        "country_name": country_name,
        "country_no": country_no
    }

# @app.get("/countries/japan")
# async def country():
#     return {"message": "This is Japan"}