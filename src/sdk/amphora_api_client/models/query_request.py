# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.26
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class QueryRequest(object):
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
        'get_events': 'OneOfGetEvents',
        'get_series': 'OneOfGetSeries',
        'aggregate_series': 'OneOfAggregateSeries'
    }

    attribute_map = {
        'get_events': 'getEvents',
        'get_series': 'getSeries',
        'aggregate_series': 'aggregateSeries'
    }

    def __init__(self,
                 get_events=None,
                 get_series=None,
                 aggregate_series=None,
                 local_vars_configuration=None):  # noqa: E501
        """QueryRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._get_events = None
        self._get_series = None
        self._aggregate_series = None
        self.discriminator = None

        self.get_events = get_events
        self.get_series = get_series
        self.aggregate_series = aggregate_series

    @property
    def get_events(self):
        """Gets the get_events of this QueryRequest.  # noqa: E501


        :return: The get_events of this QueryRequest.  # noqa: E501
        :rtype: OneOfGetEvents
        """
        return self._get_events

    @get_events.setter
    def get_events(self, get_events):
        """Sets the get_events of this QueryRequest.


        :param get_events: The get_events of this QueryRequest.  # noqa: E501
        :type: OneOfGetEvents
        """

        self._get_events = get_events

    @property
    def get_series(self):
        """Gets the get_series of this QueryRequest.  # noqa: E501


        :return: The get_series of this QueryRequest.  # noqa: E501
        :rtype: OneOfGetSeries
        """
        return self._get_series

    @get_series.setter
    def get_series(self, get_series):
        """Sets the get_series of this QueryRequest.


        :param get_series: The get_series of this QueryRequest.  # noqa: E501
        :type: OneOfGetSeries
        """

        self._get_series = get_series

    @property
    def aggregate_series(self):
        """Gets the aggregate_series of this QueryRequest.  # noqa: E501


        :return: The aggregate_series of this QueryRequest.  # noqa: E501
        :rtype: OneOfAggregateSeries
        """
        return self._aggregate_series

    @aggregate_series.setter
    def aggregate_series(self, aggregate_series):
        """Sets the aggregate_series of this QueryRequest.


        :param aggregate_series: The aggregate_series of this QueryRequest.  # noqa: E501
        :type: OneOfAggregateSeries
        """

        self._aggregate_series = aggregate_series

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
        if not isinstance(other, QueryRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryRequest):
            return True

        return self.to_dict() != other.to_dict()
