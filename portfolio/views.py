from django.shortcuts import render
from .models import Projecto
# Create your views here.

#pagina principal
def home(request):
    projectos=Projecto.objects.all()
    return render(request,'portfolio/home.html', {'projectos' : projectos})
#sobre mim
def sobre(request):
    return render(request, 'portfolio/sobre.html')
