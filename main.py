from fastapi import FastAPI

app = FastAPI()

users = []

@app.post("/user")
def create_user(name: str):
    users.append(name)
    return {"message": f"User {name} created"}

@app.get("/user")
def get_user():
    return {"users": users}