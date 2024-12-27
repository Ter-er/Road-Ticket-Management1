from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'license_no', 'state', 'is_staff']
    search_fields = ['email', 'first_name', 'last_name', 'license_no', 'state'] # This will add a search bar in the admin page
    ordering = ['last_name'] # This will order the users by last name

    filter_horizontal = []  # Don't show filter_horizontal for non-existent fields
    list_filter = ['is_active', 'is_staff']  # Remove 'groups' from list_filter


    # Define the fields to be displayed in the admin form (remove password and add license_number)
    fieldsets = (
        (None, {'fields': ('email', 'license_no')}),  # Use 'license_number' instead of password
        ('Personal info', {'fields': ('first_name', 'middle_name', 'last_name', 'phone_no', 'address', 'state')}),  # Add 'middle_name' field
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Define which fields should appear in the add/edit form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'license_no'),  # Use 'license_number' instead of password1/password2
        }),
    )

    # Exclude 'username', 'date_joined', and 'last_login' fields
    exclude = ('username',)

    readonly_fields = ('last_login', 'date_joined', 'is_superuser', 'is_staff')  # Make 'last_login' and 'date_joined' read-only

if admin.site.is_registered(User):
    admin.site.unregister(User)


admin.site.register(User, UserAdmin)