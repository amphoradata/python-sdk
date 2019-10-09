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
from openapi_client.api.organisations_api import OrganisationsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestOrganisationsApi(unittest.TestCase):
    """OrganisationsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.organisations_api.OrganisationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_organisations_id_delete(self):
        """Test case for api_organisations_id_delete

        Deletes an organisation.  # noqa: E501
        """
        pass

    def test_api_organisations_id_get(self):
        """Test case for api_organisations_id_get

        Gets an organisation's details.  # noqa: E501
        """
        pass

    def test_api_organisations_id_invitations_get(self):
        """Test case for api_organisations_id_invitations_get

        Accept an invitation to an organisation.  # noqa: E501
        """
        pass

    def test_api_organisations_id_invitations_post(self):
        """Test case for api_organisations_id_invitations_post

        Invite a user/ email address to your organisation.  # noqa: E501
        """
        pass

    def test_api_organisations_id_put(self):
        """Test case for api_organisations_id_put

        Updates an organisation.  # noqa: E501
        """
        pass

    def test_api_organisations_post(self):
        """Test case for api_organisations_post

        Creates a new Organisation. This will assign the logged in user to the organisation.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
