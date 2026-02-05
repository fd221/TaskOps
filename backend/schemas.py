from pydantic import BaseModel, EmailStr, ConfigDict


# Схема для создания пользователя
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password_hash: str


# Схема для ответа
class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr