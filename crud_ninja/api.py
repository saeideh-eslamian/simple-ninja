from typing import Any
from django.conf import settings
from django.contrib.auth import authenticate
from django.http import HttpRequest
from ninja import Query
from ninja.responses import codes_4xx
from django.shortcuts import get_object_or_404
from ninja.security import APIKeyHeader
import jwt
from django.db.models import Q
from ninja_extra import NinjaExtraAPI, api_controller, http_post
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.tokens import RefreshToken

# All import from our apps and project
from .models import Student,Teacher, School
from .schema import (
    StudentSchema,
    TeacherSchema, 
    SchoolSchema, 
    StudentFilterSchema, 
    ErrorSchema, 
    LoginSchema
)

# class ApiKey(APIKeyHeader):
#     param_name = "Authorization"

#     def authenticate(self, request: HttpRequest, key: str | None) -> Any | None:
#         try:
#             access_token = key.split(" ")[1]
#             data = jwt.decode(access_token, settings.SECRET_KEY, algorithms=["HS256"])
#             request.auth = data
#         except jwt.DecodeError as e:  
#             return e  
#         return data
    
# header_key = ApiKey()    

# create instance NinjaAPI
api = NinjaExtraAPI()

# login
@api_controller('')
class AuthController:
    @http_post('/login')
    def login(self, request, data: LoginSchema):
        user = authenticate(username=data.username, password=data.password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        else:
            return api.create_response(request, {"error": "Invalid credentials"}, status=401)
        
# For access the endpoint that difine in AuthController class
api.register_controllers(AuthController)


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
           full_name = teacher_name.split(" ")
           if len(full_name)>=2:
               first_name =full_name[0]
               last_name = full_name[1]
               q |= Q(teachers__first_name__icontains=first_name) | Q(teachers__last_name__icontains=last_name)
           else: 
               name = full_name[0]
               q |= Q(teachers__first_name__icontains=name) | Q(teachers__last_name__icontains=name) 
           

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

@api.delete("/students/{student_id}", auth=JWTAuth())
def delete_student(request, student_id: int):
    student = get_object_or_404(Student, id=student_id)
    message = f'{student.first_name} {student.last_name} deleted successfully'
    student.delete()
    return {"success": True, "message": message}

@api.delete("/teachers/{teacher_id}", auth=JWTAuth())
def delete_teacher(request, teacher_id: int):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    message = f'{teacher.first_name} {teacher.last_name} deleted successfully'
    teacher.delete()
    return {"success": True, "message": message}

@api.delete("/schools/{school_id}", auth=JWTAuth())
def delete_school(request, school_id: int):
    school = get_object_or_404(Student, id=school_id)
    message = f'{school.name} deleted successfully'
    school.delete()
    return {"success": True, "message": message}