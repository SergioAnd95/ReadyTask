from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.TaskListView.as_view(), name='tasks_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.TaskDetailView.as_view(), name='task_detail'),
]