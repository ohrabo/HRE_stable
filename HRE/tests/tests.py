from django.core import mail
from django.test import TestCase
from django.urls import reverse


from edu.models import Subject
from library.models import Text
from students.forms import CourseEnrollForm


class TestModelTest(TestCase):
    def test_string_representation(self):
        text = Text(title="My article title")
        subject = Subject(title='My subject title')
        self.assertEqual(str(text), text.title)
        self.assertEqual(str(subject), subject.title)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Text._meta.verbose_name_plural), "Texts")


class ProjectTests(TestCase):
    def test_homepage(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code, 200)

class EmailTest(TestCase):
    def test_text_share(self):
        mail.send_mail(
            'Subject here', 'Here is the message',
            'from@example.com', ['to@example.com'],
            fail_silently=False,
        )

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')


class TextListViewTest(TestCase):
    def setUp(self):
        Text.objects.create(body='just a test', category_id=1)

    def test_text_content(self):
            text = Text.objects.get(id=1)
            expected_object_name = f'{text.body}'
            self.assertEquals(expected_object_name, 'just a test')

def test_text_list_view(self):
    response = self.client.get('text_list')
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'just a test')
    self.assertTemplateUsed(response, 'list.html')



def test_paginator(self):
    for i in range(15):
        Text.objects.create(title="title", body="just a test", category_id=1)

    #access first page
    response = self.c.get(reverse('text_list', args=[1,]))
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.context['text']), 3)

    #access second page
    response = self.c.get(reverse('text_list', args=[2,]))
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.context['text']), 3)


class TestRegistrationForm(TestCase):

    def test_registration_form(self):
        # test invalid data
        invalid_data = {
            "username": "user@test.com",
            "password": "secret",
            "confirm": "not secret"
        }
        form = CourseEnrollForm(data=invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)

