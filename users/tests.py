from django.test import TestCase
from models import User
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate 
from rest_framework.test import APIClient 
from rest_framework.test import APIRequestFactory 
from django.test.client import encode_multipart, RequestFactory

factory = RequestFactory()
data = {'title': 'remember to email dave'}
content = encode_multipart('BoUnDaRyStRiNg', data)
content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'
request = factory.put('/notes/547/', content, content_type=content_type)

client = APIClient()
client.login(username='admin', password='admin')

user = User.objects.get(username='')
request = factory.get('/accounts/django-superstars/')
force_authenticate(request, user=user, token=user.auth_token)
