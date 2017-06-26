from django.test import TestCase
from su.models import Uploader

# Create your tests here.

class UploaderTestCase(TestCase):
    """
    Simple testcase to check if the models work as expected
    """
    def setUp(self):
        Uploader.objects.create(FILENAME="tmp.txt", FILE="1234", EMAIL="tmp@gmail.com", PHONE="1234567890")

    def test_create(self):
        Uploader.objects.create(FILENAME="tmp2.txt", FILE="12345", EMAIL="tmp2@gmail.com", PHONE="1234567891")
        record = Uploader.objects.get(FILENAME="tmp2.txt")
        self.assertEqual(record.FILENAME, "tmp2.txt")
        self.assertEqual(record.FILE, "12345")
        self.assertEqual(record.EMAIL, "tmp2@gmail.com")
        self.assertEqual(record.PHONE, "1234567891")
        record.delete()

    def test_select(self):
        record = Uploader.objects.get(FILENAME="tmp.txt")
        self.assertEqual(record.FILENAME, "tmp.txt")
        self.assertEqual(record.FILE, "1234")
        self.assertEqual(record.EMAIL, "tmp@gmail.com")
        self.assertEqual(record.PHONE, "1234567890")

    def tearDown(self):
        record = Uploader.objects.get(FILENAME="tmp.txt")
        record.delete()

