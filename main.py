from fastapi import FastAPI
#from routes.cpu import cpu_router

app = FastAPI()

@app.get('/')
async def index():
    return {"message":"PC Componentes Microservice"}
#app.include_router(cpu_router)