# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.28
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class CollectionResponseOfFeedItem(object):
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
        'message': 'str',
        'count': 'int',
        'items': 'list[FeedItem]'
    }

    attribute_map = {'message': 'message', 'count': 'count', 'items': 'items'}

    def __init__(self,
                 message=None,
                 count=None,
                 items=None,
                 local_vars_configuration=None):  # noqa: E501
        """CollectionResponseOfFeedItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._message = None
        self._count = None
        self._items = None
        self.discriminator = None

        self.message = message
        self.count = count
        self.items = items

    @property
    def message(self):
        """Gets the message of this CollectionResponseOfFeedItem.  # noqa: E501


        :return: The message of this CollectionResponseOfFeedItem.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CollectionResponseOfFeedItem.


        :param message: The message of this CollectionResponseOfFeedItem.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def count(self):
        """Gets the count of this CollectionResponseOfFeedItem.  # noqa: E501


        :return: The count of this CollectionResponseOfFeedItem.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CollectionResponseOfFeedItem.


        :param count: The count of this CollectionResponseOfFeedItem.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def items(self):
        """Gets the items of this CollectionResponseOfFeedItem.  # noqa: E501


        :return: The items of this CollectionResponseOfFeedItem.  # noqa: E501
        :rtype: list[FeedItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CollectionResponseOfFeedItem.


        :param items: The items of this CollectionResponseOfFeedItem.  # noqa: E501
        :type: list[FeedItem]
        """

        self._items = items

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
        if not isinstance(other, CollectionResponseOfFeedItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CollectionResponseOfFeedItem):
            return True

        return self.to_dict() != other.to_dict()
