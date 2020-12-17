from django.urls import path
from . import views

urlpatterns = [
    path('upcoming-meetings/', views.UpcomingMeetingsListView.as_view(), name='upcoming_meetings'),
    path('past-meetings/', views.PastMeetingsListView.as_view(), name='past_meetings'),
]