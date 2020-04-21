# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.9.6
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import amphora_api_client
from amphora_api_client.api.organisations_api import OrganisationsApi  # noqa: E501
from amphora_api_client.rest import ApiException


class TestOrganisationsApi(unittest.TestCase):
    """OrganisationsApi unit test stubs"""

    def setUp(self):
        self.api = amphora_api_client.api.organisations_api.OrganisationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_account_get_plan(self):
        """Test case for account_get_plan

        Get's an Organisation's plan information.  # noqa: E501
        """
        pass

    def test_account_read(self):
        """Test case for account_read

        Get's an Organisation's account information.  # noqa: E501
        """
        pass

    def test_organisations_create(self):
        """Test case for organisations_create

        Creates a new Organisation. This will assign the logged in user to the organisation.  # noqa: E501
        """
        pass

    def test_organisations_delete(self):
        """Test case for organisations_delete

        Deletes an organisation.  # noqa: E501
        """
        pass

    def test_organisations_read(self):
        """Test case for organisations_read

        Gets an organisation's details.  # noqa: E501
        """
        pass

    def test_organisations_update(self):
        """Test case for organisations_update

        Updates an organisation.  # noqa: E501
        """
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
