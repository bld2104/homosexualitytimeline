from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView, View
from django.urls import reverse_lazy
from maintimeline.models import Event

# Create your views here.

class HomePageView(ListView):
    model = Event
    template_name = 'maintimeline/index.html'
    queryset = Event.objects.all().order_by('date')

# class HomePageView(View):

#     def get(self, request, *args, **kwargs):
#         events = Event.objects.all().order_by('date')
#         # eventseven = Event.objects.all().order_by('date')[0::2]
#         # eventsodd = Event.objects.all().order_by('date')[1::2]
#         # {'eventsodd': eventsodd, 'eventseven': eventseven}
#         return render(request, 'maintimeline/index.html', {'events': events})
    
#     # def EveryOtherEventView(request):
#     #     eventseven = Event.objects.all().order_by('date')[0::2]
#     #     eventsodd = Event.objects.all().order_by('date')[1::2]
#     #     return render(request, 'maintimeline/index.html', {'eventseven': eventseven, 'eventsodd': eventsodd})

class ReferenceView(TemplateView):
    template_name = 'maintimeline/references.html'

class EventCreate(CreateView):
    model = Event
    fields = '__all__'
    exclude = ['created_by']

    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     return super().form_valid(form)

class EventUpdate(UpdateView):
    model = Event
    fields = '__all__'
    exclude = ['created_by']

class EventDelete(DeleteView):
    model = Event
    fields = '__all__'
    exclude = ['created_by']
    success_url = reverse_lazy('event-list')

# class ProfilePageView(TemplateView):
#     template_name = 'maintimeline/profile.html'


class EventDetailView(DetailView):
    model = Event
