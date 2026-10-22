from pydantic import BaseModel, ConfigDict, Field, field_validator


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserCreate(BaseModel):
    username: str
    password: str = Field(min_length=1)
    role: str = "reader"

    @field_validator("password")
    @classmethod
    def validate_password_length(cls, value: str) -> str:
        # bcrypt solo admite secretos de hasta 72 bytes, no 72 caracteres.
        if len(value.encode("utf-8")) > 72:
            raise ValueError("La contraseña no puede superar los 72 bytes")
        return value


class UserPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    role: str


class ItemCreate(BaseModel):
    name: str
    description: str = ""


class ItemPublic(ItemCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
