from django.test import TestCase

from BTdUbs.models import Store 
# Create your tests here.

class StoreTestCase(TestCase):
    def setup(self):
        Store.objects.create( store_name="another store", url="www.anotherstore.com")

    def test_unicode(self):
        expected = "a store"
        s1 = Store(store_name=expected)
        self.assertEqual(expected, s1.store_name)

    def test_url_return(self):
        expected = "http://www.astore.com"
        s1=Store(store_name="a store", url=expected)
        self.assertEqual(s1.url, expected)
