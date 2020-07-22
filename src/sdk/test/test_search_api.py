# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.11
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import unittest

import amphora_api_client
from amphora_api_client.api.search_api import SearchApi  # noqa: E501
from amphora_api_client.rest import ApiException


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""
    def setUp(self):
        self.api = amphora_api_client.api.search_api.SearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_search_search_amphorae(self):
        """Test case for search_search_amphorae

        Searches for Amphorae.  # noqa: E501
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

    def test_search_search_organisations(self):
        """Test case for search_search_organisations

        Searches for Organisations with fuzzy search.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
