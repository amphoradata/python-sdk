# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.7.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from amphora_client.configuration import Configuration


class Summary(object):
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
        'query': 'str',
        'query_type': 'str',
        'query_time': 'int',
        'num_results': 'int',
        'offset': 'int',
        'total_results': 'int',
        'fuzzy_level': 'int'
    }

    attribute_map = {
        'query': 'query',
        'query_type': 'queryType',
        'query_time': 'queryTime',
        'num_results': 'numResults',
        'offset': 'offset',
        'total_results': 'totalResults',
        'fuzzy_level': 'fuzzyLevel'
    }

    def __init__(self, query=None, query_type=None, query_time=None, num_results=None, offset=None, total_results=None, fuzzy_level=None, local_vars_configuration=None):  # noqa: E501
        """Summary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._query = None
        self._query_type = None
        self._query_time = None
        self._num_results = None
        self._offset = None
        self._total_results = None
        self._fuzzy_level = None
        self.discriminator = None

        self.query = query
        self.query_type = query_type
        if query_time is not None:
            self.query_time = query_time
        if num_results is not None:
            self.num_results = num_results
        if offset is not None:
            self.offset = offset
        if total_results is not None:
            self.total_results = total_results
        if fuzzy_level is not None:
            self.fuzzy_level = fuzzy_level

    @property
    def query(self):
        """Gets the query of this Summary.  # noqa: E501


        :return: The query of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this Summary.


        :param query: The query of this Summary.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def query_type(self):
        """Gets the query_type of this Summary.  # noqa: E501


        :return: The query_type of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this Summary.


        :param query_type: The query_type of this Summary.  # noqa: E501
        :type: str
        """

        self._query_type = query_type

    @property
    def query_time(self):
        """Gets the query_time of this Summary.  # noqa: E501


        :return: The query_time of this Summary.  # noqa: E501
        :rtype: int
        """
        return self._query_time

    @query_time.setter
    def query_time(self, query_time):
        """Sets the query_time of this Summary.


        :param query_time: The query_time of this Summary.  # noqa: E501
        :type: int
        """

        self._query_time = query_time

    @property
    def num_results(self):
        """Gets the num_results of this Summary.  # noqa: E501


        :return: The num_results of this Summary.  # noqa: E501
        :rtype: int
        """
        return self._num_results

    @num_results.setter
    def num_results(self, num_results):
        """Sets the num_results of this Summary.


        :param num_results: The num_results of this Summary.  # noqa: E501
        :type: int
        """

        self._num_results = num_results

    @property
    def offset(self):
        """Gets the offset of this Summary.  # noqa: E501


        :return: The offset of this Summary.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this Summary.


        :param offset: The offset of this Summary.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def total_results(self):
        """Gets the total_results of this Summary.  # noqa: E501


        :return: The total_results of this Summary.  # noqa: E501
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this Summary.


        :param total_results: The total_results of this Summary.  # noqa: E501
        :type: int
        """

        self._total_results = total_results

    @property
    def fuzzy_level(self):
        """Gets the fuzzy_level of this Summary.  # noqa: E501


        :return: The fuzzy_level of this Summary.  # noqa: E501
        :rtype: int
        """
        return self._fuzzy_level

    @fuzzy_level.setter
    def fuzzy_level(self, fuzzy_level):
        """Sets the fuzzy_level of this Summary.


        :param fuzzy_level: The fuzzy_level of this Summary.  # noqa: E501
        :type: int
        """

        self._fuzzy_level = fuzzy_level

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
        if not isinstance(other, Summary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Summary):
            return True

        return self.to_dict() != other.to_dict()
