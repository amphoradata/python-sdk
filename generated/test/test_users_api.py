# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.6.3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import amphora_client
from amphora_client.api.users_api import UsersApi  # noqa: E501
from amphora_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = amphora_client.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_users_create(self):
        """Test case for users_create

        Creates a new User. Returns the password.  # noqa: E501
        """
        pass

    def test_users_read_self(self):
        """Test case for users_read_self

        Get's logged in users information.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
