# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.1.4
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import amphora_client
from amphora_client.api.search_api import SearchApi  # noqa: E501
from amphora_client.rest import ApiException


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self):
        self.api = amphora_client.api.search_api.SearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_search_search_amphorae(self):
        """Test case for search_search_amphorae

        Searches for Amphorae.  # noqa: E501
        """
        pass

    def test_search_search_amphorae_by_creator(self):
        """Test case for search_search_amphorae_by_creator

        Searches for Amphorae by creator.  # noqa: E501
        """
        pass

    def test_search_search_amphorae_by_location(self):
        """Test case for search_search_amphorae_by_location

        Searches for Amphorae by loction.  # noqa: E501
        """
        pass

    def test_search_search_amphorae_by_organisation(self):
        """Test case for search_search_amphorae_by_organisation

        Searches for Amphorae in an Organisation.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
