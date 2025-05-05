from pickle import TRUE

import requests as r
from termcolor import colored

from ..config.config import Settings


async def checkUser(token: str, settings: Settings):
    # Ask the backend if user has access to use the model
    # authorized_user=r.post(url=settings.DOMAIN_NAME,data={"token":token})
    # return authorized_user==True
    if token == "abc123token":
        print(colored(True, "green"))
        return True
    else:
        print(colored(False, "red"))
        return False
    return TRUE
