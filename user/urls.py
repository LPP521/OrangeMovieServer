from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('users/', WXUserList.as_view()),
    path('users/<int:pk>/', WXUserDetail.as_view()),
    path('tickets/', TicketList.as_view()),
    path('tickets/add/', add_ticket),
]

urlpatterns = format_suffix_patterns(urlpatterns)