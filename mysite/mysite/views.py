from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    if request.user.is_authenticated:
        return render(request=request, template_name="templates/mysite/index.html", context={"is_authenticated": False})
    else:
        return render(request=request, template_name="templates/mysite/index.html", context={"is_authenticated": True})