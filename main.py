from fastapi.middleware.cors import CORSMiddleware
from routes.index import route
from fastapi import FastAPI

app = FastAPI(title="Hospital")


origins = [ 
    "http://localhost",
    "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Open docs for documentation"}


app.include_router(route)