from pydantic import BaseModel


class Path(BaseModel):
    path: object


class ItemBase(BaseModel):
    title: str
    description: str
# https://drive.google.com/uc?export=download&id=1YDtdlEIAYNUPIA9lklOYD0J4qcjLZ56i

class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True