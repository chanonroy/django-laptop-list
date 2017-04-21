from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/laptops')),
    url(r'^laptops/', include('laptops.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', admin.site.urls),
]
