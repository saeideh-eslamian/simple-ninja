from ninja import Schema, FilterSchema, Field
from pydantic import HttpUrl
from typing import Optional
from pydantic import BaseModel


class TeacherSchema(Schema):
    id: int
    first_name: str
    last_name: str
    image: Optional[str] = None
    teaching: str


class SchoolSchema(Schema):
    id: int
    name: str
    city: str
    level: str
    kind: str
    teachers: list[TeacherSchema]


class StudentSchema(Schema):
    id: int
    first_name: str
    last_name: str
    image: Optional[str] = None
    age: int
    grade: str
    teachers: list[TeacherSchema]
    school : SchoolSchema

class StudentFilterSchema(FilterSchema):
    age: Optional[int] = Field(None)
    teachers: Optional[list[str]] = Field(None)
    school: Optional[str] = Field(None, q='school__name__icontains')

class ErrorSchema(Schema):
    message: str    

class LoginSchema(BaseModel):
    username: str
    password: str    