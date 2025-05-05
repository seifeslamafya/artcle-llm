from enum import Enum


class ConstResponses(Enum):
    INVALID_REQUEST_DATA = "The request data is invalid."
    MISSING_PARAMETER = "Required parameter is missing."
    UNAUTHORIZED = "Unauthorized access."
    FORBIDDEN = "You do not have permission to access this resource."
    NOT_FOUND = "The requested resource was not found."
    INTERNAL_SERVER_ERROR = "An internal server error occurred."
    SUCCESS = "Request was successful."
    CREATED = "Resource has been successfully created."
    UPDATED = "Resource has been successfully updated." 
    DELETED = "Resource has been successfully deleted."
    INVALID_INPUT = "The input provided is invalid."
    UNPROCESSABLE_ENTITY = "The request is well-formed but cannot be processed."
    TOO_MANY_REQUESTS = "You have made too many requests. Please try again later."
    SERVICE_UNAVAILABLE = "The service is temporarily unavailable. Please try again later."


class ConstProjectConfig(Enum):
    PROJECT_NAME = "PROJECT_NAME"
    PROJECT_VERSION = "PROJECT_VERSION"
    MODEL_NAME = "MODEL_NAME"
    PORT = "PORT"


llm_instructions = [
    "You will be given a question, the model answer, and the student's answer.",
    "Your job is to check if the student's answer is correct.",
    "1. **Accuracy**: Is the student's answer correct based on the correct answer?",
    "2. **Clarity**: Is the student's answer easy to understand?",
    "If the student's answer is wrong, tell them what is wrong and how to fix it.",
    "Do not add any extra information or introductions. Just focus on the answer and explanation.",
    "Don't add any introduction or unnecessary details.",
    """
    Respond only in the following JSON format:
    {
    "status": "correct or wrong",
    "explanation": "brief explanation of why the answer is correct or not"
    }
    """,
    "respond as you are talking to the student",
    "answer using the same language of the question language make only the explaination answer in the same language of the question"
]

llm_instructions_ar= [
    "سيتم تزويدك بسؤال، وإجابة نموذجية، وإجابة الطالب.",
    "مهمتك هي التحقق مما إذا كانت إجابة الطالب صحيحة.",
    "1. **Accuracy**: Is the student's answer correct based on the correct answer?",
    "2. **Clarity**: Is the student's answer easy to understand?",
    "إذا كانت إجابة الطالب خاطئة، وضّح له الخطأ وبيّن له كيف يصحح إجابته.",
    "لا تُضف أي معلومات إضافية أو مقدمات. ركّز فقط على الإجابة والتفسير.",
    "لا تضف أي مقدمة أو تفاصيل غير ضرورية.",
    """
    Respond only in the following JSON format:
    {
    "status": "correct or wrong",
    "explanation": "brief explanation of why the answer is correct or not"
    }
    """,
    "أجب وكأنك تتحدث مع الطالب.",
    "استخدم نفس لغة السؤال في الرد، وقدم الشرح بنفس لغة السؤال فقط."
]
