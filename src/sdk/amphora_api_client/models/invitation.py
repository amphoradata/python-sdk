# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.6
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class Invitation(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'target_email': 'str',
        'target_organisation_id': 'str',
        'is_claimed': 'bool'
    }

    attribute_map = {
        'target_email': 'targetEmail',
        'target_organisation_id': 'targetOrganisationId',
        'is_claimed': 'isClaimed'
    }

    def __init__(self,
                 target_email=None,
                 target_organisation_id=None,
                 is_claimed=None,
                 local_vars_configuration=None):  # noqa: E501
        """Invitation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._target_email = None
        self._target_organisation_id = None
        self._is_claimed = None
        self.discriminator = None

        self.target_email = target_email
        self.target_organisation_id = target_organisation_id
        self.is_claimed = is_claimed

    @property
    def target_email(self):
        """Gets the target_email of this Invitation.  # noqa: E501


        :return: The target_email of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._target_email

    @target_email.setter
    def target_email(self, target_email):
        """Sets the target_email of this Invitation.


        :param target_email: The target_email of this Invitation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and target_email is None:  # noqa: E501
            raise ValueError(
                "Invalid value for `target_email`, must not be `None`"
            )  # noqa: E501
        if (self.local_vars_configuration.client_side_validation
                and target_email is not None and len(target_email) < 1):
            raise ValueError(
                "Invalid value for `target_email`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._target_email = target_email

    @property
    def target_organisation_id(self):
        """Gets the target_organisation_id of this Invitation.  # noqa: E501


        :return: The target_organisation_id of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._target_organisation_id

    @target_organisation_id.setter
    def target_organisation_id(self, target_organisation_id):
        """Sets the target_organisation_id of this Invitation.


        :param target_organisation_id: The target_organisation_id of this Invitation.  # noqa: E501
        :type: str
        """

        self._target_organisation_id = target_organisation_id

    @property
    def is_claimed(self):
        """Gets the is_claimed of this Invitation.  # noqa: E501


        :return: The is_claimed of this Invitation.  # noqa: E501
        :rtype: bool
        """
        return self._is_claimed

    @is_claimed.setter
    def is_claimed(self, is_claimed):
        """Sets the is_claimed of this Invitation.


        :param is_claimed: The is_claimed of this Invitation.  # noqa: E501
        :type: bool
        """

        self._is_claimed = is_claimed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Invitation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Invitation):
            return True

        return self.to_dict() != other.to_dict()
