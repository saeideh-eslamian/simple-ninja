from ninja import Schema, FilterSchema, Field
from typing import Optional
from pydantic import BaseModel


class TeacherSchema(Schema):
    id: Optional[int] = None
    first_name: str
    last_name: str
    image: Optional[str] = None
    teaching: str

class CreateTeacherSchema(Schema):
    first_name: str
    last_name: str
    image: Optional[str] = None
    teaching: str    


class SchoolSchema(Schema):
    id: Optional[int] = None
    name: str
    city: str
    level: str
    kind: str
    teachers_id: Optional[list[int]]

class CreateSchoolSchema(Schema):
    name: str
    city: str
    level: str
    kind: str
    teachers_id: Optional[list[int]]    


class StudentSchema(Schema):
    id: Optional[int] = None
    first_name: str
    last_name: str
    image: Optional[str] = None
    age: int
    grade: str
    teachers_id: list[int]
    school_id : Optional[int]

class CreateStudentSchema(Schema):
    first_name: str
    last_name: str
    image: Optional[str] = None
    age: int
    grade: str
    teachers_id: list[int]
    school_id: Optional[int]    

class StudentFilterSchema(FilterSchema):
    age: Optional[int] = Field(None)
    teachers: Optional[list[str]] = Field(None)
    school: Optional[str] = Field(None, q='school__name__icontains')

class ErrorSchema(Schema):
    message: str    

class LoginSchema(BaseModel):
    username: str
    password: str    