# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
class SimpleTest(TestCase):
    def test_details(self):
        response = self.client.get('/V1/applast/')
        self.assertEqual(response.status_code, 200)

    # def test_index(self):
    #     response = self.client.get('/V1/firmwarelast/')
    #     self.assertEqual(response.status_code, 200)s