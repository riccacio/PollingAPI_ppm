from django.contrib import admin
from .models import Poll, Choice, Response

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Response)