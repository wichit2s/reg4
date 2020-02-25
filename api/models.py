from django.db import models
from rest_framework import serializers

from core.models import *

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = [ 'username', 'first_name', 'last_name', 'email', 'avatar', 'dob' ]

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = [ 'id', 'text', 'member' ]

class CurriculumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curriculum
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
