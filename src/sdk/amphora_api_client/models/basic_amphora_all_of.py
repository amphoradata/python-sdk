# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.9.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class BasicAmphoraAllOf(object):
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
        'name': 'str',
        'price': 'float',
        'labels': 'str'
    }

    attribute_map = {
        'name': 'name',
        'price': 'price',
        'labels': 'labels'
    }

    def __init__(self, name=None, price=None, labels=None, local_vars_configuration=None):  # noqa: E501
        """BasicAmphoraAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._price = None
        self._labels = None
        self.discriminator = None

        self.name = name
        self.price = price
        self.labels = labels

    @property
    def name(self):
        """Gets the name of this BasicAmphoraAllOf.  # noqa: E501


        :return: The name of this BasicAmphoraAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BasicAmphoraAllOf.


        :param name: The name of this BasicAmphoraAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def price(self):
        """Gets the price of this BasicAmphoraAllOf.  # noqa: E501


        :return: The price of this BasicAmphoraAllOf.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this BasicAmphoraAllOf.


        :param price: The price of this BasicAmphoraAllOf.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and price is None:  # noqa: E501
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def labels(self):
        """Gets the labels of this BasicAmphoraAllOf.  # noqa: E501


        :return: The labels of this BasicAmphoraAllOf.  # noqa: E501
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this BasicAmphoraAllOf.


        :param labels: The labels of this BasicAmphoraAllOf.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                labels is not None and not re.search(r'^(([-\w ]{0,12})[, ]?){1,6}$', labels)):  # noqa: E501
            raise ValueError(r"Invalid value for `labels`, must be a follow pattern or equal to `/^(([-\w ]{0,12})[, ]?){1,6}$/`")  # noqa: E501

        self._labels = labels

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
        if not isinstance(other, BasicAmphoraAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BasicAmphoraAllOf):
            return True

        return self.to_dict() != other.to_dict()
