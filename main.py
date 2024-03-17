from fastapi import FastAPI
from src.auth.router import auth_router
from src.database import Base, engine



app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get('/')
def hello_world():
    return {'message' : 'Hello World!'}


app.include_router(auth_router)