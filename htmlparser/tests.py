from django.test import TestCase

from htmlparser.models import UrlProperties


class HtmlParserTestCase(TestCase):
    # def setUp(self):
    #     UrlProperties.objects.create(url="http:/google.com")
    #     UrlProperties.objects.create(url="http:/yahoo.com")

    def test_urls_exists(self):
        # url1 = UrlProperties.objects.get(url = "http:/google.com")
        # self.assertIsNotNone(url1)
        # url2 = UrlProperties.objects.get(url = "http:/yahoo.com")
        # self.assertIsNotNone(url2)
        self.assetIs(True)