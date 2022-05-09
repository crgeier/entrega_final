from django.contrib import admin

from final.users.models import Avatar
from .models import *

admin.site.register(recetas)
admin.site.register(Avatar)
admin.site.register(foto)

class AvatarAdmin(admin.ModelAdmin):
    pass
    # list_display = ('user', 'imagen')

class AvatarInLineAdmin(admin.TabularInline):
    model = Avatar