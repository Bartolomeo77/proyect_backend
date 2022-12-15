from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('usuario',views.UsuariosView.as_view(),name='usuario'),
    path('usuario/<int:serie_id>',views.UsuarioDetailView.as_view())
]
