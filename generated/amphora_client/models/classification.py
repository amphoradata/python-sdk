# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Classification(object):
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
        'code': 'str',
        'names': 'list[Name]'
    }

    attribute_map = {
        'code': 'code',
        'names': 'names'
    }

    def __init__(self, code=None, names=None):  # noqa: E501
        """Classification - a model defined in OpenAPI"""  # noqa: E501

        self._code = None
        self._names = None
        self.discriminator = None

        self.code = code
        self.names = names

    @property
    def code(self):
        """Gets the code of this Classification.  # noqa: E501


        :return: The code of this Classification.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Classification.


        :param code: The code of this Classification.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def names(self):
        """Gets the names of this Classification.  # noqa: E501


        :return: The names of this Classification.  # noqa: E501
        :rtype: list[Name]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this Classification.


        :param names: The names of this Classification.  # noqa: E501
        :type: list[Name]
        """

        self._names = names

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
        if not isinstance(other, Classification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
