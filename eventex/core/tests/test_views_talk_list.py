# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r

class TalkListViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:talk_list'))

    def test_get(self):
        'GET must return 200 status code.'
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        'View must use template core/talk_list.html'
        self.asserTemplateUsed(self.resp, 'core/talk_list.html')
