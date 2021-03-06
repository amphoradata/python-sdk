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


class GetSeries(object):
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
        'projected_variables': 'list[str]',
        'inline_variables': 'dict(str, Variable)',
        'take': 'int'
    }

    attribute_map = {
        'time_series_id': 'timeSeriesId',
        'search_span': 'searchSpan',
        'filter': 'filter',
        'projected_variables': 'projectedVariables',
        'inline_variables': 'inlineVariables',
        'take': 'take'
    }

    def __init__(self,
                 time_series_id=None,
                 search_span=None,
                 filter=None,
                 projected_variables=None,
                 inline_variables=None,
                 take=None,
                 local_vars_configuration=None):  # noqa: E501
        """GetSeries - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._time_series_id = None
        self._search_span = None
        self._filter = None
        self._projected_variables = None
        self._inline_variables = None
        self._take = None
        self.discriminator = None

        self.time_series_id = time_series_id
        self.search_span = search_span
        self.filter = filter
        self.projected_variables = projected_variables
        self.inline_variables = inline_variables
        self.take = take

    @property
    def time_series_id(self):
        """Gets the time_series_id of this GetSeries.  # noqa: E501


        :return: The time_series_id of this GetSeries.  # noqa: E501
        :rtype: list[object]
        """
        return self._time_series_id

    @time_series_id.setter
    def time_series_id(self, time_series_id):
        """Sets the time_series_id of this GetSeries.


        :param time_series_id: The time_series_id of this GetSeries.  # noqa: E501
        :type: list[object]
        """

        self._time_series_id = time_series_id

    @property
    def search_span(self):
        """Gets the search_span of this GetSeries.  # noqa: E501


        :return: The search_span of this GetSeries.  # noqa: E501
        :rtype: OneOfDateTimeRange
        """
        return self._search_span

    @search_span.setter
    def search_span(self, search_span):
        """Sets the search_span of this GetSeries.


        :param search_span: The search_span of this GetSeries.  # noqa: E501
        :type: OneOfDateTimeRange
        """

        self._search_span = search_span

    @property
    def filter(self):
        """Gets the filter of this GetSeries.  # noqa: E501


        :return: The filter of this GetSeries.  # noqa: E501
        :rtype: OneOfTsx
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this GetSeries.


        :param filter: The filter of this GetSeries.  # noqa: E501
        :type: OneOfTsx
        """

        self._filter = filter

    @property
    def projected_variables(self):
        """Gets the projected_variables of this GetSeries.  # noqa: E501


        :return: The projected_variables of this GetSeries.  # noqa: E501
        :rtype: list[str]
        """
        return self._projected_variables

    @projected_variables.setter
    def projected_variables(self, projected_variables):
        """Sets the projected_variables of this GetSeries.


        :param projected_variables: The projected_variables of this GetSeries.  # noqa: E501
        :type: list[str]
        """

        self._projected_variables = projected_variables

    @property
    def inline_variables(self):
        """Gets the inline_variables of this GetSeries.  # noqa: E501


        :return: The inline_variables of this GetSeries.  # noqa: E501
        :rtype: dict(str, Variable)
        """
        return self._inline_variables

    @inline_variables.setter
    def inline_variables(self, inline_variables):
        """Sets the inline_variables of this GetSeries.


        :param inline_variables: The inline_variables of this GetSeries.  # noqa: E501
        :type: dict(str, Variable)
        """

        self._inline_variables = inline_variables

    @property
    def take(self):
        """Gets the take of this GetSeries.  # noqa: E501


        :return: The take of this GetSeries.  # noqa: E501
        :rtype: int
        """
        return self._take

    @take.setter
    def take(self, take):
        """Sets the take of this GetSeries.


        :param take: The take of this GetSeries.  # noqa: E501
        :type: int
        """

        self._take = take

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
        if not isinstance(other, GetSeries):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetSeries):
            return True

        return self.to_dict() != other.to_dict()
