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
from openapi_client.api.images_api import ImagesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestImagesApi(unittest.TestCase):
    """ImagesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.images_api.ImagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_organisations_id_profile_jpg_get(self):
        """Test case for api_organisations_id_profile_jpg_get

        Gets an organisations profile picture  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
