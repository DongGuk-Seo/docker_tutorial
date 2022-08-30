import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.environ["PORT"]))


# docker run -it -p 8000:8000 {IMAGE's: id}
## -> 8000:8000 -> {myport} : {docker's port}
