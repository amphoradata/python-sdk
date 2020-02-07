# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.7.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import amphora_client
from amphora_client.api.authentication_api import AuthenticationApi  # noqa: E501
from amphora_client.rest import ApiException


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self):
        self.api = amphora_client.api.authentication_api.AuthenticationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_authentication_request_token(self):
        """Test case for authentication_request_token

        Returns a JWT (JSON Web Token).               # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
