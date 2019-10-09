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
from openapi_client.api.users_api import UsersApi  # noqa: E501
from openapi_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_users_post(self):
        """Test case for api_users_post

        Creates a new User. Returns the password.  # noqa: E501
        """
        pass

    def test_api_users_self_get(self):
        """Test case for api_users_self_get

        Get's logged in users information.  # noqa: E501
        """
        pass

    def test_api_users_username_delete(self):
        """Test case for api_users_username_delete

        Deletes a user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
