from pydantic import BaseSettings


class Settings(BaseSettings):
    RDS_HOST: str
    RDS_USER: str
    RDS_PW: str
    RDS_DB: str
    RDS_PORT: int

    class Config:
        env_file = ".env"


settings = Settings()
RDS_URL = "postgresql://{}:{}@{}:{}/{}".format(
    settings.RDS_USER,
    settings.RDS_PW,
    settings.RDS_HOST,
    settings.RDS_PORT,
    settings.RDS_DB
)
