from fastapi import APIRouter
from models.cpu import cpu
from config.db import conn
from schema.cpu_schema import CPU

cpu_router = APIRouter()

@cpu_router.get('/')
async def index():
    return {"message":"PC Componentes Microservice"}

@cpu_router.get('/get_all')
async def get_all_pets():
    return conn.execute(cpu.select()).fetchall()