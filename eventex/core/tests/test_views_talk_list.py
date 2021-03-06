# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Talk, Speaker

class TalkListTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Artur Sousa', slug='artur-sousa',
            url='http://artursousa.com.br', description='Passionate software developer!')
        t1 = Talk.objects.create(title=u'Título da palestra',
            description=u'Descrição da palestra', start_time='10:00')
        t2 = Talk.objects.create(title=u'Título da palestra',
            description=u'Descrição da palestra', start_time='10:00')
        t1.speakers.add(s)
        t2.speakers.add(s)
        self.resp = self.client.get(r('core:talk_list'))

    def test_get(self):
        'GET must return 200 status code.'
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        'View must use template core/talk_list.html'
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        'Html should list talks.'
        self.assertContains(self.resp, u'Título da palestra', 2)
        self.assertContains(self.resp, u'/palestras/1/')
        self.assertContains(self.resp, u'/palestras/2/')
        self.assertContains(self.resp, u'/palestrantes/artur-sousa/', 2)
        self.assertContains(self.resp, u'Passionate software developer!', 2)
        self.assertContains(self.resp, u'Artur Sousa', 2)
        self.assertContains(self.resp, u'Descrição da palestra', 2)

    def test_morning_talks_in_context(self):
        'Morning talks should appear separated in the context.'
        self.assertIn('morning_talks', self.resp.context)

    def test_afternoon_talks_in_context(self):
        'Afternoon talks should appear separated in the context.'
        self.assertIn('afternoon_talks', self.resp.context)
