from routes.pasien import pasien
from fastapi import APIRouter

route = APIRouter()

route.include_router(pasien, prefix="/api/v1", tags=["Pasien"])