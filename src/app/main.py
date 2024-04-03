from fastapi import FastAPI
from routers import router

app = FastAPI()

# Подключаем роуты
app.include_router(router)