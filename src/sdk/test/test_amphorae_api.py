# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.28
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
        self.api = amphora_api_client.api.amphorae_api.AmphoraeApi(
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_amphora_quality_get(self):
        """Test case for amphora_quality_get

        Gets the data quality metrics for this Amphora.  # noqa: E501
        """
        pass

    def test_amphora_quality_set(self):
        """Test case for amphora_quality_set

        Sets the data quality metrics for this Amphora.  # noqa: E501
        """
        pass

    def test_amphorae_access_controls_create_for_all(self):
        """Test case for amphorae_access_controls_create_for_all

        Creates an Access Control Rule for all on this Amphora.  # noqa: E501
        """
        pass

    def test_amphorae_access_controls_create_for_organisation(self):
        """Test case for amphorae_access_controls_create_for_organisation

        Creates an Access Control Rule on this Amphora.  # noqa: E501
        """
        pass

    def test_amphorae_access_controls_create_for_user(self):
        """Test case for amphorae_access_controls_create_for_user

        Creates an Access Control rule on this Amphora.  # noqa: E501
        """
        pass

    def test_amphorae_access_controls_delete(self):
        """Test case for amphorae_access_controls_delete

        Deletes an Access Control on this Amphora.  # noqa: E501
        """
        pass

    def test_amphorae_access_controls_get_for_all_rule(self):
        """Test case for amphorae_access_controls_get_for_all_rule

        Gets the 'for all' rule, if it exists, else an empty 200.  # noqa: E501
        """
        pass

    def test_amphorae_access_controls_get_organisation_rules(self):
        """Test case for amphorae_access_controls_get_organisation_rules

        Gets the list of access rules applied to organisations.  # noqa: E501
        """
        pass

    def test_amphorae_access_controls_get_user_rules(self):
        """Test case for amphorae_access_controls_get_user_rules

        Gets the list of access rules applied to users.  # noqa: E501
        """
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

    def test_amphorae_files_delete_file(self):
        """Test case for amphorae_files_delete_file

        Gets the contents of a file. Returns application/octet-stream.  # noqa: E501
        """
        pass

    def test_amphorae_files_download_file(self):
        """Test case for amphorae_files_download_file

        Gets the contents of a file. Returns application/octet-stream.  # noqa: E501
        """
        pass

    def test_amphorae_files_list_files(self):
        """Test case for amphorae_files_list_files

        Lists an Amphora's files.  # noqa: E501
        """
        pass

    def test_amphorae_files_query_files(self):
        """Test case for amphorae_files_query_files

        Queries an Amphora's files.  # noqa: E501
        """
        pass

    def test_amphorae_files_read_file_attributes(self):
        """Test case for amphorae_files_read_file_attributes

        Gets the attributes of a file.  # noqa: E501
        """
        pass

    def test_amphorae_files_write_file_attributes(self):
        """Test case for amphorae_files_write_file_attributes

        Gets the attributes of a file.  # noqa: E501
        """
        pass

    def test_amphorae_list(self):
        """Test case for amphorae_list

        Gets a list of Amphora for yourself or your org, created or purchased by you (or organisation).  # noqa: E501
        """
        pass

    def test_amphorae_read(self):
        """Test case for amphorae_read

        Gets details of an Amphora by Id.  # noqa: E501
        """
        pass

    def test_amphorae_signals_create_signal(self):
        """Test case for amphorae_signals_create_signal

        Associates a signal with an Amphora. Signal is created if not existing.  # noqa: E501
        """
        pass

    def test_amphorae_signals_get_signal(self):
        """Test case for amphorae_signals_get_signal

        Gets the signals associated with an Amphora.  # noqa: E501
        """
        pass

    def test_amphorae_signals_get_signals(self):
        """Test case for amphorae_signals_get_signals

        Gets the signals associated with an Amphora.  # noqa: E501
        """
        pass

    def test_amphorae_signals_update_signal(self):
        """Test case for amphorae_signals_update_signal

        Associates a signal with an Amphora. Signal is created if not existing.  # noqa: E501
        """
        pass

    def test_amphorae_signals_upload_signal(self):
        """Test case for amphorae_signals_upload_signal

        Uploads values to an Amphora signal(s).  # noqa: E501
        """
        pass

    def test_amphorae_signals_upload_signal2(self):
        """Test case for amphorae_signals_upload_signal2

        Uploads values to an Amphora signal(s).  # noqa: E501
        """
        pass

    def test_amphorae_signals_upload_signal_batch(self):
        """Test case for amphorae_signals_upload_signal_batch

        Uploads values in batch to an Amphora signal(s).  # noqa: E501
        """
        pass

    def test_amphorae_signals_upload_signal_batch_all(self):
        """Test case for amphorae_signals_upload_signal_batch_all

        Uploads values in batch to an Amphora signal(s).  # noqa: E501
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
