from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('data_analysis/', views.data_analysis, name='data_analysis'),
    url('about/', views.about, name='about'),
    url('admin/', admin.site.urls),
]
