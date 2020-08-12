# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.16
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import unittest

import amphora_api_client
from amphora_api_client.api.permission_api import PermissionApi  # noqa: E501
from amphora_api_client.rest import ApiException


class TestPermissionApi(unittest.TestCase):
    """PermissionApi unit test stubs"""
    def setUp(self):
        self.api = amphora_api_client.api.permission_api.PermissionApi(
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_permission_get_permissions(self):
        """Test case for permission_get_permissions

        The permission level for each object id in the request.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
