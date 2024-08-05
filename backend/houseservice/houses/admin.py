from django.contrib import admin


from .models import House
from .models import Checker


admin.site.register(House)
admin.site.register(Checker)
