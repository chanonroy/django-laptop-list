from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^laptops', views.Laptops.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
