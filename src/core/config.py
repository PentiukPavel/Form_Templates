from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App config
    AUTH_SECRET: str
    ERROR_LOG_FILENAME: str

    model_config = SettingsConfigDict(env_file="../.env")


settings = Settings()
