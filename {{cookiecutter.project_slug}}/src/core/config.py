from pydantic_settings import BaseSettings


class DBConfig(BaseSettings):
    database_url: str


class AppConfig(BaseSettings):
    pass


db_config = DBConfig()
app_config = AppConfig()
