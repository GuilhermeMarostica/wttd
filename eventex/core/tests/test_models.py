# coding: utf-8
from django.test import TestCase
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact

class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker(name='Guilherme Marostica',
                               slug='guilherme-marostica',
                               url='softsoftwares.com',
                               description='Iniciante no mundo dos Softwares!')
        self.speaker.save()

    def test_created(self):
        'Speaker instance should be saved.'
        self.assertEqual(1, self.speaker.pk)

    def test_unicode(self):
        'Speaker string representation should be the name.'
        self.assertEqual(u'Guilherme Marostica', unicode(self.speaker))

class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker=Speaker.objects.create(name='Guilherme Marostica',
                                            slug='guilherme-marostica', url='http://softsoftwares.com',
                                            description='Iniciantes no mundo dos Softwares!')

    def test_email(self):
        contact=Contact.objects.create(speaker=self.speaker, kind='E', value='guilherme@email.com',)
        self.assertEqual(1, contact.pk)

    def test_phone(self):
        contact=Contact.objects.create(speaker=self.speaker, kind='P', value='11-97320-7085')
        self.assertEqual(1, contact.pk)

    def test_fax(self):
        contact=Contact.objects.create(speaker=self.speaker, kind='F', value='11-4458-1313')
        self.assertEqual(1, contact.pk)

    def test_kind(self):
        'Contact kind should be limited to E, P or F.'
        contact=Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_unicode(self):
        'Contact string representation should be value'
        contact = Contact(speaker=self.speaker, kind='E',
                          value='guilherme@email.com')
        self.assertEqual(u'guilherme@email.com', unicode(contact))