from django.contrib import admin
from .models import Teacher

# Register your models here.

@admin.register(Teacher)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields={'slug':('name',)}
    
# @admin.register(Tag)
# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields={'slug':('name',)}