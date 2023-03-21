from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User 
# Unregister the provided model admin:  
admin.site.unregister(User)

from .models import Reservation
admin.site.register(Reservation)

from django.contrib.auth.admin import UserAdmin 
@admin.register(User) 
class NewAdmin(UserAdmin): 
    def get_form(self, request, obj=None, **kwargs): 
        form = super().get_form(request, obj, **kwargs) 
        is_superuser = request.user.is_superuser 

        if not is_superuser: 
            form.base_fields['username'].disabled = True 

        return form  