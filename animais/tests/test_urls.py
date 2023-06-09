from urllib import response
from django.test import TestCase, RequestFactory
from django.urls import reverse
from animais.views import index

class AnimaisUrlsTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_rota_url_utiliza_view_index(self):
        """Teste se a home da aplicação a função index da view"""
        request = self.factory.get('/')

        with self.assertTemplateUsed('index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)