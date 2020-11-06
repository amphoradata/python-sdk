# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.26
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import unittest

import amphora_api_client
from amphora_api_client.api.users_api import UsersApi  # noqa: E501
from amphora_api_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""
    def setUp(self):
        self.api = amphora_api_client.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_users_create(self):
        """Test case for users_create

        Creates a new User. Returns the password.  # noqa: E501
        """
        pass

    def test_users_read_self(self):
        """Test case for users_read_self

        Gets logged in users information.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
