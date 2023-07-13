from django.contrib import admin
from .models import *


class What_you_learn_TabulaInline(admin.TabularInline):
    model = What_you_learn

class Requirements_TabulaInline(admin.TabularInline):
    model = Requirements

class course_admin(admin.ModelAdmin):
    inlines = (What_you_learn_TabulaInline, Requirements_TabulaInline)





admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Course, course_admin)
admin.site.register(Level)
admin.site.register(What_you_learn)
admin.site.register(Requirements)
