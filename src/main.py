from fastapi import FastAPI
from src.auth.routers import router_auth


app = FastAPI(title='Test_task_Bewise.ai')
app.include_router(router_auth)
