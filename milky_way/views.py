from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Star
from .serializers import StarSerializer, StarSerializerOther
# Create your views here.

class MilkyStar(RetrieveUpdateDestroyAPIView):
    queryset = Star.objects.all()
    serializer_class = StarSerializer


class MilkyStarOther(ListCreateAPIView):
    queryset = Star.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return StarSerializer
        return StarSerializerOther

