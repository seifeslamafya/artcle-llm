import os
from fastapi import FastAPI, APIRouter, Depends, Request

from ..helpers.constants import ConstProjectConfig
from ..config.config import get_settings, Settings
from ..helpers.my_loggers.my_logger_decorator import log_action
base_router = APIRouter(
    prefix="/api/v1",
    tags=["Base Router"]
)


@base_router.get("/")
@log_action
async def base_route(request: Request,app_settings: Settings = Depends(get_settings)):

    app_name = app_settings.PROJECT_NAME
    app_version = app_settings.PROJECT_VERSION
    print("---------------Base_route---------------")
    return {
        "APP_NAME": app_name,
        "APP_VERSION": app_version
    }

