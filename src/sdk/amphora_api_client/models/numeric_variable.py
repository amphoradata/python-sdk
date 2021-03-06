# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.29
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class NumericVariable(object):
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
        'aggregation': 'OneOfTsx',
        'kind': 'str'
    }

    attribute_map = {
        'filter': 'filter',
        'value': 'value',
        'interpolation': 'interpolation',
        'aggregation': 'aggregation',
        'kind': 'Kind'
    }

    def __init__(self,
                 filter=None,
                 value=None,
                 interpolation=None,
                 aggregation=None,
                 kind=None,
                 local_vars_configuration=None):  # noqa: E501
        """NumericVariable - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._filter = None
        self._value = None
        self._interpolation = None
        self._aggregation = None
        self._kind = None
        self.discriminator = None

        self.filter = filter
        self.value = value
        self.interpolation = interpolation
        self.aggregation = aggregation
        self.kind = kind

    @property
    def filter(self):
        """Gets the filter of this NumericVariable.  # noqa: E501


        :return: The filter of this NumericVariable.  # noqa: E501
        :rtype: OneOfTsx
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this NumericVariable.


        :param filter: The filter of this NumericVariable.  # noqa: E501
        :type: OneOfTsx
        """

        self._filter = filter

    @property
    def value(self):
        """Gets the value of this NumericVariable.  # noqa: E501


        :return: The value of this NumericVariable.  # noqa: E501
        :rtype: OneOfTsx
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this NumericVariable.


        :param value: The value of this NumericVariable.  # noqa: E501
        :type: OneOfTsx
        """

        self._value = value

    @property
    def interpolation(self):
        """Gets the interpolation of this NumericVariable.  # noqa: E501


        :return: The interpolation of this NumericVariable.  # noqa: E501
        :rtype: OneOfInterpolation
        """
        return self._interpolation

    @interpolation.setter
    def interpolation(self, interpolation):
        """Sets the interpolation of this NumericVariable.


        :param interpolation: The interpolation of this NumericVariable.  # noqa: E501
        :type: OneOfInterpolation
        """

        self._interpolation = interpolation

    @property
    def aggregation(self):
        """Gets the aggregation of this NumericVariable.  # noqa: E501


        :return: The aggregation of this NumericVariable.  # noqa: E501
        :rtype: OneOfTsx
        """
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation):
        """Sets the aggregation of this NumericVariable.


        :param aggregation: The aggregation of this NumericVariable.  # noqa: E501
        :type: OneOfTsx
        """

        self._aggregation = aggregation

    @property
    def kind(self):
        """Gets the kind of this NumericVariable.  # noqa: E501

        Should be set to numeric  # noqa: E501

        :return: The kind of this NumericVariable.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this NumericVariable.

        Should be set to numeric  # noqa: E501

        :param kind: The kind of this NumericVariable.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and kind is None:  # noqa: E501
            raise ValueError(
                "Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

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
        if not isinstance(other, NumericVariable):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NumericVariable):
            return True

        return self.to_dict() != other.to_dict()
