# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.16
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class FileQueryOptionsAllOf(object):
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
    openapi_types = {'attributes': 'dict(str, str)', 'all_attributes': 'bool'}

    attribute_map = {
        'attributes': 'attributes',
        'all_attributes': 'allAttributes'
    }

    def __init__(self,
                 attributes=None,
                 all_attributes=None,
                 local_vars_configuration=None):  # noqa: E501
        """FileQueryOptionsAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attributes = None
        self._all_attributes = None
        self.discriminator = None

        self.attributes = attributes
        if all_attributes is not None:
            self.all_attributes = all_attributes

    @property
    def attributes(self):
        """Gets the attributes of this FileQueryOptionsAllOf.  # noqa: E501

        Gets or sets the attribute filters.  # noqa: E501

        :return: The attributes of this FileQueryOptionsAllOf.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this FileQueryOptionsAllOf.

        Gets or sets the attribute filters.  # noqa: E501

        :param attributes: The attributes of this FileQueryOptionsAllOf.  # noqa: E501
        :type: dict(str, str)
        """

        self._attributes = attributes

    @property
    def all_attributes(self):
        """Gets the all_attributes of this FileQueryOptionsAllOf.  # noqa: E501

        Gets or sets a value indicating whether whether all attributes are required to match. Defaults to false.  # noqa: E501

        :return: The all_attributes of this FileQueryOptionsAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._all_attributes

    @all_attributes.setter
    def all_attributes(self, all_attributes):
        """Sets the all_attributes of this FileQueryOptionsAllOf.

        Gets or sets a value indicating whether whether all attributes are required to match. Defaults to false.  # noqa: E501

        :param all_attributes: The all_attributes of this FileQueryOptionsAllOf.  # noqa: E501
        :type: bool
        """

        self._all_attributes = all_attributes

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
        if not isinstance(other, FileQueryOptionsAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileQueryOptionsAllOf):
            return True

        return self.to_dict() != other.to_dict()
