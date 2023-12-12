# atm/tests/test_views.py

import json
from django.test import TestCase
from django.urls import reverse
from .models import Project
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


class ProjectCRUDTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username="testuser", password="12345")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        self.project = Project.objects.create(
            name="Test Project",
            description="Test Description",
            start_date="2021-01-01",
            end_date="2021-12-31",
            owner=self.user,
        )
        self.list_create_url = reverse("project_list_create")
        self.detail_url = reverse("project_retrieve_update_delete", args=[self.project.id])

    def test_project_list(self):
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.project.name)

    def test_project_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.project.name)

    def test_project_create(self):
        response = self.client.post(
            self.list_create_url,
            json.dumps(
                {
                    "name": "New Project",
                    "description": "New Description",
                    "start_date": "2022-01-01",
                    "end_date": "2022-12-31",
                }
            ),
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Project.objects.count(), 2)
        self.assertEqual(Project.objects.last().name, "New Project")

    def test_project_update(self):
        response = self.client.put(
            self.detail_url,
            json.dumps(
                {
                    "name": "Updated Project",
                    "description": "Updated Description",
                    "start_date": "2021-01-01",
                    "end_date": "2021-12-31",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.project.refresh_from_db()
        self.assertEqual(self.project.name, "Updated Project")

    def test_project_delete(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Project.objects.count(), 0)


class ProjectAuthTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username="testuser", password="12345")
        self.project = Project.objects.create(
            name="Test Project",
            description="Test Description",
            start_date="2021-01-01",
            end_date="2021-12-31",
            owner=self.user,
        )
        self.list_create_url = reverse("project_list_create")
        self.detail_url = reverse("project_retrieve_update_delete", args=[self.project.id])

    def test_project_list_unauth(self):
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, 401)

    def test_project_detail_unauth(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 401)

    def test_project_create_unauth(self):
        response = self.client.post(
            self.list_create_url,
            {
                "name": "New Project",
                "description": "New Description",
                "start_date": "2022-01-01",
                "end_date": "2022-12-31",
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 401)

    def test_project_update_unauth(self):
        response = self.client.put(
            self.detail_url,
            json.dumps(
                {
                    "name": "Updated Project",
                    "description": "Updated Description",
                    "start_date": "2021-01-01",
                    "end_date": "2021-12-31",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 401)
        project = Project.objects.get(id=self.project.id)
        self.assertEqual(project.name, "Test Project")

    def test_project_delete_unauth(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(Project.objects.count(), 1)
