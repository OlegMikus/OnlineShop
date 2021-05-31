from django.contrib import admin

from customer.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'age', 'is_staff')
