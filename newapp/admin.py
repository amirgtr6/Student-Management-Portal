from django.contrib import admin

from .models import newapp
from .models import daneshjo
from .models import info_dars

admin.site.register(newapp)
admin.site.register(daneshjo)
admin.site.register(info_dars)

# Register your models here.
