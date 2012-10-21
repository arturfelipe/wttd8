# coding: utf-8
from django.test import TestCase
from eventex.core.models import Speaker

class SpeakerTest(TestCase):
    def setUp(self):
        self.speaker = Speaker(
            name='Artur Sousa',
            slug='artur-sousa',
            url='http://artursousa.com.br',
            description='Passionate software developer!'
        )
        self.speaker.save()

    def test_create(self):
        'Speaker must have name, slug, url and description.'
        self.assertEqual(1, self.speaker.pk)

    def test_unicode(self):
        'Speaker string repr should be its name.'
        self.assertEquals(u'Artur Sousa', unicode(self.speaker))
