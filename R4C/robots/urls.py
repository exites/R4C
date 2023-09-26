from django.urls import path
from .views import RobotAPIView

urlpatterns = [
    path('api/robot/', RobotAPIView.as_view(), name='robot-api'),
]