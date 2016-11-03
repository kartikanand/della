from django.conf.urls import url

from .views import MessageCreateView, ThreadDetailView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ThreadDetailView.as_view(), name='thread-detail'),
    url(r'^(?P<pk>\d+)/new/$', MessageCreateView.as_view(),
        name='new-message'),
]