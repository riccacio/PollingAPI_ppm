from django.contrib import admin
from .models import Poll, Question, Response

admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Response)