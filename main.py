from fastapi import FastAPI
from routes.cpu import cpu_router

app = FastAPI()

app.include_router(cpu_router)