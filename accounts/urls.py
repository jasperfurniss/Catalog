"""
Urls for accounts app
"""

from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('authtools.urls')),
]
