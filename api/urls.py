from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^all/', views.LaptopsAll.as_view()),
    url(r'^filter$', views.LaptopsFilter.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
