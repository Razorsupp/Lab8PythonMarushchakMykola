from django.shortcuts import render
from .models import Errors, Programmers, BugFixes

def DbDisplay(request):
    error = Errors.objects.all()
    programmer = Programmers.objects.all()
    bugfix = BugFixes.objects.all()
    return render(request, 'DisplayCompany/DbDisplay.html', {'error':error, 'programmer':programmer,'bugfix':bugfix})