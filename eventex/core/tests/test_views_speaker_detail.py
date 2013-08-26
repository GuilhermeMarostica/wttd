# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker

class SpeakerDetailTest(TestCase):
    def setUp(self):
        Speaker.objects.create(
            name='Guilherme Marostica',
            slug='guilherme-marostica',
            url= 'http://softsoftwares.com',
            description='Iniciante no mundo dos Softwares!')


        url = r('core:speaker_detail', kwargs={'slug': 'guilherme-marostica'})
        self.resp=self.client.get(url)

    def test_get(self):
        'GET should result in 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Template should be core/speaker_detail.html'
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        'Html must contain data.'
        self.assertContains(self.resp, 'Guilherme Marostica')
        self.assertContains(self.resp, 'Iniciante no mundo dos Softwares!')
        self.assertContains(self.resp, 'http://softsoftwares.com')

    def test_context(self):
        'Speaker must be in context.'
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)

class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        url = r('core:speaker_detail', kwargs={'slug': 'john-doe'})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)