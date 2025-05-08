from fastapi import Request, Response
from fastapi.responses import JSONResponse
from functools import wraps
from termcolor import colored


def log_action(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Try to find the Request object
        request: Request = kwargs.get("request")
            
        method = request.method if request else "NULL"
        ip = request.client.host if request else "NULL"
        brower = request.headers.get("user-agent") if request else "NULL"
        function_name=func.__name__
        client_id="1234"

        print(colored(f"[{method}] Function name: {func.__name__} -------------------", "green"))

        result = await func(*args, **kwargs)
        if not isinstance(result, Response):
            result = JSONResponse(content=result)
        code=result.status_code

        
        print(colored(f"[{method}] Status code: {result.status_code} -------------------", "cyan"))

        log_data={
            "method":method,
            "client_id":client_id,
            "function_name":function_name,
            "ip":ip,
            "brower":brower,
            "code":code,
        }
        print(colored(f"{log_data}", "red"))
        return result

    return wrapper
