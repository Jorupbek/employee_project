from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin, MPTTModelAdmin
from employee.models import Division, Employee, Position


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'slug', 'position')
    prepopulated_fields = {"slug": ("full_name",)}


@admin.register(Division)
class DivisionAdmin(MPTTModelAdmin):
    list_display = ('title', 'slug',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
