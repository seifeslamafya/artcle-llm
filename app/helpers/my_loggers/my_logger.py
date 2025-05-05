from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Custom middleware class
class RequestLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Log the incoming request details
        client_ip = request.client.host
        url = request.url.path
        logger.info(f"Request from IP: {client_ip}, URL: {url}")

        # Call the next middleware or endpoint
        response = await call_next(request)

        # Log the status code of the response
        logger.info(f"Response status code: {response.status_code}")
        
        return response
