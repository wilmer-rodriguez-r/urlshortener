from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_test():
    return {"message": "FastApi Run"}

@app.get("/{item_id}")
def get_item(item_id: int):
    return {"message": f"The id was {item_id}"}