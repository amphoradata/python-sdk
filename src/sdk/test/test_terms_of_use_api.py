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
from amphora_api_client.api.terms_of_use_api import TermsOfUseApi  # noqa: E501
from amphora_api_client.rest import ApiException


class TestTermsOfUseApi(unittest.TestCase):
    """TermsOfUseApi unit test stubs"""
    def setUp(self):
        self.api = amphora_api_client.api.terms_of_use_api.TermsOfUseApi(
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_terms_of_use_accept(self):
        """Test case for terms_of_use_accept

        Accepts a Terms of Use.  # noqa: E501
        """
        pass

    def test_terms_of_use_create(self):
        """Test case for terms_of_use_create

        Creates a Terms of Use object.  # noqa: E501
        """
        pass

    def test_terms_of_use_delete(self):
        """Test case for terms_of_use_delete

        Deletes a Terms of Use object.  # noqa: E501
        """
        pass

    def test_terms_of_use_list(self):
        """Test case for terms_of_use_list

        Returns all Terms of Use.  # noqa: E501
        """
        pass

    def test_terms_of_use_read(self):
        """Test case for terms_of_use_read

        Returns all Terms of Use.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
