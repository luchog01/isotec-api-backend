from fastapi import HTTPException

class EmailAlreadyRegisteredError(HTTPException):
    def __init__(self, email: str):
        super().__init__(status_code=400, detail=f"Email {email} already registered")

class InvalidCredentialsError(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="Invalid credentials")