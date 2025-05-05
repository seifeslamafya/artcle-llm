from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    
    PROJECT_NAME: str
    PROJECT_VERSION: str
    MODEL_NAME: str
    PORT: int
    DOMAIN_NAME: str

    class config:
        env_file = ".env"

def get_settings():
    return Settings()