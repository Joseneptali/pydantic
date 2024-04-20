from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
def hello_world_check():
    return{
        "msg":"hola mundo"
    }

if __name__ == "__main__":
    uvicorn.run("main:app",
                host="localhost",
                reload= True)