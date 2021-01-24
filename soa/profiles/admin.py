from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    # ...
    empty_value_display = '-empty-'
    fields = ('user', 'image')
    list_display = ('user_id', '__getFullName__', '__getUsername__', "__str__", '__getGroups__', '__isActive__', '__isTeacher__',)
    list_display_links = ('__getFullName__', 'user_id')
    search_fields = ['user_id', 'user__username', 'user__first_name', 'user__last_name', 'user__email',]

admin.site.register(Profile,ProfileAdmin)