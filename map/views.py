import json
from django.shortcuts import render
from map.models import Marker

def map(request):
    markers_list=Marker.objects.all().values_list('lat', 'lon', 'description', 'category')
    markers = json.dumps(list(markers_list))
    return render(request, 'map/hrmap.html', {'markers': markers}

                  )