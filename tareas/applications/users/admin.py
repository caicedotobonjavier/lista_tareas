from django.contrib import admin
#
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'address',
        'date_birth',
        'phone',
        'photo',
        'is_active',
        'is_superuser',
        'is_staff',
    )


admin.site.register(User, UserAdmin)