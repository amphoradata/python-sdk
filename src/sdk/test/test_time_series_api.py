# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.29
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import unittest

import amphora_api_client
from amphora_api_client.api.time_series_api import TimeSeriesApi  # noqa: E501
from amphora_api_client.rest import ApiException


class TestTimeSeriesApi(unittest.TestCase):
    """TimeSeriesApi unit test stubs"""
    def setUp(self):
        self.api = amphora_api_client.api.time_series_api.TimeSeriesApi(
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_time_series_query_time_series(self):
        """Test case for time_series_query_time_series

        Updates the details of an Amphora by Id.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
