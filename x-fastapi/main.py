from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_status():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
