from pydantic_settings import BaseSettings


class DBConfig(BaseSettings):
    database_url: str


class AppConfig(BaseSettings):
    jwt_secret_key: str


db_config = DBConfig()
app_config = AppConfig()
