import pytest
from datetime import datetime, timezone, timedelta
from app.core.auth import verify_password, generate_session_data, hash_password
from app.core.config import settings

def test_hash_and_verify_password():
    password = "test_password"
    hashed = hash_password(password)
    assert hashed != password
    assert verify_password(password, hashed) is True
    assert verify_password("wrong_password", hashed) is False

def test_generate_session_data():
    session_data = generate_session_data()
    
    assert "new_session_id" in session_data
    assert "expire_date" in session_data
    assert len(session_data["new_session_id"]) > 0
    
    # Check if expire_date is roughly settings.session_expire_at seconds from now
    now = datetime.now(timezone.utc)
    expected_expire = now + timedelta(seconds=settings.session_expire_at)
    
    # Allow for a small time difference (e.g., 2 seconds)
    assert abs((session_data["expire_date"] - expected_expire).total_seconds()) < 2
