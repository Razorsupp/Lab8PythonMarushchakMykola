from django.contrib import admin
from .models import Errors, Programmers, BugFixes


admin.site.register(Errors)
admin.site.register(Programmers)
admin.site.register(BugFixes)