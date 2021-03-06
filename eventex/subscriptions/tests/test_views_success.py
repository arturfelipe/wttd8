# coding: utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.subscriptions.models import Subscription

class SuccessTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(name='Artur Sousa', cpf='12345678901',
                                        email='artur@sousa.net', phone='21-9555595')
        self.resp = self.client.get(r('subscriptions:success', args=[s.pk]))

    def test_get(self):
        'GET /inscricao/1/ should return status 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Uses template'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        'Context must have a subscription instance'
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        'Check if subscription data was rendered.'
        self.assertContains(self.resp, 'Artur Sousa')

class SuccessNotFound(TestCase):
    def test_not_found(self):
        'A subscription not found must return 404 status code'
        resp = self.client.get(r('subscriptions:success', args=[0]))
        self.assertEqual(404, resp.status_code)

