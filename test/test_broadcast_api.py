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
from radiomanager_sdk.apis.broadcast_api import BroadcastApi


class TestBroadcastApi(unittest.TestCase):
    """ BroadcastApi unit test stubs """

    def setUp(self):
        self.api = radiomanager_sdk.apis.broadcast_api.BroadcastApi()

    def tearDown(self):
        pass

    def test_create_broadcast(self):
        """
        Test case for create_broadcast

        Create broadcast.
        """
        pass

    def test_delete_broadcast_by_id(self):
        """
        Test case for delete_broadcast_by_id

        Delete broadcast by id
        """
        pass

    def test_get_broadcast_by_id(self):
        """
        Test case for get_broadcast_by_id

        Get broadcast by id
        """
        pass

    def test_get_current_broadcast(self):
        """
        Test case for get_current_broadcast

        Get current Broadcast
        """
        pass

    def test_get_daily_epg(self):
        """
        Test case for get_daily_epg

        Get daily EPG
        """
        pass

    def test_get_epg_by_date(self):
        """
        Test case for get_epg_by_date

        Get EPG by date
        """
        pass

    def test_get_next_broadcast(self):
        """
        Test case for get_next_broadcast

        Get next Broadcast
        """
        pass

    def test_get_weekly_epg(self):
        """
        Test case for get_weekly_epg

        Get weekly EPG
        """
        pass

    def test_list_broadcasts(self):
        """
        Test case for list_broadcasts

        Get all broadcasts.
        """
        pass

    def test_print_broadcast_by_id(self):
        """
        Test case for print_broadcast_by_id

        Print Broadcast by id
        """
        pass

    def test_update_broadcast_by_id(self):
        """
        Test case for update_broadcast_by_id

        Update broadcast by id
        """
        pass


if __name__ == '__main__':
    unittest.main()
