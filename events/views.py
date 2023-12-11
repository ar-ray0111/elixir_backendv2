from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Events
from .serializers import EventSerializer

# Create your views here.
def index(request):
    return render(request, 'events/index.html')


@api_view(['GET'])
def get_events(request):
    events = Events.objects.all().order_by('-id')
    serializer = EventSerializer(events, many=True)

    return Response(serializer.data)
