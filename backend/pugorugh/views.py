from django.contrib.auth import get_user_model

from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import DogSerializer, UserSerializer, UserPrefSerializer
from .models import Dog, UserPref, UserDog


class UserRegisterView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    model = get_user_model()
    serializer_class = UserSerializer

class UserPrefUpdateView(APIView):
    serializer_class = UserPrefSerializer

    def get_object(self):
        print(self.request.data)
        return UserPref.objects.filter(user__id__exact=self.request.user.id).first()

    def get(self, request):
        user = self.get_object()
        serializer = UserPrefSerializer(user)
        return Response(serializer.data)
    
    def put(self, request):
        user = self.get_object()
        serializer = UserPrefSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)