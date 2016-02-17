from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Create.as_view(), name='course'),
]