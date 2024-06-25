from ninja import Schema
# from pydantic import HttpUrl



class StudentSchema(Schema):
    id: int
    first_name: str
    last_name: str
    # image: HttpUrl
    age: int
    grade: str


class TeacherSchema(Schema):
    id: int
    first_name: str
    last_name: str
    # image: HttpUrl
    teaching: str


class SchoolSchema(Schema):
    id: int
    name: str
    city: str
    level: str
    kind: str