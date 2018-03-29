from django.test import TestCase
from django.http import HttpRequest
from quiz.views import success

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class AddQuizPageTest(TestCase):

    def test_uses_add_quiz_template(self):
        response = self.client.get('/addquiz/')
        self.assertTemplateUsed(response, 'addquiz.html')

    def test_add_success_page_can_save_post_requests(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['quiz'] = '1+1=2'
        request.POST['ans'] = 'True'

        response = success(request)
        self.assertIn('1+1=2', response.content.decode())
        self.assertIn('True', response.content.decode())
