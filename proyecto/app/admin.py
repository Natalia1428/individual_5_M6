from django.contrib import admin

from app.models import Usuario

# Register your models here.
@admin.register(Usuario)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Usuario._meta.get_fields()]