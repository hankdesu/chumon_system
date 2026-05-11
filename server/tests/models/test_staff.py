import pytest
from pydantic import ValidationError
from app.models.staff import Staff, StaffBase, CreateStaffDto
from app.enums.staff import StaffRole, ActiveStatus

def test_staff_base_required_fields():
    # username and password are required
    with pytest.raises(ValidationError):
        StaffBase()

def test_staff_base_defaults():
    staff = StaffBase(username="admin", password="password123")
    assert staff.username == "admin"
    assert staff.password == "password123"
    assert staff.role == StaffRole.STAFF
    assert staff.is_active == ActiveStatus.ACTIVE

def test_staff_base_custom_values():
    staff = StaffBase(
        username="manager",
        password="securepassword",
        role=StaffRole.ADMIN,
        is_active=ActiveStatus.INACTIVE
    )
    assert staff.role == StaffRole.ADMIN
    assert staff.is_active == ActiveStatus.INACTIVE

def test_create_staff_dto():
    dto = CreateStaffDto(username="newuser", password="newpassword")
    assert dto.username == "newuser"
    assert dto.password == "newpassword"

def test_staff_table_defaults():
    staff = Staff(username="user", password="pass")
    assert staff.id is None
    assert staff.created_at is None
    assert staff.updated_at is None

def test_staff_invalid_role():
    with pytest.raises(ValidationError):
        StaffBase(username="u", password="p", role="INVALID_ROLE")
