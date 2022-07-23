from pydantic import BaseModel


class UserSchema(BaseModel):

    Firstname: str
    Lastname: str
