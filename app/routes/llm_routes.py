from http.client import HTTPException
from fastapi import APIRouter, Depends

from ..controllers.llm_controller import reviewAnswerByLLM
from ..config.config import get_settings, Settings
from ..schemas.llm_models.request_model import RequestAnswer
from ..helpers.my_loggers.my_logger_decorator import log_action
llm_router = APIRouter(
    prefix="/api/v1/llm",
    tags=["LLM"]
)

@llm_router.post("/review-answer/")
@log_action
async def review_answer(request_answer: RequestAnswer, settings: Settings = Depends(get_settings)):
    llm_response = await reviewAnswerByLLM(set_settings=settings, request_answer=request_answer)
    return llm_response
