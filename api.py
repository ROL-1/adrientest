from fastapi import FastAPI, Request
import uvicorn
import pandas as pd

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "ONLINE"}



@app.get("/test/{key_word}")
async def test(key_word):
    return f" le keyword est {key_word}"

@app.get("/hello/")
def read_main(request: Request):
    return {"message": (f"Hello World"), "root_path": request.scope.get("root_path")}


# lancer le serveur en local :
# uvicorn api:app --reload




















if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


