from fastapi import FastAPI
import uvicorn
from core.config import get_db
from fastapi.middleware.cors import CORSMiddleware
from routes.auth_routes import router as auth_routes

from routes.user_routes import router as user_routes



#model.Base.metadata.create_all(bind=engine)


app = FastAPI()

    

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello_world_check():
    return{
        "msg":"hola mundo"
    }


#app.include_router(router=user_routes, tags=['Users'], prefix='/users')
app.include_router(router=auth_routes, tags=["Auth"], prefix="/auth")

if __name__ == "__main__":
    uvicorn.run("main:app",
                host="localhost",
                reload= True)