# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.6.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from amphora_client.configuration import Configuration


class Position(object):
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
        'lat': 'float',
        'lon': 'float'
    }

    attribute_map = {
        'lat': 'lat',
        'lon': 'lon'
    }

    def __init__(self, lat=None, lon=None, local_vars_configuration=None):  # noqa: E501
        """Position - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._lat = None
        self._lon = None
        self.discriminator = None

        if lat is not None:
            self.lat = lat
        if lon is not None:
            self.lon = lon

    @property
    def lat(self):
        """Gets the lat of this Position.  # noqa: E501


        :return: The lat of this Position.  # noqa: E501
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this Position.


        :param lat: The lat of this Position.  # noqa: E501
        :type: float
        """

        self._lat = lat

    @property
    def lon(self):
        """Gets the lon of this Position.  # noqa: E501


        :return: The lon of this Position.  # noqa: E501
        :rtype: float
        """
        return self._lon

    @lon.setter
    def lon(self, lon):
        """Sets the lon of this Position.


        :param lon: The lon of this Position.  # noqa: E501
        :type: float
        """

        self._lon = lon

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
        if not isinstance(other, Position):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Position):
            return True

        return self.to_dict() != other.to_dict()
