from django.test import TestCase, Client
from django.urls import reverse
from login_things.models import *
from login_things.views import *

class TestModels(TestCase):
    
    def test_login_user_GET(self):
        client = Client()
        response = client.get(reverse("login:login_user"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_login_register_GET(self):
        client = Client()
        response = client.get(reverse("login:register_user"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        self.assertTemplateUsed(response, 'base.html')
    
    def test_register_admin_GET(self):
        client = Client()
        response = client.get(reverse("login:register_admin"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register_admin.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_logout_GET(self):
        client = Client()
        response = client.get(reverse("login:logout"))

        self.assertEquals(response.status_code, 302) 

    def test_show_profile_GET(self):
        client = Client()
        response = client.get(reverse("login:show_profile", kwargs={'id': 0}))
        response = client.get(reverse("login:show_profile", kwargs={'id': 1}))
        response = client.get(reverse("login:show_profile", kwargs={'id': 2}))

        self.assertEquals(response.status_code, 302) 

    def test_get_json_GET(self):
        client = Client()
        response = client.get(reverse("login:get_json"))

        self.assertEquals(response.status_code, 302) 

    def test_get_dashboard_GET(self):
        client = Client()
        response = client.get(reverse("login:get_dashboard"))

        self.assertEquals(response.status_code, 302) 

    # def test_login_user_GET(self):
    #     client = Client()
    #     response = client.get(reverse("login:login_user"))

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'login.html')
    #     self.assertTemplateUsed(response, 'base.html')
    
    # def test_login_user_GET(self):
    #     client = Client()
    #     response = client.get(reverse("login:login_user"))

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'login.html')
    #     self.assertTemplateUsed(response, 'base.html')
    # def test_mywatchlist_json(self):
    #     client = Client()
    #     response = client.get(reverse("mywatchlist:show_json"))
    #     self.assertEquals(response.status_code, 200)

    # def test_mywatchlist_xml(self):
    #     client = Client()
    #     response = client.get(reverse("mywatchlist:show_xml"))
    #     self.assertEquals(response.status_code, 200)
