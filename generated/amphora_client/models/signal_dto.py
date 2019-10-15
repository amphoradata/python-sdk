# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.0.2
    Contact: rian@amphoradata.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SignalDto(object):
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
        'id': 'str',
        'key_name': 'str',
        'value_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'key_name': 'keyName',
        'value_type': 'valueType'
    }

    def __init__(self, id=None, key_name=None, value_type=None):  # noqa: E501
        """SignalDto - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._key_name = None
        self._value_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if key_name is not None:
            self.key_name = key_name
        if value_type is not None:
            self.value_type = value_type

    @property
    def id(self):
        """Gets the id of this SignalDto.  # noqa: E501


        :return: The id of this SignalDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SignalDto.


        :param id: The id of this SignalDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def key_name(self):
        """Gets the key_name of this SignalDto.  # noqa: E501


        :return: The key_name of this SignalDto.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this SignalDto.


        :param key_name: The key_name of this SignalDto.  # noqa: E501
        :type: str
        """
        if key_name is not None and not re.search(r'^[a-zA-Z]{1,20}$', key_name):  # noqa: E501
            raise ValueError(r"Invalid value for `key_name`, must be a follow pattern or equal to `/^[a-zA-Z]{1,20}$/`")  # noqa: E501

        self._key_name = key_name

    @property
    def value_type(self):
        """Gets the value_type of this SignalDto.  # noqa: E501


        :return: The value_type of this SignalDto.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this SignalDto.


        :param value_type: The value_type of this SignalDto.  # noqa: E501
        :type: str
        """

        self._value_type = value_type

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
        if not isinstance(other, SignalDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
