# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import amphora_client
from amphora_client.api.amphorae_statistics_api import AmphoraeStatisticsApi  # noqa: E501
from amphora_client.rest import ApiException


class TestAmphoraeStatisticsApi(unittest.TestCase):
    """AmphoraeStatisticsApi unit test stubs"""

    def setUp(self):
        self.api = amphora_client.api.amphorae_statistics_api.AmphoraeStatisticsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_amphorae_statistics_count(self):
        """Test case for amphorae_statistics_count

        Gets ta count of all the Amphora  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
