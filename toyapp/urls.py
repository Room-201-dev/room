from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('work_space/', views.WorkSpace.as_view(), name='work_space'),
    path('work_space/export', views.export, name='export_excel'),
]
