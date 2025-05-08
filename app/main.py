from .helpers.my_loggers.my_logger import  RequestLoggerMiddleware
from .routes.base_route import base_router
from json import load
from fastapi import FastAPI, Request
from dotenv import load_dotenv
from .routes.base_route import base_router
from .routes.llm_routes import llm_router
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
# from .helpers.my_loggers.logger_config import logger

load_dotenv(".env")
app = FastAPI()


app.add_middleware(RequestLoggerMiddleware)

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     # Extract the first error message
#     error_message = exc.errors()[0].get("msg", "Invalid input")
#     return JSONResponse(
#         status_code=422,
#         content={"details": error_message},
#     )

app.include_router(base_router)
app.include_router(llm_router)
