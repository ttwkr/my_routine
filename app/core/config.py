from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    STAGE: str
    RDS_HOST: str
    RDS_USER: str
    RDS_PW: str
    RDS_DB: str
    RDS_PORT: int
    RDS_URL: str
    MASTER_MAIL: str
    MASTER_MAIL_PW: str

    class Config:
        env_file = ".env"


class DevSettings(CommonSettings):
    class Config:
        env_file = ".env"


class ProdSettings(CommonSettings):
    class Config:
        env_file = ".env.prod"


# 환경 별로 분리
class Settings:
    @staticmethod
    def env_load():
        stage = CommonSettings().STAGE
        if stage == 'dev':
            return DevSettings()
        elif stage == 'prod':
            return ProdSettings()


settings = Settings().env_load()
