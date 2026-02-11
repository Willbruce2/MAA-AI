from fastapi import FastAPI
from routes import router

app = FastAPI(title="MAA-AI")
app.include_router(router)
