# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.9.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import amphora_api_client
from amphora_api_client.api.amphorae_api import AmphoraeApi  # noqa: E501
from amphora_api_client.rest import ApiException


class TestAmphoraeApi(unittest.TestCase):
    """AmphoraeApi unit test stubs"""

    def setUp(self):
        self.api = amphora_api_client.api.amphorae_api.AmphoraeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_amphorae_create(self):
        """Test case for amphorae_create

        Creates a new empty Amphora in the user's organisation.  # noqa: E501
        """
        pass

    def test_amphorae_delete(self):
        """Test case for amphorae_delete

        Deletes an Amphora.  # noqa: E501
        """
        pass

    def test_amphorae_files_create_file_request(self):
        """Test case for amphorae_files_create_file_request

        Creates a file. Returns a blob URL to upload to.  # noqa: E501
        """
        pass

    def test_amphorae_files_download_file(self):
        """Test case for amphorae_files_download_file

        Get's the contents of a file. Returns application/octet-stream.  # noqa: E501
        """
        pass

    def test_amphorae_files_list_files(self):
        """Test case for amphorae_files_list_files

        Get's a list of an Amphora's files.  # noqa: E501
        """
        pass

    def test_amphorae_files_write_file_metadata(self):
        """Test case for amphorae_files_write_file_metadata

        """
        pass

    def test_amphorae_read(self):
        """Test case for amphorae_read

        Get's details of an Amphora by Id.  # noqa: E501
        """
        pass

    def test_amphorae_restrictions_create(self):
        """Test case for amphorae_restrictions_create

        Creates a restriction on this Amphora.  # noqa: E501
        """
        pass

    def test_amphorae_restrictions_delete(self):
        """Test case for amphorae_restrictions_delete

        Deletes a restriction on this Amphora.  # noqa: E501
        """
        pass

    def test_amphorae_signals_create_signal(self):
        """Test case for amphorae_signals_create_signal

        Associates a signal with an Amphora. Signal is created if not existing.  # noqa: E501
        """
        pass

    def test_amphorae_signals_get_signals(self):
        """Test case for amphorae_signals_get_signals

        Get's the signals associated with an Amphora.  # noqa: E501
        """
        pass

    def test_amphorae_signals_update_signal(self):
        """Test case for amphorae_signals_update_signal

        Associates a signal with an Amphora. Signal is created if not existing.  # noqa: E501
        """
        pass

    def test_amphorae_signals_upload_signal(self):
        """Test case for amphorae_signals_upload_signal

        """
        pass

    def test_amphorae_signals_upload_signal2(self):
        """Test case for amphorae_signals_upload_signal2

        """
        pass

    def test_amphorae_signals_upload_signal_batch(self):
        """Test case for amphorae_signals_upload_signal_batch

        """
        pass

    def test_amphorae_signals_upload_signal_batch2(self):
        """Test case for amphorae_signals_upload_signal_batch2

        """
        pass

    def test_amphorae_update(self):
        """Test case for amphorae_update

        Updates the details of an Amphora by Id.  # noqa: E501
        """
        pass

    def test_purchases_purchase(self):
        """Test case for purchases_purchase

        Purchases an Amphora as the logged in user.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
