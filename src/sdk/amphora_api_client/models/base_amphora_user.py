# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.11
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class BaseAmphoraUser(object):
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
        'phone_number': 'str',
        'about': 'str',
        'full_name': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'phone_number': 'phoneNumber',
        'about': 'about',
        'full_name': 'fullName',
        'user_name': 'userName'
    }

    def __init__(self,
                 phone_number=None,
                 about=None,
                 full_name=None,
                 user_name=None,
                 local_vars_configuration=None):  # noqa: E501
        """BaseAmphoraUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._phone_number = None
        self._about = None
        self._full_name = None
        self._user_name = None
        self.discriminator = None

        self.phone_number = phone_number
        self.about = about
        self.full_name = full_name
        self.user_name = user_name

    @property
    def phone_number(self):
        """Gets the phone_number of this BaseAmphoraUser.  # noqa: E501


        :return: The phone_number of this BaseAmphoraUser.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this BaseAmphoraUser.


        :param phone_number: The phone_number of this BaseAmphoraUser.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation
                and phone_number is not None and len(phone_number) > 20):
            raise ValueError(
                "Invalid value for `phone_number`, length must be less than or equal to `20`"
            )  # noqa: E501
        if (self.local_vars_configuration.client_side_validation
                and phone_number is not None and len(phone_number) < 6):
            raise ValueError(
                "Invalid value for `phone_number`, length must be greater than or equal to `6`"
            )  # noqa: E501

        self._phone_number = phone_number

    @property
    def about(self):
        """Gets the about of this BaseAmphoraUser.  # noqa: E501


        :return: The about of this BaseAmphoraUser.  # noqa: E501
        :rtype: str
        """
        return self._about

    @about.setter
    def about(self, about):
        """Sets the about of this BaseAmphoraUser.


        :param about: The about of this BaseAmphoraUser.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation
                and about is not None and len(about) > 255):
            raise ValueError(
                "Invalid value for `about`, length must be less than or equal to `255`"
            )  # noqa: E501

        self._about = about

    @property
    def full_name(self):
        """Gets the full_name of this BaseAmphoraUser.  # noqa: E501


        :return: The full_name of this BaseAmphoraUser.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this BaseAmphoraUser.


        :param full_name: The full_name of this BaseAmphoraUser.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def user_name(self):
        """Gets the user_name of this BaseAmphoraUser.  # noqa: E501


        :return: The user_name of this BaseAmphoraUser.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this BaseAmphoraUser.


        :param user_name: The user_name of this BaseAmphoraUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_name is None:  # noqa: E501
            raise ValueError(
                "Invalid value for `user_name`, must not be `None`"
            )  # noqa: E501
        if (self.local_vars_configuration.client_side_validation
                and user_name is not None and len(user_name) < 1):
            raise ValueError(
                "Invalid value for `user_name`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._user_name = user_name

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
        if not isinstance(other, BaseAmphoraUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BaseAmphoraUser):
            return True

        return self.to_dict() != other.to_dict()
