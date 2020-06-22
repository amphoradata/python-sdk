# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.7
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class AccessLevelResponse(object):
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
        'amphora_id': 'str',
        'access_level': 'int',
        'is_authorized': 'bool'
    }

    attribute_map = {
        'amphora_id': 'amphoraId',
        'access_level': 'accessLevel',
        'is_authorized': 'isAuthorized'
    }

    def __init__(self,
                 amphora_id=None,
                 access_level=None,
                 is_authorized=None,
                 local_vars_configuration=None):  # noqa: E501
        """AccessLevelResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amphora_id = None
        self._access_level = None
        self._is_authorized = None
        self.discriminator = None

        self.amphora_id = amphora_id
        if access_level is not None:
            self.access_level = access_level
        if is_authorized is not None:
            self.is_authorized = is_authorized

    @property
    def amphora_id(self):
        """Gets the amphora_id of this AccessLevelResponse.  # noqa: E501

        Gets or sets The id of the Amphora you are checking.  # noqa: E501

        :return: The amphora_id of this AccessLevelResponse.  # noqa: E501
        :rtype: str
        """
        return self._amphora_id

    @amphora_id.setter
    def amphora_id(self, amphora_id):
        """Sets the amphora_id of this AccessLevelResponse.

        Gets or sets The id of the Amphora you are checking.  # noqa: E501

        :param amphora_id: The amphora_id of this AccessLevelResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation
                and amphora_id is not None and len(amphora_id) > 50):
            raise ValueError(
                "Invalid value for `amphora_id`, length must be less than or equal to `50`"
            )  # noqa: E501
        if (self.local_vars_configuration.client_side_validation
                and amphora_id is not None and len(amphora_id) < 5):
            raise ValueError(
                "Invalid value for `amphora_id`, length must be greater than or equal to `5`"
            )  # noqa: E501

        self._amphora_id = amphora_id

    @property
    def access_level(self):
        """Gets the access_level of this AccessLevelResponse.  # noqa: E501

        Gets or sets the access level that will be checked. Ranges from 0 (none) to 256 (Administer).  # noqa: E501

        :return: The access_level of this AccessLevelResponse.  # noqa: E501
        :rtype: int
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        """Sets the access_level of this AccessLevelResponse.

        Gets or sets the access level that will be checked. Ranges from 0 (none) to 256 (Administer).  # noqa: E501

        :param access_level: The access_level of this AccessLevelResponse.  # noqa: E501
        :type: int
        """

        self._access_level = access_level

    @property
    def is_authorized(self):
        """Gets the is_authorized of this AccessLevelResponse.  # noqa: E501

        Gets or sets a value indicating whether is authorized at that level.  # noqa: E501

        :return: The is_authorized of this AccessLevelResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_authorized

    @is_authorized.setter
    def is_authorized(self, is_authorized):
        """Sets the is_authorized of this AccessLevelResponse.

        Gets or sets a value indicating whether is authorized at that level.  # noqa: E501

        :param is_authorized: The is_authorized of this AccessLevelResponse.  # noqa: E501
        :type: bool
        """

        self._is_authorized = is_authorized

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
        if not isinstance(other, AccessLevelResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessLevelResponse):
            return True

        return self.to_dict() != other.to_dict()
