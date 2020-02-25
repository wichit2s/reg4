from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class Member(AbstractUser):

    username = models.CharField(max_length=100, unique=True, verbose_name='ชื่อเข้าใช้งาน')
    first_name = models.CharField(max_length=500, verbose_name='ชื่อ')
    last_name = models.CharField(max_length=500, verbose_name='นามสกุล')
    email = models.EmailField(unique=True, primary_key=True)
    avatar =  models.ImageField(upload_to='images/avatar/',default='images/avatar/default.png')
    dob = models.DateField(default = timezone.now)

    #USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(blank=True)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Staff(models.Model):
    id                  = models.AutoField(primary_key=True)
    initial             = models.CharField(max_length=100)
    first_name          = models.CharField(max_length=200)
    last_name           = models.CharField(max_length=200)
    email               = models.EmailField()
    position            = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Curriculum(models.Model):
    id                  = models.AutoField(primary_key=True)
    thai_name           = models.CharField(max_length=300)
    english_name        = models.CharField(max_length=300)
    thai_degree         = models.CharField(max_length=300)
    english_degree      = models.CharField(max_length=300)

    def __str__(self):
        return self.thai_name

class Course(models.Model):
    id                  = models.AutoField(primary_key=True)
    thai_title          = models.CharField(max_length=300)
    english_title       = models.CharField(max_length=300)
    credits             = models.IntegerField()
    lecture             = models.IntegerField()
    laboratory          = models.IntegerField()
    self_study          = models.IntegerField()
    prerequisite        = models.CharField(max_length=500)
    corequisite         = models.CharField(max_length=500)
    thai_description    = models.CharField(max_length=2000)
    english_description = models.CharField(max_length=2000)
    curriculum          = models.ForeignKey(Curriculum, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.thai_title} ({self.english_title})'

class Student(models.Model):
    id                  = models.AutoField(primary_key=True)
    initial             = models.CharField(max_length=100)
    first_name          = models.CharField(max_length=200)
    last_name           = models.CharField(max_length=200)
    email               = models.EmailField()
    faculty             = models.CharField(max_length=200)
    curriculum          = models.ForeignKey(Curriculum, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

