from pydantic import BaseSettings

class Settings(BaseSettings):
    api_key: str 
    api_key_secret: str 
    access_token: str 
    access_token_secret: str 
    database_hostname: str
    database_name: str
    database_user: str
    database_password: str
    conn_string: str

    class Config:
        env_file = ".env"

settings = Settings()