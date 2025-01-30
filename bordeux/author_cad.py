from pydantic import BaseModel

class Author(BaseModel):
    id: int
    nick_name: str
    author_name: str
    