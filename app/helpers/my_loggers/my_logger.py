from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import logging
from termcolor import colored
from datetime import datetime

# Configure logging to save to a file
now = datetime.now()
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler(f"{now.day}{now.month}{now.year}.log", mode='a'),  # save logs to this file
        logging.StreamHandler() 
    ]
)

logger = logging.getLogger(__name__)


# Custom middleware class
class RequestLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Log the incoming request details
        
        user_agent= request.headers.get('user-agent')
        client_ip = request.client.host
        url = request.url.path
        logger.info(f"Request from IP: {client_ip}, URL: {url}")

        # Call the next middleware or endpoint
        response = await call_next(request)

        # Log the status code of the response
        logger.info(f"Response status code: {response.status_code}")
        all_logs={
            "IP":client_ip,
            "url":url,
            "status":response.status_code,
            "user_agent":user_agent,
            # "function":
        }
        print(colored(all_logs, "cyan"))
        return response
    
