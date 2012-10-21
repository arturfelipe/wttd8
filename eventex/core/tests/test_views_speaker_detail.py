# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker

class SpeakerDetailTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Artur Sousa',
            slug='artur-sousa',
            url='http://artursousa.com.br',
            description='Passionate software developer!')

        url = r('core:speaker_detail', kwargs={'slug': s.slug})
        self.resp = self.client.get(url)

    def test_get(self):
        'GET must return 200 status code.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Template shoud be core/speaker_detail.html.'
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        'Html must contain data.'
        self.assertContains(self.resp, 'Artur Sousa')
        self.assertContains(self.resp, 'Passionate software developer!')
        self.assertContains(self.resp, 'http://artursousa.com.br')

    def test_context(self):
        'Speaker must be in the context.'
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)

class SpeakerDatailNotFound(TestCase):
    def test_not_found(self):
        'Speaker was not found.'
        url = r('core:speaker_detail', kwargs={'slug': 'henrique-bastos'})
        resp = self.client.get(url)
        self.assertEqual(404, resp.status_code)
