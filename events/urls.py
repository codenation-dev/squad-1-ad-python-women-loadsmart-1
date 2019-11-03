from django.urls import include, path, re_path
from rest_framework import routers
from events import views
from events.views import (
    EventsListView,
    EventFilter, 
    EventDetail, 
    ArchievedEventApiView, 
    UnarchivedEventApiView,
    DeleteEventApiView
)

router = routers.DefaultRouter()
router.register(r'events', views.EventAPIViewSet)
router.register(r'agents', views.AgentAPIViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', EventFilter.as_view(), name='events-list'),
    path('<int:event_id>', EventDetail.as_view(), name='detail'),
    re_path(r'(?P<pk>\d+)/archived', ArchievedEventApiView.as_view(), name='archived'),
    re_path(r'(?P<pk>\d+)/unarchived', UnarchivedEventApiView.as_view(), name='unarchived'),
    re_path(r'(?P<pk>\d+)/delete', DeleteEventApiView.as_view(), name='delete')
]