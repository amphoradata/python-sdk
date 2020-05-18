# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.1
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import unittest

import amphora_api_client
from amphora_api_client.api.version_api import VersionApi  # noqa: E501
from amphora_api_client.rest import ApiException


class TestVersionApi(unittest.TestCase):
    """VersionApi unit test stubs"""
    def setUp(self):
        self.api = amphora_api_client.api.version_api.VersionApi(
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_version_get_current_version(self):
        """Test case for version_get_current_version

        Get's the current server version.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
