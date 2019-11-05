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
from amphora_client.api.invitations_api import InvitationsApi  # noqa: E501
from amphora_client.rest import ApiException


class TestInvitationsApi(unittest.TestCase):
    """InvitationsApi unit test stubs"""

    def setUp(self):
        self.api = amphora_client.api.invitations_api.InvitationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_invitations_accept_invitation(self):
        """Test case for invitations_accept_invitation

        Accepts an invitation sent to me  # noqa: E501
        """
        pass

    def test_invitations_get_my_invitations(self):
        """Test case for invitations_get_my_invitations

        Returns all the invitations sent to me  # noqa: E501
        """
        pass

    def test_invitations_invite_new_user(self):
        """Test case for invitations_invite_new_user

        Invite a new email address to Amphora Data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()