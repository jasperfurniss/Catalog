from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Create.as_view(), name='course'),
    url(r'^(?P<pk>[0-9]+)/$', views.Create.as_view(), name="course"),
    url(r'^list/$', views.CourseList.as_view(), name='course_list'),
    url(r'^list/detail/(?P<pk>[0-9]+)/$', views.CourseDetail.as_view(), name='course_detail'),
]