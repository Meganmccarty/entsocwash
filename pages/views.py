from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from .models import Meeting
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class UpcomingMeetingsListView(generic.ListView):
    model = Meeting
    template_name = 'pages/upcoming_meetings.html'

    def get_context_data(self, **kwargs):
        context = super(UpcomingMeetingsListView, self).get_context_data(**kwargs)
        context['upcoming_meetings'] = Meeting.objects.filter(date__gte=timezone.now()).order_by('-date')
        return context

class PastMeetingsListView(generic.ListView):
    model = Meeting
    template_name = 'pages/past_meetings.html'

    def get_context_data(self, **kwargs):
        context = super(PastMeetingsListView, self).get_context_data(**kwargs)
        context['past_meetings'] = Meeting.objects.filter(date__lte=timezone.now()).order_by('-date')
        return context