from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView, ListAPIView
from rest_framework.views import APIView
from .models import Star
from .serializers import StarSerializer, StarSerializerOther, Seria, ChangePassSeria, StarAll
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrAdmin
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class MilkyStar(RetrieveUpdateDestroyAPIView):
    queryset = Star.objects.all()
    serializer_class = StarAll
    permission_classes = [IsOwnerOrAdmin]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views_count += 1
        instance.save(update_fields=['views_count'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class MilkyStarOther(ListCreateAPIView):
    queryset = Star.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return StarSerializer
        return StarSerializerOther

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, views_count=0)


class RegisterView(CreateAPIView):
    serializer_class = Seria
    queryset = User.objects.all()


class ProfileView(ListAPIView):
    serializer_class = Seria
    
    def get_queryset(self):
        return User.objects.filter(username=self.request.user)

    def list(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'login error!':'You are not logged in!'})
        return super().list(request, *args, **kwargs)

class ChangePassView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=ChangePassSeria,
        responses={200: openapi.Response('Password updated')}
    )

    def post(self, request):
        serializer = ChangePassSeria(data=request.data)
        user = request.user

        if serializer.is_valid():
            print(serializer.validated_data)
            if user.check_password(serializer.validated_data['old_pass']):
                return Response({'old_password':'wrong!'})

            user.set_password(serializer.validated_data['old_pass'])
            user.save()
            return Response({'Congratulations!':'The password is changed'})
        return Response(serializer.errors)

