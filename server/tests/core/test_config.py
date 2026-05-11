import pytest
from app.core.config import Setting

def test_settings_default_values():
    settings = Setting()
    assert settings.database_url == "postgresql+asyncpg://hank:12345678@127.0.0.1:5432/chumon_system"
    assert settings.echo_sql is False
    assert settings.session_id_bytes == 32
    assert settings.session_expire_at == 7 * 24 * 60 * 60

def test_settings_env_override(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://user:pass@host:port/db")
    monkeypatch.setenv("ECHO_SQL", "True")
    
    settings = Setting()
    assert settings.database_url == "postgresql+asyncpg://user:pass@host:port/db"
    assert settings.echo_sql is True
