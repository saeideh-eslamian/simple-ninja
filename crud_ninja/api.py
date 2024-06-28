from typing import Any
from django.conf import settings
from django.http import HttpRequest
from ninja import NinjaAPI, Query
from django.shortcuts import get_object_or_404
from ninja.security import APIKeyHeader
import jwt
from django.db.models import Q

# All import from our apps and project
from .models import Student,Teacher, School
from .schema import StudentSchema, TeacherSchema, SchoolSchema, StudentFilterSchema

class ApiKey(APIKeyHeader):
    param_name = "Authorization"

    def authenticate(self, request: HttpRequest, key: str | None) -> Any | None:
        try:
            access_token = key.split(" ")[1]
            data = jwt.decode(access_token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.DecodeError as e:  
            return e  

        return data
    
header_key = ApiKey()    

# create instance NinjaAPI
api = NinjaAPI()


# CRUD IN NINja

#1- Create(C): http method post 
# @api.post("/create-student", auth=header_key)
# def create_student(request, sudent: StudentSchema):
#     pass


#2- Update(U): http method Put


#3- Read(R): http method get
@api.get("/students/", response=list[StudentSchema])
def show_students(request, filters: StudentFilterSchema = Query(...)):
    """return a list of all students"""
    students = Student.objects.all()

    # Apply filters dynamically
    if filters.age is not None:
        students = students.filter(age=filters.age)
    if filters.teachers is not None:
        q = Q()
        for teacher_name in filters.teachers:
           q |= Q(teachers__first_name__icontains=teacher_name) | Q(teachers__last_name__icontains=teacher_name)
        students = students.filter(q)
    if filters.school is not None:
        students = students.filter(school__name__icontains=filters.school)
    return list(students)

@api.get("/teachers/", response=list[TeacherSchema])
def show_teachers(request):
    """return a list of all teachers"""
    teachers = Teacher.objects.all()
    return list(teachers)

@api.get("/schools/", response=list[SchoolSchema])
def show_schools(request):
    """return a list of all schools"""
    schools = School.objects.all()
    return list(schools)

@api.get("/student/{student_id}", response=StudentSchema)
def show_students(request, student_id:int):
    """return a Specefic student by id for show details"""
    student = get_object_or_404(Student, pk=student_id)
    return student

@api.get("/teacher/{teacher_id}", response=TeacherSchema)
def show_teachers(request, teacher_id:int):
    """return a Specefic teacher by id for show details"""
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    return teacher

@api.get("/school/{school_id}", response=SchoolSchema)
def show_schools(request, school_id:int):
    """return a Specefic school by id for show details"""
    teacher = get_object_or_404(School, pk=school_id)
    return teacher

#4- Delete(D): http method delete 