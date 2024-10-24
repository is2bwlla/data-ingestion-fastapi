from pydantic.v1 import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    # Configurações gerais usadas na aplicação

    API_V1_STR: str = '/api/v1'
    DB_URL: str = "mysql+asyncmy://root@127.0.0.1:3306/foods"
    DBBaseModel = declarative_base()

class Config:
    case_sensitive = False
    venv_file = "venv"

settings = Settings()