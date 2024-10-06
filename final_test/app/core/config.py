from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Final test AutoCareer"
    admin_email: str = "tran.chien@jvb-corp.com"
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
