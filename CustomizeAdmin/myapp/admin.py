from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User 
# Unregister the provided model admin:  
admin.site.unregister(User)

from django.contrib.auth.admin import UserAdmin 
@admin.register(User) 
class NewAdmin(UserAdmin): 
    readonly_fields = [ 
        'date_joined', 
    ]  