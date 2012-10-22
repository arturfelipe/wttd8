# coding: utf-8
from django.test import TestCase
from eventex.core.models import Talk, Course
from eventex.core.managers import PeriodManager

class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title=u'Introdução ao Django',
            description=u'Descrição da palestra.',
            start_time='10:00')

    def test_create(self):
        'Talk must have title, description and start_time.'
        self.assertEqual(1, self.talk.pk)

    def test_unicode(self):
        'Talk must have title as repr.'
        self.assertEqual(u'Introdução ao Django', unicode(self.talk))

    def test_speakers(self):
        'Talk has many speakers and vice-versa.'
        self.talk.speakers.create(name='Artur Sousa', slug='artur-sousa',
                                     url='http://artursousa.com.br')
        self.assertEqual(1, self.talk.speakers.count())

    def test_period_manager(self):
        'Talk default manager must be an instance of PeriodManager.'
        self.assertIsInstance(Talk.objects, PeriodManager)

class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(title=u'Tutorial Django',
            description=u'Descrição do curso.', start_time='10:00', slots=20)

    def test_create(self):
        'Course must have title, description, start_time and slots.'
        self.assertEquals(1, self.course.id)

    def test_unicode(self):
        'Course must have title as repr.'
        self.assertEquals(u'Tutorial Django', unicode(self.course))

    def test_speakers(self):
        'Course can have many speakers and vice-versa.'
        self.course.speakers.create(name='Artur Sousa', slug='artur-sousa',
                                     url='http://artursousa.com.br')
        self.assertEquals(1, self.course.speakers.count())

    def test_period_manager(self):
        'Course default manager must be an instance of PeriodManager'
        self.assertIsInstance(Course.objects, PeriodManager)
