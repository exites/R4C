from django.urls import path

from . import views
from .views import RobotAPIView, index_view


urlpatterns = [
    path('', index_view, name='index'),
    path('api/robot/', RobotAPIView.as_view(), name='robot-api'),
    path('robots/generate_excel_summary/', views.generate_excel_summary,
         name='generate_excel_summary'),

]