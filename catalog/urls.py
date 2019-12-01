from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('publicaciones/', views.publicaciones, name='publicaciones'),
    path('galeria', views.galeria, name='galeria'),
    path('ingresar', views.ingresar, name='ingresar'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('detalle_publicaciones', views.detalle_publicaciones, name='detalle_publicaciones'),
    path('login', views.login, name='login'),
    path('logged_out', views.logged_out, name='logged_out'),

    #path('mascota/', views.mascota, name='mascota'),
    path('mascota/', views.MascotaView.as_view(), name='mascota'),
    path('mascota/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('mascota/create', views.MascotaCreate.as_view(), name='mascota-create'),
    path('mascota/<int:pk>/update', views.MascotaUpdate.as_view(), name='mascota-update'),
    path('mascota/<int:pk>/delete', views.MascotaDelete.as_view(), name='mascota-delete'),
]