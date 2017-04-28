from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/(?P<pk>[0-9]+)/$', views.add_task_to_basket, name='add_task'),
    url(r'^remove/(?P<pk>[0-9]+)/$', views.remove_task_from_basket, name='remove_task'),
]