from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CourseList.as_view(), name='course_list'),
    url(r'^add/$', views.Create.as_view(), name='course'),
    url(r'^(?P<pk>[0-9]+)/$', views.Create.as_view(), name='course_edit'),
    url(r'^list/detail/(?P<slug>[\w\-]+)/$', views.CourseDetail.as_view(), name='course_detail'),
]