import json
from django.conf import settings
from django.utils.six import BytesIO
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.parsers import JSONParser
from transformers_api.organization.models import Organization

class OrganizationTests(APITestCase):

    def setUp(self):
          user = User(**{
              'id': 1,
              'username': 'user',
              'first_name': 'user',
              'last_name': 'user',
              'email': 'user@test.com',
              'password': 'user',
              'is_superuser': True,
              'is_staff': True,
              'is_active': True
          })
          self.client.force_authenticate(user=user)

    def test_get_organizations(self):
        data = [{
          "name": "Test",
          "createUser": "user"
        }]

        post = self.client.post('/organizations/', data, format='json')
        response = self.client.get('/organizations/')

        self.assertEqual(post.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_organization(self):
        data = [{
          "name": "Test",
          "createUser": "user"
        }]

        post = self.client.post('/organizations/', data, format='json')
        response = self.client.get('/organizations/1/')

        self.assertEqual(post.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_organization_not_found(self):
        response = self.client.get('/organizations/1/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_organization(self):
        data = [{
          "name": "Test",
          "createUser": "user"
        }]

        response = self.client.post('/organizations/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_list_organization(self):
        data = [{
          "name": "Test",
          "createUser": "user"
        },{
          "name": "Test 2",
          "createUser": "user"
        }]

        response = self.client.post('/organizations/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_organization(self):
        data = [{
          "name": "Test",
          "createUser": "user"
        },{
          "name": "Test 2",
          "createUser": "user"
        }]

        post = self.client.post('/organizations/', data, format='json')
        delete = self.client.delete('/organizations/1/')

        self.assertEqual(post.status_code, status.HTTP_201_CREATED)
        self.assertEqual(delete.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_organization_not_found(self):
        delete = self.client.delete('/organizations/1/')

        self.assertEqual(delete.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_organization_invalid_pk(self):
        delete = self.client.delete('/organizations/')

        self.assertEqual(delete.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_organization(self):
        data = [{
          "name": "Test",
          "createUser": "user"
        }]

        data_update = {
            "name": "Test Update",
            "createUser": "user",
            "changeUser": "user"
        }

        post = self.client.post('/organizations/', data, format='json')
        update = self.client.put('/organizations/1/', data_update, format='json')

        self.assertEqual(post.status_code, status.HTTP_201_CREATED)
        self.assertEqual(update.status_code, status.HTTP_200_OK)

    def test_update_organization_not_found(self):
        data_update = {
            "name": "Test Update",
            "createUser": "user",
            "changeUser": "user"
        }

        update = self.client.put('/organizations/1/', data_update, format='json')

        self.assertEqual(update.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_organization_invalid_pk(self):
        data_update = {
            "name": "Test Update",
            "createUser": "user",
            "changeUser": "user"
        }

        update = self.client.put('/organizations/', data_update, format='json')

        self.assertEqual(update.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_organization_verify_fields(self):
        data = [{
          "name": "Test",
          "createUser": "user"
        }]

        post = self.client.post('/organizations/', data, format='json')
        response = self.client.get('/organizations/')

        stream = BytesIO(response.content)
        json = JSONParser().parse(stream)

        self.assertEqual(post.status_code, status.HTTP_201_CREATED)
        self.assertIn('meta', str(json))
        self.assertIn('records', str(json))
        self.assertIn('id', str(json))
        self.assertIn('name', str(json))
        self.assertIn('createUser', str(json))
        self.assertIn('changeUser', str(json))
        self.assertIn('changeDate', str(json))
