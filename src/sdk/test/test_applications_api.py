# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.6
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import unittest

import amphora_api_client
from amphora_api_client.api.applications_api import ApplicationsApi  # noqa: E501
from amphora_api_client.rest import ApiException


class TestApplicationsApi(unittest.TestCase):
    """ApplicationsApi unit test stubs"""
    def setUp(self):
        self.api = amphora_api_client.api.applications_api.ApplicationsApi(
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_applications_create_application(self):
        """Test case for applications_create_application

        Creates a new application. Applications are external websites that Amphora users can sign in to.  # noqa: E501
        """
        pass

    def test_applications_create_application2(self):
        """Test case for applications_create_application2

        Gets an application by Id, if it exists.  # noqa: E501
        """
        pass

    def test_applications_delete_application(self):
        """Test case for applications_delete_application

        Deletes an application. Must be done by an Organisation administrator.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
