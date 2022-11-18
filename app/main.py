from fastapi import FastAPI

from app.api.ordering import checkout

app = FastAPI()

app.include_router(checkout.router)
