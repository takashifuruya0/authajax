from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdminRev(UserAdmin):
    list_display = [*UserAdmin.list_display, 'is_pro']
    list_editable = [*UserAdmin.list_editable, 'is_pro']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': (
            'is_active', 'is_staff', 'is_pro',
            "groups", "user_permissions",
        )}),
    )


admin.site.register(User, UserAdminRev)
