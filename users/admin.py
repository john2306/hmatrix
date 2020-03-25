from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin 

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
# Register your models here.
class CustomUserResource(resources.ModelResource):
    class Meta:
        model = CustomUser

class CustomUserAdmin(ImportExportModelAdmin,admin.ModelAdmin): # new
    search_fields = ['username']
    list_display = ('username','email','estado','date_creation','age','is_staff',)
    resources_class = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)

