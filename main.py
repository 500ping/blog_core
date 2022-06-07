from fastapi import FastAPI
import uvicorn

from src.routers import router

HOST = 'localhost'
PORT = 8000

app = FastAPI()
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run("main:app", host=HOST, port=PORT, log_level="info", reload=True)
