from django.shortcuts import render
from django.http import HttpResponse, response
from rest_framework import generics, viewsets, permissions
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.response import Response
from .models import MenuItem, Booking

# Create your views here.
def sayHello(request):
    return HttpResponse("Hello World!")

def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
