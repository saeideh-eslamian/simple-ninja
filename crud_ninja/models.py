from django.db import models
from django.core.exceptions import ValidationError

def validate_grade(grade):
    if grade < 1 or grade > 12:
        raise ValidationError(f'{grade} is not a valid grade. Grade must be between 1 and 12.')
    
def validate_age(age) :
    if age<6 or  age>19:  
        raise ValidationError(f'{age} is not a valid age. Age must be between 6 and 19.')

class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='teacher_image/', null=True, blank=True)
    teaching = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class School(models.Model):
    STATE = 'state'
    PRIVATE = 'private'
    BOARDING = 'boarding'
    SCHOOL_KIND_CHOICES = [
        (STATE, 'State school'),
        (PRIVATE, 'Private school'),
        (BOARDING, 'Boarding school'),
    ]

    PRIMARY = 'primary'
    HIGH = 'high'
    SCHOOL_LEVEL_CHOICES = [
        (PRIMARY, 'Primary school'),
        (HIGH, 'High school'),
    ]

    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    level = models.CharField(
        max_length=50,
        choices=SCHOOL_LEVEL_CHOICES,
        default=PRIMARY,
    )
    kind = models.CharField(
        max_length=50,
        choices=SCHOOL_KIND_CHOICES,
        default=STATE
    )
    teachers = models.ManyToManyField(Teacher, related_name='schools')

    def __str__(self):
        return f'{self.name} : {self.city}'

    def total_student(self):
        return self.student_set.count()

    def total_teacher(self):
        return self.teachers.count()


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='student_image/', null=True, blank=True)
    age = models.PositiveIntegerField(validators=[validate_age])
    grade = models.PositiveIntegerField(validators=[validate_grade])
    teachers = models.ManyToManyField(Teacher, related_name='students')
    school = models.ForeignKey(School, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.first_name} {self.last_name} : {self.grade}'
