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
from radiomanager_sdk.apis.block_api import BlockApi


class TestBlockApi(unittest.TestCase):
    """ BlockApi unit test stubs """

    def setUp(self):
        self.api = radiomanager_sdk.apis.block_api.BlockApi()

    def tearDown(self):
        pass

    def test_get_block_by_id(self):
        """
        Test case for get_block_by_id

        Get block by id
        """
        pass

    def test_get_current_block(self):
        """
        Test case for get_current_block

        Get current Block
        """
        pass

    def test_get_next_block(self):
        """
        Test case for get_next_block

        Get upcoming Block
        """
        pass

    def test_list_blocks(self):
        """
        Test case for list_blocks

        Get a list of all blocks currently in your station.
        """
        pass


if __name__ == '__main__':
    unittest.main()
