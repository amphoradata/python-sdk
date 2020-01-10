# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.5.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from amphora_client.configuration import Configuration


class UserDto(object):
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
        'about': 'str',
        'full_name': 'str',
        'organisation_id': 'str',
        'user_name': 'str',
        'last_modified': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'about': 'about',
        'full_name': 'fullName',
        'organisation_id': 'organisationId',
        'user_name': 'userName',
        'last_modified': 'lastModified'
    }

    def __init__(self, id=None, email=None, about=None, full_name=None, organisation_id=None, user_name=None, last_modified=None, local_vars_configuration=None):  # noqa: E501
        """UserDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._email = None
        self._about = None
        self._full_name = None
        self._organisation_id = None
        self._user_name = None
        self._last_modified = None
        self.discriminator = None

        self.id = id
        self.email = email
        self.about = about
        self.full_name = full_name
        self.organisation_id = organisation_id
        self.user_name = user_name
        self.last_modified = last_modified

    @property
    def id(self):
        """Gets the id of this UserDto.  # noqa: E501


        :return: The id of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserDto.


        :param id: The id of this UserDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def email(self):
        """Gets the email of this UserDto.  # noqa: E501


        :return: The email of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserDto.


        :param email: The email of this UserDto.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def about(self):
        """Gets the about of this UserDto.  # noqa: E501


        :return: The about of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._about

    @about.setter
    def about(self, about):
        """Sets the about of this UserDto.


        :param about: The about of this UserDto.  # noqa: E501
        :type: str
        """

        self._about = about

    @property
    def full_name(self):
        """Gets the full_name of this UserDto.  # noqa: E501


        :return: The full_name of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this UserDto.


        :param full_name: The full_name of this UserDto.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def organisation_id(self):
        """Gets the organisation_id of this UserDto.  # noqa: E501


        :return: The organisation_id of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this UserDto.


        :param organisation_id: The organisation_id of this UserDto.  # noqa: E501
        :type: str
        """

        self._organisation_id = organisation_id

    @property
    def user_name(self):
        """Gets the user_name of this UserDto.  # noqa: E501


        :return: The user_name of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserDto.


        :param user_name: The user_name of this UserDto.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def last_modified(self):
        """Gets the last_modified of this UserDto.  # noqa: E501


        :return: The last_modified of this UserDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this UserDto.


        :param last_modified: The last_modified of this UserDto.  # noqa: E501
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
        if not isinstance(other, UserDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserDto):
            return True

        return self.to_dict() != other.to_dict()
