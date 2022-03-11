from fastapi import FastAPI
from routes.user import user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Crud api",
    version="0.0.1",
    openapi_tags=[{"name": "users", "description": "Routes"}],
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
