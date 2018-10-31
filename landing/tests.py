from django.test import TestCase
from django.urls import reverse
# Create your tests here.

from landing.models import Subscriber

class SubscriberModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Subscriber.objects.create(name='Big', email='ti@i.ua')

    def test_name_label(self):
        subscriber = Subscriber.objects.get(id=1)
        field_label = subscriber._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        subscriber = Subscriber.objects.get(id=1)
        max_length = subscriber._meta.get_field('name').max_length
        self.assertEquals(max_length, 128)

    def test_email_label(self):
        subscriber = Subscriber.objects.get(id=1)
        field_label = subscriber._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_email_max_length(self):
        subscriber = Subscriber.objects.get(id=1)
        max_length = subscriber._meta.get_field('email').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_email_and_name(self):
        subscriber = Subscriber.objects.get(id=1)
        expected_object_name = '%s %s' % (subscriber.email, subscriber.name)
        self.assertEquals(expected_object_name, str(subscriber))





class SubscribersListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_subs = 13
        for subs_num in range(number_of_subs):
            Subscriber.objects.create(name='Christian %s' % subs_num, email='urname@i.ua %s' % subs_num, )



    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/landing/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('landing'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('landing'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'landing/landing.html')




