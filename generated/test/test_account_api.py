# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import amphora_client
from amphora_client.api.account_api import AccountApi  # noqa: E501
from amphora_client.rest import ApiException


class TestAccountApi(unittest.TestCase):
    """AccountApi unit test stubs"""

    def setUp(self):
        self.api = amphora_client.api.account_api.AccountApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_account_get_account(self):
        """Test case for account_get_account

        Deletes an organisation.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
