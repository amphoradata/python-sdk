# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.1.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class GetEvents(object):
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
        'time_series_id': 'list[object]',
        'search_span': 'OneOfDateTimeRange',
        'filter': 'OneOfTsx',
        'projected_properties': 'list[str]'
    }

    attribute_map = {
        'time_series_id': 'timeSeriesId',
        'search_span': 'searchSpan',
        'filter': 'filter',
        'projected_properties': 'projectedProperties'
    }

    def __init__(self, time_series_id=None, search_span=None, filter=None, projected_properties=None):  # noqa: E501
        """GetEvents - a model defined in OpenAPI"""  # noqa: E501

        self._time_series_id = None
        self._search_span = None
        self._filter = None
        self._projected_properties = None
        self.discriminator = None

        self.time_series_id = time_series_id
        self.search_span = search_span
        self.filter = filter
        self.projected_properties = projected_properties

    @property
    def time_series_id(self):
        """Gets the time_series_id of this GetEvents.  # noqa: E501


        :return: The time_series_id of this GetEvents.  # noqa: E501
        :rtype: list[object]
        """
        return self._time_series_id

    @time_series_id.setter
    def time_series_id(self, time_series_id):
        """Sets the time_series_id of this GetEvents.


        :param time_series_id: The time_series_id of this GetEvents.  # noqa: E501
        :type: list[object]
        """

        self._time_series_id = time_series_id

    @property
    def search_span(self):
        """Gets the search_span of this GetEvents.  # noqa: E501


        :return: The search_span of this GetEvents.  # noqa: E501
        :rtype: OneOfDateTimeRange
        """
        return self._search_span

    @search_span.setter
    def search_span(self, search_span):
        """Sets the search_span of this GetEvents.


        :param search_span: The search_span of this GetEvents.  # noqa: E501
        :type: OneOfDateTimeRange
        """

        self._search_span = search_span

    @property
    def filter(self):
        """Gets the filter of this GetEvents.  # noqa: E501


        :return: The filter of this GetEvents.  # noqa: E501
        :rtype: OneOfTsx
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this GetEvents.


        :param filter: The filter of this GetEvents.  # noqa: E501
        :type: OneOfTsx
        """

        self._filter = filter

    @property
    def projected_properties(self):
        """Gets the projected_properties of this GetEvents.  # noqa: E501


        :return: The projected_properties of this GetEvents.  # noqa: E501
        :rtype: list[str]
        """
        return self._projected_properties

    @projected_properties.setter
    def projected_properties(self, projected_properties):
        """Sets the projected_properties of this GetEvents.


        :param projected_properties: The projected_properties of this GetEvents.  # noqa: E501
        :type: list[str]
        """

        self._projected_properties = projected_properties

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
        if not isinstance(other, GetEvents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
