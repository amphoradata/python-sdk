# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.9.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class Signal(object):
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
        '_property': 'str',
        'value_type': 'str',
        'attributes': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        '_property': 'property',
        'value_type': 'valueType',
        'attributes': 'attributes'
    }

    def __init__(self, id=None, _property=None, value_type=None, attributes=None, local_vars_configuration=None):  # noqa: E501
        """Signal - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self.__property = None
        self._value_type = None
        self._attributes = None
        self.discriminator = None

        self.id = id
        self._property = _property
        self.value_type = value_type
        self.attributes = attributes

    @property
    def id(self):
        """Gets the id of this Signal.  # noqa: E501


        :return: The id of this Signal.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Signal.


        :param id: The id of this Signal.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def _property(self):
        """Gets the _property of this Signal.  # noqa: E501


        :return: The _property of this Signal.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this Signal.


        :param _property: The _property of this Signal.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                _property is not None and not re.search(r'^[a-z][a-zA-Z_]{2,20}$', _property)):  # noqa: E501
            raise ValueError(r"Invalid value for `_property`, must be a follow pattern or equal to `/^[a-z][a-zA-Z_]{2,20}$/`")  # noqa: E501

        self.__property = _property

    @property
    def value_type(self):
        """Gets the value_type of this Signal.  # noqa: E501


        :return: The value_type of this Signal.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this Signal.


        :param value_type: The value_type of this Signal.  # noqa: E501
        :type: str
        """

        self._value_type = value_type

    @property
    def attributes(self):
        """Gets the attributes of this Signal.  # noqa: E501


        :return: The attributes of this Signal.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Signal.


        :param attributes: The attributes of this Signal.  # noqa: E501
        :type: dict(str, str)
        """

        self._attributes = attributes

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
        if not isinstance(other, Signal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Signal):
            return True

        return self.to_dict() != other.to_dict()
