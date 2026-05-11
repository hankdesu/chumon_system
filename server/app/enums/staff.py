from enum import Enum


class StaffRole(str, Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    CASHIER = "CASHIER"
    WAITER = "WAITER"
    KITCHEN = "KITCHEN"
    STAFF = "STAFF"

class ActiveStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"