# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.27
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class CategoricalVariable(object):
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
        'filter': 'OneOfTsx',
        'value': 'OneOfTsx',
        'interpolation': 'OneOfInterpolation',
        'categories': 'list[TimeSeriesAggregateCategory]',
        'default_category': 'OneOfTimeSeriesDefaultCategory'
    }

    attribute_map = {
        'filter': 'filter',
        'value': 'value',
        'interpolation': 'interpolation',
        'categories': 'categories',
        'default_category': 'defaultCategory'
    }

    def __init__(self,
                 filter=None,
                 value=None,
                 interpolation=None,
                 categories=None,
                 default_category=None,
                 local_vars_configuration=None):  # noqa: E501
        """CategoricalVariable - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._filter = None
        self._value = None
        self._interpolation = None
        self._categories = None
        self._default_category = None
        self.discriminator = None

        self.filter = filter
        self.value = value
        self.interpolation = interpolation
        self.categories = categories
        self.default_category = default_category

    @property
    def filter(self):
        """Gets the filter of this CategoricalVariable.  # noqa: E501


        :return: The filter of this CategoricalVariable.  # noqa: E501
        :rtype: OneOfTsx
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this CategoricalVariable.


        :param filter: The filter of this CategoricalVariable.  # noqa: E501
        :type: OneOfTsx
        """

        self._filter = filter

    @property
    def value(self):
        """Gets the value of this CategoricalVariable.  # noqa: E501


        :return: The value of this CategoricalVariable.  # noqa: E501
        :rtype: OneOfTsx
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CategoricalVariable.


        :param value: The value of this CategoricalVariable.  # noqa: E501
        :type: OneOfTsx
        """

        self._value = value

    @property
    def interpolation(self):
        """Gets the interpolation of this CategoricalVariable.  # noqa: E501


        :return: The interpolation of this CategoricalVariable.  # noqa: E501
        :rtype: OneOfInterpolation
        """
        return self._interpolation

    @interpolation.setter
    def interpolation(self, interpolation):
        """Sets the interpolation of this CategoricalVariable.


        :param interpolation: The interpolation of this CategoricalVariable.  # noqa: E501
        :type: OneOfInterpolation
        """

        self._interpolation = interpolation

    @property
    def categories(self):
        """Gets the categories of this CategoricalVariable.  # noqa: E501


        :return: The categories of this CategoricalVariable.  # noqa: E501
        :rtype: list[TimeSeriesAggregateCategory]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this CategoricalVariable.


        :param categories: The categories of this CategoricalVariable.  # noqa: E501
        :type: list[TimeSeriesAggregateCategory]
        """

        self._categories = categories

    @property
    def default_category(self):
        """Gets the default_category of this CategoricalVariable.  # noqa: E501


        :return: The default_category of this CategoricalVariable.  # noqa: E501
        :rtype: OneOfTimeSeriesDefaultCategory
        """
        return self._default_category

    @default_category.setter
    def default_category(self, default_category):
        """Sets the default_category of this CategoricalVariable.


        :param default_category: The default_category of this CategoricalVariable.  # noqa: E501
        :type: OneOfTimeSeriesDefaultCategory
        """

        self._default_category = default_category

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
        if not isinstance(other, CategoricalVariable):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CategoricalVariable):
            return True

        return self.to_dict() != other.to_dict()
