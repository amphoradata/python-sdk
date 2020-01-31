# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.6.6
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import amphora_client
from amphora_client.api.terms_and_conditions_api import TermsAndConditionsApi  # noqa: E501
from amphora_client.rest import ApiException


class TestTermsAndConditionsApi(unittest.TestCase):
    """TermsAndConditionsApi unit test stubs"""

    def setUp(self):
        self.api = amphora_client.api.terms_and_conditions_api.TermsAndConditionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_terms_and_conditions_create(self):
        """Test case for terms_and_conditions_create

        Adds new Terms and Conditions to your Organisations T/C Library.  # noqa: E501
        """
        pass

    def test_terms_and_conditions_read(self):
        """Test case for terms_and_conditions_read

        Get's a list of an Organisation's Terms and Conditions.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
