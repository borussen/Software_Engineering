from django.urls import path
from .views import *

# api 앱 내의 url 관리
# 추후 server의 urls에 연결

urlpatterns = [
    path("classes/", getClasses),
    path("classes/<int:id>/enroll/", enrollClasses),
    path("classes/<int:id>/", getIdClasses),
]