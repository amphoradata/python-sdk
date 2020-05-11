# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.0
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class CreateAmphoraUserAllOf(object):
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
        'password': 'str',
        'confirm_password': 'str',
        'email': 'str'
    }

    attribute_map = {
        'password': 'password',
        'confirm_password': 'confirmPassword',
        'email': 'email'
    }

    def __init__(self,
                 password=None,
                 confirm_password=None,
                 email=None,
                 local_vars_configuration=None):  # noqa: E501
        """CreateAmphoraUserAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._password = None
        self._confirm_password = None
        self._email = None
        self.discriminator = None

        self.password = password
        self.confirm_password = confirm_password
        self.email = email

    @property
    def password(self):
        """Gets the password of this CreateAmphoraUserAllOf.  # noqa: E501


        :return: The password of this CreateAmphoraUserAllOf.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateAmphoraUserAllOf.


        :param password: The password of this CreateAmphoraUserAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`"
                             )  # noqa: E501
        if (self.local_vars_configuration.client_side_validation
                and password is not None and len(password) > 100):
            raise ValueError(
                "Invalid value for `password`, length must be less than or equal to `100`"
            )  # noqa: E501
        if (self.local_vars_configuration.client_side_validation
                and password is not None and len(password) < 6):
            raise ValueError(
                "Invalid value for `password`, length must be greater than or equal to `6`"
            )  # noqa: E501

        self._password = password

    @property
    def confirm_password(self):
        """Gets the confirm_password of this CreateAmphoraUserAllOf.  # noqa: E501


        :return: The confirm_password of this CreateAmphoraUserAllOf.  # noqa: E501
        :rtype: str
        """
        return self._confirm_password

    @confirm_password.setter
    def confirm_password(self, confirm_password):
        """Sets the confirm_password of this CreateAmphoraUserAllOf.


        :param confirm_password: The confirm_password of this CreateAmphoraUserAllOf.  # noqa: E501
        :type: str
        """

        self._confirm_password = confirm_password

    @property
    def email(self):
        """Gets the email of this CreateAmphoraUserAllOf.  # noqa: E501


        :return: The email of this CreateAmphoraUserAllOf.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateAmphoraUserAllOf.


        :param email: The email of this CreateAmphoraUserAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError(
                "Invalid value for `email`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation
                and email is not None and len(email) < 1):
            raise ValueError(
                "Invalid value for `email`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._email = email

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
        if not isinstance(other, CreateAmphoraUserAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateAmphoraUserAllOf):
            return True

        return self.to_dict() != other.to_dict()
