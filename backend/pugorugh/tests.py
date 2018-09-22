from django.test import TestCase
from rest_framework import status
from rest_framework.test import (APIRequestFactory, APITestCase,
                                 force_authenticate)

from .models import *
from .views import *

class APITest(APITestCase):
    """Tests the API and classes"""
    def setUp(self):
        """Setup testing environment"""
        # Create temp dog
        self.dog = Dog.objects.create(
            name='Shadow',
            image_filename='img1',
            breed='Labradoodle',
            age=15,
            gender='f',
            size='m'
        )
        # Create temp user
        self.user = User.objects.create(username='unittest')
        # Create class wide request factory
        self.factory = APIRequestFactory()
    
    def test_user_prefs_update(self):
        """Test getting and updating UserPrefs"""
        view = UserPrefUpdateView.as_view()
        request = self.factory.get('update-prefs')
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, 200)
        request = self.factory.put('update-prefs', data=dict(
            age='b,a,s',
            gender='m',
            size='l,xl'
        ))
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, 200)
    
    def test_user_dog_like(self):
        """Test liking a dog"""
        view = UpdateDogStatusView.as_view()
        request = self.factory.put('update-dog')
        force_authenticate(request, user=self.user)
        response = view(request, pk=self.dog.pk, type='liked')
        self.assertEqual(response.status_code, 200)
        udog = UserDog.objects.filter(
            user__id=self.user.id,
            dog__id=self.dog.id
        ).first()
        self.assertEqual(udog.status, 'l')
    
    def test_user_dog_dislike(self):
        """Test disliking a dog"""
        view = UpdateDogStatusView.as_view()
        request = self.factory.put('update-dog')
        force_authenticate(request, user=self.user)
        response = view(request, pk=self.dog.pk, type='disliked')
        self.assertEqual(response.status_code, 200)
        udog = UserDog.objects.filter(
            user__id=self.user.id,
            dog__id=self.dog.id
        ).first()
        self.assertEqual(udog.status, 'd')
    
    def test_next_dog_view(self):
        """Test viewing the next dog in the system"""
        view = GetNextDogView.as_view()
        request = self.factory.get('next-dog')
        force_authenticate(request, self.user)
        response = view(request, pk=-1, type='undecided')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], self.dog.name)