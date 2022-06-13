from fastapi import FastAPI

app = FastAPI()

# minimal app - get request


@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"ping": "pong"}

# GET --> Read Todo


@app.get("/todo", tags=['todos'])
async def get_todo() -> dict:
    return {'data': todos}

# POST --> Create Todo


@app.post("/todo", tags=['todos'])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data": "todo added"
    }
# PUT --> Update Todo
# DELETE --> Delete Todo

todos = [
    {
        "id": "1",
        "activity": "jogging"
    },
    {
        "id": "2",
        "activity": "coding"
    }
]
