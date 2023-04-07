from fastapi import FastAPI

# インスタンス化
app = FastAPI()

# ルートにアクセスがあったら実行する
# async→非同期処理
@app.get("/countries/{country_name}")
async def country(country_name: str):
    return {"country_name": country_name}

@app.get("/countries/japan")
async def country():
    return {"message": "This is Japan"}