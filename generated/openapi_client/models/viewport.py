# coding: utf-8

"""
    AmphoraApi

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Viewport(object):
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
        'top_left_point': 'Position',
        'btm_right_point': 'Position'
    }

    attribute_map = {
        'top_left_point': 'topLeftPoint',
        'btm_right_point': 'btmRightPoint'
    }

    def __init__(self, top_left_point=None, btm_right_point=None):  # noqa: E501
        """Viewport - a model defined in OpenAPI"""  # noqa: E501

        self._top_left_point = None
        self._btm_right_point = None
        self.discriminator = None

        if top_left_point is not None:
            self.top_left_point = top_left_point
        if btm_right_point is not None:
            self.btm_right_point = btm_right_point

    @property
    def top_left_point(self):
        """Gets the top_left_point of this Viewport.  # noqa: E501


        :return: The top_left_point of this Viewport.  # noqa: E501
        :rtype: Position
        """
        return self._top_left_point

    @top_left_point.setter
    def top_left_point(self, top_left_point):
        """Sets the top_left_point of this Viewport.


        :param top_left_point: The top_left_point of this Viewport.  # noqa: E501
        :type: Position
        """

        self._top_left_point = top_left_point

    @property
    def btm_right_point(self):
        """Gets the btm_right_point of this Viewport.  # noqa: E501


        :return: The btm_right_point of this Viewport.  # noqa: E501
        :rtype: Position
        """
        return self._btm_right_point

    @btm_right_point.setter
    def btm_right_point(self, btm_right_point):
        """Sets the btm_right_point of this Viewport.


        :param btm_right_point: The btm_right_point of this Viewport.  # noqa: E501
        :type: Position
        """

        self._btm_right_point = btm_right_point

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
        if not isinstance(other, Viewport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
