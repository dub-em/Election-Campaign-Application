from pydantic import BaseSettings

class Settings(BaseSettings):
    hostname: str
    name: str
    user: str
    password: str
    conn_string: str
    api_key: str
    api_key_secret: str
    access_token: str
    access_token_secret: str
    port: str

    class Config:
        env_file = ".env"

settings = Settings()