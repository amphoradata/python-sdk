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
from amphora_api_client.api.identity_api import IdentityApi  # noqa: E501
from amphora_api_client.rest import ApiException


class TestIdentityApi(unittest.TestCase):
    """IdentityApi unit test stubs"""
    def setUp(self):
        self.api = amphora_api_client.api.identity_api.IdentityApi(
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_identity_get(self):
        """Test case for identity_get

        """
        pass


if __name__ == '__main__':
    unittest.main()
