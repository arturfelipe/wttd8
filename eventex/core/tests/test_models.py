# coding: utf-8
from django.test import TestCase
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact

class SpeakerModelTest(TestCase):
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

class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Artur Sousa',
            slug='artur-sousa',
            url='http://artursousa.com.br',
            description='Passionate software developer!'
        )

    def test_email(self):
        'Contact email could be added to a speaker.'
        contact = Contact.objects.create(speaker=self.speaker, kind='E',
                                        value='artur@sousa.net')
        self.assertEqual(1, contact.pk)

    def test_phone(self):
        'Contact phone could be added to a speaker.'
        contact = Contact.objects.create(speaker=self.speaker, kind='P',
                                         value='21-95555595')
        self.assertEqual(1, contact.pk)

    def test_fax(self):
        'Contact fax could be added to a speaker.'
        contact = Contact.objects.create(speaker=self.speaker, kind='F',
                                         value='21-12345678')
        self.assertEqual(1, contact.pk)

    def test_kind(self):
        'Kind must be E, P or F.'
        contact = Contact(speaker=self.speaker, kind='J', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_unicode(self):
        'Contact repr must be the value.'
        contact = Contact.objects.create(speaker=self.speaker, kind='E',
                                         value='artur@sousa.net')
        self.assertEqual(u'artur@sousa.net', unicode(contact))
