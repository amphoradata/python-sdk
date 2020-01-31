# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.6.6
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from amphora_client.configuration import Configuration


class Name(object):
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
        'name_locale': 'str',
        'name_name': 'str'
    }

    attribute_map = {
        'name_locale': 'nameLocale',
        'name_name': 'nameName'
    }

    def __init__(self, name_locale=None, name_name=None, local_vars_configuration=None):  # noqa: E501
        """Name - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name_locale = None
        self._name_name = None
        self.discriminator = None

        self.name_locale = name_locale
        self.name_name = name_name

    @property
    def name_locale(self):
        """Gets the name_locale of this Name.  # noqa: E501


        :return: The name_locale of this Name.  # noqa: E501
        :rtype: str
        """
        return self._name_locale

    @name_locale.setter
    def name_locale(self, name_locale):
        """Sets the name_locale of this Name.


        :param name_locale: The name_locale of this Name.  # noqa: E501
        :type: str
        """

        self._name_locale = name_locale

    @property
    def name_name(self):
        """Gets the name_name of this Name.  # noqa: E501


        :return: The name_name of this Name.  # noqa: E501
        :rtype: str
        """
        return self._name_name

    @name_name.setter
    def name_name(self, name_name):
        """Sets the name_name of this Name.


        :param name_name: The name_name of this Name.  # noqa: E501
        :type: str
        """

        self._name_name = name_name

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
        if not isinstance(other, Name):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Name):
            return True

        return self.to_dict() != other.to_dict()
