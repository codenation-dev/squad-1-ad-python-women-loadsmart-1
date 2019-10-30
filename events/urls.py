from django.urls import include, path, re_path
from rest_framework import routers
from events import views
from events.views import EventsListView, EventFilter, EventDetail, EditEventApiView

router = routers.DefaultRouter()
router.register(r'events', views.EventAPIViewSet)
router.register(r'agents', views.AgentAPIViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', EventFilter.as_view(), name='events-list'),
    path('<int:event_id>', EventDetail.as_view(), name='detail'),
    re_path(r'(?P<pk>\d+)/edit', EditEventApiView.as_view(), name='edit')
]