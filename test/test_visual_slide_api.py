# coding: utf-8

"""
    RadioManager

    RadioManager

    OpenAPI spec version: 2.0
    Contact: support@pluxbox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import radiomanager_sdk
from radiomanager_sdk.rest import ApiException
from radiomanager_sdk.apis.visual_slide_api import VisualSlideApi


class TestVisualSlideApi(unittest.TestCase):
    """ VisualSlideApi unit test stubs """

    def setUp(self):
        self.api = radiomanager_sdk.apis.visual_slide_api.VisualSlideApi()

    def tearDown(self):
        pass

    def test_get_visual_slide(self):
        """
        Test case for get_visual_slide

        Get Visual Slide Image as Base64
        """
        pass


if __name__ == '__main__':
    unittest.main()
