from fastapi import FastAPI

from src.auth.routers import router_auth
from src.media_upload.routers import media_upload_router

app = FastAPI(title='Test_task_Bewise.ai')
app.include_router(router_auth)
app.include_router(media_upload_router)
