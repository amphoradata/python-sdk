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
from amphora_api_client.api.feeds_api import FeedsApi  # noqa: E501
from amphora_api_client.rest import ApiException


class TestFeedsApi(unittest.TestCase):
    """FeedsApi unit test stubs"""
    def setUp(self):
        self.api = amphora_api_client.api.feeds_api.FeedsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_feed_get_feed(self):
        """Test case for feed_get_feed

        Gets the feed for the logged in user.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
