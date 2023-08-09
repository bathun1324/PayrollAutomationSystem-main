from django.urls import path, re_path
from apps.home import views
from django.views.generic import TemplateView
from apps.home.api.management import *
from apps.home.api.login import *

urlpatterns = [
    # The home page
    path('get_departments/', DepartmentAPIView.as_view()),
    path('post_departments/', DepartmentAPIPost.as_view()),
    path('login/', LoginAPI.as_view()),
]
