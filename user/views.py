from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .serializers import *

class WXUserList(generics.ListCreateAPIView):
    queryset = WXUser.objects.all()
    serializer_class = WXUserSerializer

class WXUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WXUser.objects.all()
    serializer_class = WXUserSerializer

class TicketList(generics.ListAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        queryset = Ticket.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            user = get_object_or_404(WXUser, name=user)
            queryset = queryset.filter(user=user)
        return queryset

@csrf_exempt
def add_ticket(request):
    # print(request.POST)
    user = WXUser.objects.get(name=request.POST.get('user'))
    scene = Scene.objects.get(pk=request.POST.get('scene'))
    seats = request.POST.get('seats')
    seats = seats.split(',')
    i = 0
    while i < len(seats):
        instance = Ticket()
        instance.user = user
        instance.scene = scene
        instance.row = int(seats[i])
        instance.col = int(seats[i+1])
        instance.save()
        i += 2
    return JsonResponse({'error': '0'})
