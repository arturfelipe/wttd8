# coding: utf-8
from django.test import TestCase
from eventex.core.models import Talk, Media

class MediaModelTest(TestCase):
    def setUp(self):
        t = Talk.objects.create(title='Talk', start_time='10:00')
        self.media = Media.objects.create(talk=t, kind='YT',
            media_id='QjA5faZF1A8', title='Video')

    def test_create(self):
        'Media must have kind, media_id, title and refer to a talk.'
        self.assertEqual(1, self.media.pk)

    def test_unicode(self):
        'Media must have Talk.title - Media.title as repr.'
        self.assertEqual(u'Talk - Video', unicode(self.media))
