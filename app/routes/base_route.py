import os
from fastapi import FastAPI, APIRouter, Depends

from ..helpers.constants import ConstProjectConfig
from ..config.config import get_settings, Settings
base_router = APIRouter(
    prefix="/api/v1",
    tags=["Base Router"]
)


@base_router.get("/")
async def base_route(app_settings: Settings = Depends(get_settings)):

    app_name = app_settings.PROJECT_NAME
    app_version = app_settings.PROJECT_VERSION
    return {
        "APP_NAME": app_name,
        "APP_VERSION": app_version
    }

