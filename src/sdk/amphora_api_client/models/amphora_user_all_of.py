# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.9.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class AmphoraUserAllOf(object):
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
        'id': 'str',
        'email': 'str',
        'organisation_id': 'str',
        'last_modified': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'organisation_id': 'organisationId',
        'last_modified': 'lastModified'
    }

    def __init__(self, id=None, email=None, organisation_id=None, last_modified=None, local_vars_configuration=None):  # noqa: E501
        """AmphoraUserAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._email = None
        self._organisation_id = None
        self._last_modified = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.email = email
        self.organisation_id = organisation_id
        self.last_modified = last_modified

    @property
    def id(self):
        """Gets the id of this AmphoraUserAllOf.  # noqa: E501


        :return: The id of this AmphoraUserAllOf.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AmphoraUserAllOf.


        :param id: The id of this AmphoraUserAllOf.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def email(self):
        """Gets the email of this AmphoraUserAllOf.  # noqa: E501


        :return: The email of this AmphoraUserAllOf.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AmphoraUserAllOf.


        :param email: The email of this AmphoraUserAllOf.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def organisation_id(self):
        """Gets the organisation_id of this AmphoraUserAllOf.  # noqa: E501


        :return: The organisation_id of this AmphoraUserAllOf.  # noqa: E501
        :rtype: str
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this AmphoraUserAllOf.


        :param organisation_id: The organisation_id of this AmphoraUserAllOf.  # noqa: E501
        :type: str
        """

        self._organisation_id = organisation_id

    @property
    def last_modified(self):
        """Gets the last_modified of this AmphoraUserAllOf.  # noqa: E501


        :return: The last_modified of this AmphoraUserAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this AmphoraUserAllOf.


        :param last_modified: The last_modified of this AmphoraUserAllOf.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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
        if not isinstance(other, AmphoraUserAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AmphoraUserAllOf):
            return True

        return self.to_dict() != other.to_dict()