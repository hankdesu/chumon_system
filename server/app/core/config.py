from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):
    database_url: str = (
        "postgresql+asyncpg://hank:12345678@127.0.0.1:5432/chumon_system"
    )
    echo_sql: bool = False
    session_id_bytes: int = 32
    session_expire_at: int = 7 * 24 * 60 * 60

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Setting()
