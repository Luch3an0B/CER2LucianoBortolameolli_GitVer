from django.shortcuts import render
from django.contrib.auth.models import User
from core import views

# Create your views here.


def PagHomeIndex(request):
    return render(request, 'core/home.html')

def PagUserPageIndex(request):
    return render(request, 'core/UserPage.html')


#def RegistroIndex(request):
    #if (request.POST):
        
       # nombre_usuario=request.POST[User.username]
      #  correo_usuario=request.POST[User.]

        #usuario_trabajador=User.objects.create_user[]
   # if request.POST=='POST':
    #    form=UserCreationForm()
     #   if form.is_valid():
      #      form.save()