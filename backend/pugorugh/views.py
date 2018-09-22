from django.contrib.auth import get_user_model

from rest_framework import permissions
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

from .serializers import DogSerializer, UserSerializer, UserPrefSerializer, UserDogSerializer
from .models import Dog, UserPref, UserDog


class UserRegisterView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    model = get_user_model()
    serializer_class = UserSerializer

class UpdateDogStatusView(APIView):
    def get_object(self):
        return UserDog.objects.filter(
            user__id=self.request.user.id,
            dog__id=self.kwargs.get('pk')
        ).first()
    
    def put(self, request, pk, type):
        udog = self.get_object()
        udog.status = type[0].lower()
        udog.save()
        return Response(UserDogSerializer(udog).data)

class GetNextDogView(RetrieveAPIView):
    serializer_class = DogSerializer

    def get_queryset(self):
        user = self.request.user
        prefs = UserPref.objects.get(user=user)

        pref_dogs = Dog.objects.filter(
            gender__in=prefs.gender.split(','),
            size__in=prefs.size.split(','),
            age_classification__in=prefs.age.split(',')
        )
        
        rel_type = self.kwargs.get('type')
        return pref_dogs.filter(
            userdog__user__id=user.id,
            userdog__status=rel_type[0].lower()
        )
    
    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        
        dog = queryset.filter(id__gt=pk).first()

        if dog is None:
            if queryset.first() is None:
                raise Http404
            return queryset.first()
        return dog


class UserPrefUpdateView(APIView):
    serializer_class = UserPrefSerializer

    def get_object(self):
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