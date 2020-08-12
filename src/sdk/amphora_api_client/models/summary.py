# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.16
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


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
        'num_results': 'int',
        'total_results': 'int',
        'fuzzy_level': 'int'
    }

    attribute_map = {
        'query': 'query',
        'query_type': 'queryType',
        'num_results': 'numResults',
        'total_results': 'totalResults',
        'fuzzy_level': 'fuzzyLevel'
    }

    def __init__(self,
                 query=None,
                 query_type=None,
                 num_results=None,
                 total_results=None,
                 fuzzy_level=None,
                 local_vars_configuration=None):  # noqa: E501
        """Summary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._query = None
        self._query_type = None
        self._num_results = None
        self._total_results = None
        self._fuzzy_level = None
        self.discriminator = None

        self.query = query
        self.query_type = query_type
        if num_results is not None:
            self.num_results = num_results
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
        if not isinstance(other, Summary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Summary):
            return True

        return self.to_dict() != other.to_dict()
