from django.urls import path, include
from maintimeline.views import EventCreate, EventUpdate, EventDelete, EventDetailView
from . import views

urlpatterns = [
    # ...
    path('maintimeline/add/', EventCreate.as_view(), name='event-add'),
    path('maintimeline/<int:pk>/update', EventUpdate.as_view(), name='event-update'),
    path('maintimeline/<int:pk>/delete/', EventDelete.as_view(), name='event-delete'),
    path('', views.HomePageView.as_view(), name='home'),
    path('infinite', views.TestView.as_view(), name='test'),
    path('graham', views.GrahamView.as_view(), name='graham'),
    path('references', views.ReferenceView.as_view(), name='references'),
    # path('accounts/profile/', views.ProfilePageView.as_view(), name='user_profile'),
    path('maintimeline/<int:pk>', EventDetailView.as_view(), name='event-detail'),
]