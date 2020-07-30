# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.14
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class FileListOptionsAllOf(object):
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
    openapi_types = {'order_by': 'str', 'prefix': 'str'}

    attribute_map = {'order_by': 'orderBy', 'prefix': 'prefix'}

    def __init__(self,
                 order_by=None,
                 prefix=None,
                 local_vars_configuration=None):  # noqa: E501
        """FileListOptionsAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._order_by = None
        self._prefix = None
        self.discriminator = None

        self.order_by = order_by
        self.prefix = prefix

    @property
    def order_by(self):
        """Gets the order_by of this FileListOptionsAllOf.  # noqa: E501

        Gets or sets the the orderBy parameter. Options are Alphabetical or LastModified.  # noqa: E501

        :return: The order_by of this FileListOptionsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this FileListOptionsAllOf.

        Gets or sets the the orderBy parameter. Options are Alphabetical or LastModified.  # noqa: E501

        :param order_by: The order_by of this FileListOptionsAllOf.  # noqa: E501
        :type: str
        """

        self._order_by = order_by

    @property
    def prefix(self):
        """Gets the prefix of this FileListOptionsAllOf.  # noqa: E501

        Gets or sets a prefix filter for all file names. Is case sensitive.  # noqa: E501

        :return: The prefix of this FileListOptionsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this FileListOptionsAllOf.

        Gets or sets a prefix filter for all file names. Is case sensitive.  # noqa: E501

        :param prefix: The prefix of this FileListOptionsAllOf.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

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
        if not isinstance(other, FileListOptionsAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileListOptionsAllOf):
            return True

        return self.to_dict() != other.to_dict()
