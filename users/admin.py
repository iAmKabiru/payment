from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Profile


class ProfileInline(admin.StackedInline): 
	model = Profile


class CustomUserAdmin(UserAdmin):
    #add_form = CustomUserCreationForm
    #form = CustomUserChangeForm
    list_display = ['username', 'first_name', 'last_name', 'email',]
    model = CustomUser
    inlines = [ProfileInline]


class ProfileAdmin(admin.ModelAdmin):
	search_fields = ['user']
	list_display = ['user', 'balance', 'department', 'is_student', 'reg_no']
	list_filter = ['is_student']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
