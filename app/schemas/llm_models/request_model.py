from pydantic import BaseModel, Field, field_validator


class RequestAnswer(BaseModel):
    token: str = Field(..., description="Token is required")
    question: str = Field(..., description="Question is required")
    model_answer: str = Field(..., description="Correct model answer")
    student_answer: str = Field(..., description="Student's submitted answer")

    @field_validator("question")
    @classmethod
    def validate_question(cls, value: str):
        if not value.strip():
            raise ValueError("Question is required and cannot be empty")
        return value

    @field_validator("token", "question", "model_answer", "student_answer")
    @classmethod
    def no_blank_fields(cls, value: str, info):
        if not value.strip():
            raise ValueError(
                f"{info.field_name.replace('_', ' ')} can not be empty")
        return value
