# coding: utf-8

"""
    RadioManager

    RadioManager  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: support@pluxbox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import radiomanager_sdk
from radiomanager_sdk.api.model_type_api import ModelTypeApi  # noqa: E501
from radiomanager_sdk.rest import ApiException


class TestModelTypeApi(unittest.TestCase):
    """ModelTypeApi unit test stubs"""

    def setUp(self):
        self.api = radiomanager_sdk.api.model_type_api.ModelTypeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_model_type_by_id(self):
        """Test case for get_model_type_by_id

        Get modelType by id  # noqa: E501
        """
        pass

    def test_list_model_types(self):
        """Test case for list_model_types

        Get all modelTypes.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
