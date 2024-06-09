from django.urls import path
from . import views

app_name = 'curso' 

urlpatterns = [
    path('', views.cursos, name='index'),
    path('curso/<int:curso_id>/', views.curso_detail_view, name='curso_detail'),
    path('projeto/<int:projeto_id>/', views.projeto_detail_view, name='projeto_detail'),
    path('new/', views.create_curso, name='curso_create'),
    path('edit/<int:pk>/', views.update_curso, name='curso_edit'),
    path('delete/<int:pk>/', views.delete_curso, name='curso_delete'),
    path('area-cientifica/create/', views.create_area_cientifica, name='area_cientifica_create'),
    path('area-cientifica/<int:pk>/update/', views.update_area_cientifica, name='area_cientifica_update'),
    path('area-cientifica/<int:pk>/delete/', views.delete_area_cientifica, name='area_cientifica_delete'),
    path('docente/create/', views.docente_create, name='docente_create'),
    path('docente/<int:pk>/update/', views.docente_update, name='docente_update'),
    path('docente/<int:pk>/delete/', views.docente_delete, name='docente_delete'),
    path('create/', views.create_disciplina, name='create_disciplina'),
    path('update/<int:pk>/', views.update_disciplina, name='update_disciplina'),
    path('disciplina/delete/<int:pk>/', views.delete_disciplina, name='delete_disciplina'),
]