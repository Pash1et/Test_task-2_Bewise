from pydantic import BaseModel


class UserOut(BaseModel):
    id: str
    UUID: str

    class Config:
        orm_mode = True
