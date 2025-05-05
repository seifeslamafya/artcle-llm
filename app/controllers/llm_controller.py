from fastapi import HTTPException
from ..helpers.constants import ConstResponses
from ..schemas.llm_models.request_model import RequestAnswer
from ..services.user_service import checkUser
from ..services.llm_service import askLLM
from ..config.config import Settings
from termcolor import colored
import logging


async def reviewAnswerByLLM(set_settings: Settings, request_answer: RequestAnswer):
    authorized_user = await checkUser(request_answer.token ,set_settings)
    if not authorized_user:
        # logging here
        raise HTTPException(
            status_code=401, detail=ConstResponses.UNAUTHORIZED.value)

    feedback = await askLLM(settings=set_settings, request_answer=request_answer)
    return feedback
