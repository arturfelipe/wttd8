# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Talk

class TalkDetailTest(TestCase):
    def setUp(self):
        t = Talk.objects.create(title='Talk', start_time='10:00')
        t.speakers.create(name='Artur Sousa', slug='artur-sousa',
                                  url='http://artursousa.com.br')
        self.resp = self.client.get(r('core:talk_detail', args=[1]))

    def test_get(self):
        'GET must return a 200 status code.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Template core/talk_detail.html must be used.'
        self.assertTemplateUsed(self.resp, 'core/talk_detail.html')

    def test_talk_in_context(self):
        'Talk must be in context.'
        talk = self.resp.context['talk']
        self.assertIsInstance(talk, Talk)

    def test_not_found(self):
        'Talk was not found.'
        resp = self.client.get(r('core:talk_detail', args=[0]))
        self.assertEqual(404, resp.status_code)

    def test_html(self):
        'Html must show talk data.'
        self.assertContains(self.resp, 'Talk')
        self.assertContains(self.resp, '/palestrantes/artur-sousa/')
        self.assertContains(self.resp, 'Artur Sousa')
