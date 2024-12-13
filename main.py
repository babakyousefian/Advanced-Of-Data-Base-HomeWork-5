
from fastapi import FastAPI
from myRouter.my_Router import my_Router

app = FastAPI()

app.include_router(my_Router)

@app.get("/Items/Details/hello/")
async def print_hello() -> dict:
    return {"your output is : ":"hi there...!!!"}

