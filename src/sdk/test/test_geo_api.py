# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.28
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import unittest

import amphora_api_client
from amphora_api_client.api.geo_api import GeoApi  # noqa: E501
from amphora_api_client.rest import ApiException


class TestGeoApi(unittest.TestCase):
    """GeoApi unit test stubs"""
    def setUp(self):
        self.api = amphora_api_client.api.geo_api.GeoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_geo_lookup_location(self):
        """Test case for geo_lookup_location

        Executes a fuzzy location search.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
