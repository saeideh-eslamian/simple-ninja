from ninja import NinjaAPI
from .models import Student,Teacher, School
from .schema import StudentSchema, TeacherSchema, SchoolSchema

api = NinjaAPI()

# CRUD IN NINja

#1- Create(C): http method post 
# @api.post("/create-student")
# def create_student(request):
#     pass


#2- Update(U): http method Put


#3- Read(R): http method get
@api.get("/students/", response={200: list[StudentSchema]})
def show_students(request):
    """return a list of all students"""
    students = Student.objects.all()
    return list(students)

@api.get("/teachers/", response={200: list[TeacherSchema]})
def show_teachers(request):
    """return a list of all teachers"""
    teachers = Teacher.objects.all()
    return list(teachers)

@api.get("/schools/", response={200: list[SchoolSchema]})
def show_schools(request):
    """return a list of all schools"""
    Schools = School.objects.all()
    return list(School)

#4- Delete(D): http method delete 