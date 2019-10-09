# coding: utf-8

"""
    AmphoraApi

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.search_api import SearchApi  # noqa: E501
from openapi_client.rest import ApiException


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.search_api.SearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_search_amphorae_by_creator_get(self):
        """Test case for api_search_amphorae_by_creator_get

        Searches for Amphorae by creator.  # noqa: E501
        """
        pass

    def test_api_search_amphorae_by_location_get(self):
        """Test case for api_search_amphorae_by_location_get

        Searches for Amphorae by loction.  # noqa: E501
        """
        pass

    def test_api_search_amphorae_by_organisation_get(self):
        """Test case for api_search_amphorae_by_organisation_get

        Searches for Amphorae in an Organisation.  # noqa: E501
        """
        pass

    def test_api_search_amphorae_post(self):
        """Test case for api_search_amphorae_post

        Searches for Amphorae.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
