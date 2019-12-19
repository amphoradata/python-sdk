# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.4.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from amphora_client.configuration import Configuration


class Poi(object):
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
        'phone': 'str',
        'category_set': 'list[CategorySet]',
        'categories': 'list[str]',
        'classifications': 'list[Classification]'
    }

    attribute_map = {
        'name': 'name',
        'phone': 'phone',
        'category_set': 'categorySet',
        'categories': 'categories',
        'classifications': 'classifications'
    }

    def __init__(self, name=None, phone=None, category_set=None, categories=None, classifications=None, local_vars_configuration=None):  # noqa: E501
        """Poi - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._phone = None
        self._category_set = None
        self._categories = None
        self._classifications = None
        self.discriminator = None

        self.name = name
        self.phone = phone
        if category_set is not None:
            self.category_set = category_set
        if categories is not None:
            self.categories = categories
        if classifications is not None:
            self.classifications = classifications

    @property
    def name(self):
        """Gets the name of this Poi.  # noqa: E501


        :return: The name of this Poi.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Poi.


        :param name: The name of this Poi.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this Poi.  # noqa: E501


        :return: The phone of this Poi.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Poi.


        :param phone: The phone of this Poi.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def category_set(self):
        """Gets the category_set of this Poi.  # noqa: E501


        :return: The category_set of this Poi.  # noqa: E501
        :rtype: list[CategorySet]
        """
        return self._category_set

    @category_set.setter
    def category_set(self, category_set):
        """Sets the category_set of this Poi.


        :param category_set: The category_set of this Poi.  # noqa: E501
        :type: list[CategorySet]
        """

        self._category_set = category_set

    @property
    def categories(self):
        """Gets the categories of this Poi.  # noqa: E501


        :return: The categories of this Poi.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this Poi.


        :param categories: The categories of this Poi.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    @property
    def classifications(self):
        """Gets the classifications of this Poi.  # noqa: E501


        :return: The classifications of this Poi.  # noqa: E501
        :rtype: list[Classification]
        """
        return self._classifications

    @classifications.setter
    def classifications(self, classifications):
        """Sets the classifications of this Poi.


        :param classifications: The classifications of this Poi.  # noqa: E501
        :type: list[Classification]
        """

        self._classifications = classifications

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
        if not isinstance(other, Poi):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Poi):
            return True

        return self.to_dict() != other.to_dict()
