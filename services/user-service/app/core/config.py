from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):


    ENVIRONMENT: str = "local"   # ✅ default
    USER_DB_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )

settings = Settings()
