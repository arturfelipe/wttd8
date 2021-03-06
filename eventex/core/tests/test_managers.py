# coding: utf-8
from django.test import TestCase
from eventex.core.models import Contact, Speaker, Talk

class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Artur Sousa', slug='artur-sousa',
                                   url='http://artursousa.com.br')
        s.contact_set.add(Contact(kind='E', value='artur@sousa.net'),
                          Contact(kind='P', value='21-95555595'),
                          Contact(kind='F', value='21-12345678'))

    def test_emails(self):
        'Contact must have emails manager.'
        qs = Contact.emails.all()
        expected = ['<Contact: artur@sousa.net>']
        self.assertQuerysetEqual(qs, expected)

    def test_phones(self):
        'Contact must have phones manager.'
        qs = Contact.phones.all()
        expected = ['<Contact: 21-95555595>']
        self.assertQuerysetEqual(qs, expected)

    def test_faxes(self):
        'Contact must have faxes managers.'
        qs = Contact.faxes.all()
        expected = ['<Contact: 21-12345678>']
        self.assertQuerysetEqual(qs, expected)

class PeriodManagerTest(TestCase):
    def setUp(self):
        Talk.objects.create(title='Morning Talk', start_time='10:00')
        Talk.objects.create(title='Afternoon Talk', start_time='12:00')

    def test_morning(self):
        'Should return all talks before 12:00.'
        self.assertQuerysetEqual(Talk.objects.at_morning(), ['Morning Talk'],
                                 lambda t: t.title)

    def test_afternoon(self):
        'Should return all talks from 12:00.'
        self.assertQuerysetEqual(Talk.objects.at_afternoon(), ['Afternoon Talk'],
                                 lambda t: t.title)
