# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.21
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class FuzzySearchResponse(object):
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
    openapi_types = {'summary': 'OneOfSummary', 'results': 'list[Result]'}

    attribute_map = {'summary': 'summary', 'results': 'results'}

    def __init__(self,
                 summary=None,
                 results=None,
                 local_vars_configuration=None):  # noqa: E501
        """FuzzySearchResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._summary = None
        self._results = None
        self.discriminator = None

        self.summary = summary
        self.results = results

    @property
    def summary(self):
        """Gets the summary of this FuzzySearchResponse.  # noqa: E501


        :return: The summary of this FuzzySearchResponse.  # noqa: E501
        :rtype: OneOfSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this FuzzySearchResponse.


        :param summary: The summary of this FuzzySearchResponse.  # noqa: E501
        :type: OneOfSummary
        """

        self._summary = summary

    @property
    def results(self):
        """Gets the results of this FuzzySearchResponse.  # noqa: E501


        :return: The results of this FuzzySearchResponse.  # noqa: E501
        :rtype: list[Result]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this FuzzySearchResponse.


        :param results: The results of this FuzzySearchResponse.  # noqa: E501
        :type: list[Result]
        """

        self._results = results

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
        if not isinstance(other, FuzzySearchResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FuzzySearchResponse):
            return True

        return self.to_dict() != other.to_dict()
