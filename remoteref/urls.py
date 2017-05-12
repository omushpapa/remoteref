from django.conf.urls import url, include
from django.contrib import admin
from .views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^debt/', include('debtinfo.urls')),
    url(r'^$', home, name='home_page')
]
