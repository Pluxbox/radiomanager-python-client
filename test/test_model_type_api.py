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
from radiomanager_sdk.apis.model_type_api import ModelTypeApi


class TestModelTypeApi(unittest.TestCase):
    """ ModelTypeApi unit test stubs """

    def setUp(self):
        self.api = radiomanager_sdk.apis.model_type_api.ModelTypeApi()

    def tearDown(self):
        pass

    def test_get_model_type_by_id(self):
        """
        Test case for get_model_type_by_id

        Get modelType by id
        """
        pass

    def test_list_model_types(self):
        """
        Test case for list_model_types

        Get all modelTypes.
        """
        pass


if __name__ == '__main__':
    unittest.main()
