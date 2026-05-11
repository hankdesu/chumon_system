class AppException(Exception):
    def __init__(self, error_code: str, message: str, status_code: int = 400):
        self.error_code = error_code
        self.message = message
        self.status_code = status_code


class InvalidCredentialsException(AppException):
    def __init__(self, message: str = "Wrong username or password!"):
        super().__init__("1001", message, 401)


class InvalidSessionException(AppException):
    def __init__(self, message: str = "Invalid or expired session!"):
        super().__init__("1002", message, 401)


class InvalidStaffException(AppException):
    def __init__(self, message: str = "Invalid staff!"):
        super().__init__("1003", message, 401)


class AuthenticationRequiredException(AppException):
    def __init__(self, message: str = "Authentication required!"):
        super().__init__("1004", message, 401)


class DatabaseRecordNotFoundException(AppException):
    def __init__(self, message: str = "Database record not found!"):
        super().__init__("1005", message, 404)
