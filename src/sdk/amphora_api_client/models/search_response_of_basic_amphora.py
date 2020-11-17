# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.29
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class SearchResponseOfBasicAmphora(object):
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
        'count': 'int',
        'items': 'list[BasicAmphora]',
        'message': 'str'
    }

    attribute_map = {'count': 'count', 'items': 'items', 'message': 'message'}

    def __init__(self,
                 count=None,
                 items=None,
                 message=None,
                 local_vars_configuration=None):  # noqa: E501
        """SearchResponseOfBasicAmphora - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._items = None
        self._message = None
        self.discriminator = None

        self.count = count
        self.items = items
        self.message = message

    @property
    def count(self):
        """Gets the count of this SearchResponseOfBasicAmphora.  # noqa: E501


        :return: The count of this SearchResponseOfBasicAmphora.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this SearchResponseOfBasicAmphora.


        :param count: The count of this SearchResponseOfBasicAmphora.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def items(self):
        """Gets the items of this SearchResponseOfBasicAmphora.  # noqa: E501


        :return: The items of this SearchResponseOfBasicAmphora.  # noqa: E501
        :rtype: list[BasicAmphora]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this SearchResponseOfBasicAmphora.


        :param items: The items of this SearchResponseOfBasicAmphora.  # noqa: E501
        :type: list[BasicAmphora]
        """

        self._items = items

    @property
    def message(self):
        """Gets the message of this SearchResponseOfBasicAmphora.  # noqa: E501


        :return: The message of this SearchResponseOfBasicAmphora.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SearchResponseOfBasicAmphora.


        :param message: The message of this SearchResponseOfBasicAmphora.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, SearchResponseOfBasicAmphora):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchResponseOfBasicAmphora):
            return True

        return self.to_dict() != other.to_dict()
