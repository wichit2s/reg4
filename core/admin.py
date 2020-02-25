from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Member)
admin.site.register(Note)
admin.site.register(Curriculum)
admin.site.register(Course)
admin.site.register(Student)
