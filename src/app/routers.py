from fastapi import APIRouter, HTTPException
from models import DataInput
from redis import Redis
import os

redis_client = Redis(host=os.getenv("REDIS_HOST"), port=6379, db=0)

router = APIRouter()


@router.post('/write_data')
async def write_data(data: DataInput):
    redis_client.set(data.phone, data.address)
    return {"message": "Данные успешно записаны"}


@router.get('/check_data/{phone}')
async def check_data(phone: str):
    address = redis_client.get(phone)
    if address:
        return {"address": address}
    else:
        return {"Error": "Телефон не найден!"}


@router.put("/write_data")
async def update_data(data: DataInput):
    if not redis_client.exists(data.phone):
        raise HTTPException(status_code=404, detail=f"Phone number {data.phone} not found")
    redis_client.set(data.phone, data.address)
    return {"message": "Адрес обновлен"}



