from django.urls import path
from .views import EstudianteView, DetailView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns =[
    path('materia_notas_reprobadas/', views.materia_notas_reprobadas, name='materia_notas_reprobadas'),
    path('', EstudianteView.as_view(), name='estudiantes_list'),
    path('details/<int:pk>', DetailView.as_view(), name='estudiantes_detail'),
    path('desercion/', views.desercion, name='desercion' ),
    path('desercion_ciudades/', views.view_deserciones_por_ciudad, name='desercion_ciudades' ),
    path('view_estudiantes_por_materia/', views.view_estudiantes_por_materia, name='estudiantes_materia'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='base/login.html'), name="logout"),
]