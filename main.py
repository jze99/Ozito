from fastapi import FastAPI
from router import router
from database import create_tables, delete_tables
import uvicorn 


from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    print("БД готова к работе")
    yield
    print("Выключение")
    
app = FastAPI(title="Ozito", lifespan=lifespan)
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080)