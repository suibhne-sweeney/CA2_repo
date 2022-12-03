from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, UserCreationForm

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ["email", "username", "phone_num", "dob", "is_superuser"]

admin.site.register(CustomUser, CustomUserAdmin)
