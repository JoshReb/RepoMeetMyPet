from .models import Mascota
from django.shortcuts import render
#from django.http import Http404


def index(request):
    num_visits=request.session.get('num_visits',0)
    num_visits=request.session['num_visits']=num_visits+1
    contexto={'num_visits':num_visits,}
    return render(request,'catalog/index.html', contexto)


def publicaciones(request):
    return render(request,'catalog/publicaciones.html')

def galeria(request):
    return render(request,'catalog/galeria.html')

def ingresar(request):
    return render(request,'catalog/ingresar.html')

def registrarse(request):
    return render(request,'catalog/registrarse.html')

def detalle_publicaciones(request):
    return render(request,'catalog/detalle_publicaciones.html')

def login(request):
    return render(request,'registration/login.html')

def logged_out(request):
    return render(request,'registration/logged_out.html')

def Mascota(request):
    mascotas = Mascota.objects.all()
    contexto = { 
        'mascotas':mascotas,
        }
    return render(request, 'catalog/mascota.html', contexto)


from django.views import generic
from .models import Mascota
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

class MascotaView(generic.ListView):
    template_name = 'catalog/mascota.html'
    context_object_name = 'mascotas'
    def get_queryset(self):
        return Mascota.objects.all()

class DetailView(generic.DetailView):
    model = Mascota
    template_name = 'catalog/detail.html'

class MascotaCreate(CreateView):
    model = Mascota
    fields= [ 'nombre', 'tipo', 'raza', 'sexo', 'descripcion', 'foto']

class MascotaUpdate(UpdateView):
    model = Mascota
    fields= [ 'nombre', 'tipo', 'raza', 'sexo', 'descripcion', 'foto']

class MascotaDelete(DeleteView):
    model = Mascota
    success_url = reverse_lazy('mascota')