from django.test import TestCase
from django.http import HttpRequest
from django.http import HttpResponse
from django.utils.encoding import smart_text

from ..middleware.assets import AssetVersioningMiddleware
from .. import defaults as defs


class AssetTestCase(TestCase):
    """
    Testing if assets gets a version number.
    """
    def setUp(self):
        self.request = HttpRequest()
        self.response = HttpResponse()
        self.av = AssetVersioningMiddleware()

    def set_content(self, content):
        self.response.content = content
        self.response['Content-Length'] = len(self.response.content)
        self.response['Content-Type'] = 'text/html; charset=utf-8'

    def test_version_insertion(self):
        self.response.status_code == 200
        before = '<img src="example.com/img/logo.png" />'
        after = '<img src="example.com/img/logo.png?{}" />'.format(defs.FRESHLY_ASSETS_VERSION)
        self.set_content(before)
        resp = self.av.process_response(self.request, self.response)
        self.assertEquals(smart_text(resp.content), after)

    def test_version_insertion_all_extentions_img_tag(self):
        self.response.status_code == 200
        for ext in defs.FRESHLY_DEFAULT_ASSETS_EXTENTIONS:
            before = '<img src="example.com/img/logo.{}" />'.format(ext)
            after = '<img src="example.com/img/logo.{}?{}" />'.format(ext, defs.FRESHLY_ASSETS_VERSION)
            self.set_content(before)
            resp = self.av.process_response(self.request, self.response)
            self.assertEquals(smart_text(resp.content), after)

    def test_version_insertion_all_extentions_anchor_tag(self):
        self.response.status_code == 200
        for ext in defs.FRESHLY_DEFAULT_ASSETS_EXTENTIONS:
            before = '<a href="example.com/img/logo.{}">Logo</a>'.format(ext)
            after = '<a href="example.com/img/logo.{}?{}">Logo</a>'.format(ext, defs.FRESHLY_ASSETS_VERSION)
            self.set_content(before)
            resp = self.av.process_response(self.request, self.response)
            self.assertEquals(smart_text(resp.content), after)
