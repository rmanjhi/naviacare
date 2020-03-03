from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NAVUser


# Register your models here.
class NAVUserAdmin(UserAdmin):
    list_display = ('id', 'name','company_name', 'city', 'state', 'zip')
    search_fields = ['name']

    fieldsets = UserAdmin.fieldsets + (
        ('Profile info', {'fields': ('company_name','city','state','zip')}),
    )

admin.site.register(NAVUser, NAVUserAdmin)
