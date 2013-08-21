#coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription


class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Guilherme Marostica',
            cpf='12345678901',
            email='guilhermelotto@hotmail.com',
            phone='11-97320-7085'
        )

    def test_create(self):
        'Subscription must have name, cpf, email, phone'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Guilherme Marostica', unicode(self.obj))

    def test_paid_default_value_is_false(self):
        'By default paid must be False.'
        self.assertEqual(False, self.obj.paid)


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        # Create a first entry to force the colision
        Subscription.objects.create(name='Guilherme Marostica', cpf='12345678901', email='guilhermelotto@hotmail.com',
                                    phone='11 973207085')

    def test_cpf_unique(self):
        'CPF must be unique'
        s = Subscription(name='Guilherme Marostica', cpf='12345678901', email='outro@hotmail.com', phone='11 973207085')
        self.assertRaises(IntegrityError, s.save)


    def test_email_can_repeat(self):
        'Email is not unique anymore'
        s = Subscription.objects.create(name='Guilherme Marostica', email='guilherme@email.com',
                     cpf='32165498778', phone='11-973207085')
        self.assertEqual(2,s.pk)