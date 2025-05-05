from app.schemas.llm_models.request_model import RequestAnswer
from ..config.config import Settings
from ..helpers.constants import llm_instructions
import ollama
import time
import json
from termcolor import colored


def create_prompet(instruction, target_text):
    return "".join(["".join(instruction), "".join(target_text)])


def run_local_llm(instruction, target_text):
    """
    LLM takes the instructions and the target text and return a text depening on the instruction
    """

    response = {}
    start_time = time.time()
    prom = create_prompet(instruction, target_text)

    response["response"] = ollama.chat(
        model="llama3",
        messages=[
            {"role": "user", "content": prom},
        ],
    )
    end_time = time.time()
    response["time"] = end_time - start_time
    print(colored(type(response), "red"))
    print(colored(response, "green"))
    print(colored(response["response"]["message"]["content"], "cyan"))

    return response["response"]["message"]["content"]


async def askLLM(settings: Settings, request_answer: RequestAnswer):
    model_name = settings.MODEL_NAME
    target_text = f"question: {request_answer.question} \n model_answer: {request_answer.model_answer} \n student_answer: {request_answer.student_answer}"
    llm_response = run_local_llm(
        instruction=llm_instructions, target_text=target_text)
    return json.loads(llm_response)
