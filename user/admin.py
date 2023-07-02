from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_paid_user')  # update this to match your User model

admin.site.unregister(User)  # Unregister the User model
admin.site.register(User, UserAdmin)  # Register it again with the new UserAdmin
