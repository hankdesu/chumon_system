import pytest
from datetime import datetime, timedelta
from pydantic import ValidationError
from app.models.staff_session import StaffSession, StaffSessionBase

def test_staff_session_base_required_fields():
    # staff_id and session_id are required
    with pytest.raises(ValidationError):
        StaffSessionBase()

def test_staff_session_base_values():
    expires = datetime.now() + timedelta(hours=1)
    session = StaffSessionBase(
        staff_id=1,
        session_id="test-session-id",
        expires_at=expires
    )
    assert session.staff_id == 1
    assert session.session_id == "test-session-id"
    assert session.expires_at == expires

def test_staff_session_table_defaults():
    expires = datetime.now() + timedelta(hours=1)
    session = StaffSession(
        staff_id=1,
        session_id="test-session-id",
        expires_at=expires
    )
    assert session.id is None
    assert session.created_at is None
    assert session.updated_at is None

def test_staff_session_invalid_staff_id():
    with pytest.raises(ValidationError):
        StaffSessionBase(staff_id="not-an-int", session_id="sid")
