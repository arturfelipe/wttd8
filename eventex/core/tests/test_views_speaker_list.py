# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker

class SpeakerListTest(TestCase):
    def setUp(self):
        s1 = Speaker.objects.create(name='Henrique Bastos', slug='henrique-bastos')
        s2 = Speaker.objects.create(name='Artur Sousa', slug='artur-sousa')
        self.resp = self.client.get(r('core:speaker_list'))

    def test_get(self):
        'GET must return 200 status code'
        self.assertTrue(200, self.resp.status_code)

    def test_template(self):
        'Template core/speaker_list.html'
        self.assertTemplateUsed(self.resp, 'core/speaker_list.html')

    def test_html(self):
        'HTML must contain speakers name and absolute url.'
        self.assertContains(self.resp, 'Artur Sousa')
        self.assertContains(self.resp, '/palestrantes/artur-sousa')
        self.assertContains(self.resp, 'Henrique Bastos')
        self.assertContains(self.resp, '/palestrantes/henrique-bastos')

    def test_spearks_in_context(self):
        'Speakers must be in context.'
        speakers = self.resp.context['speakers']
        self.assertQuerysetEqual(speakers, ['Artur Sousa', 'Henrique Bastos'],
                                lambda s: s.name)
