# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.25
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class PermissionsRequest(object):
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
    openapi_types = {'access_queries': 'list[AccessLevelQuery]'}

    attribute_map = {'access_queries': 'accessQueries'}

    def __init__(self,
                 access_queries=None,
                 local_vars_configuration=None):  # noqa: E501
        """PermissionsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_queries = None
        self.discriminator = None

        self.access_queries = access_queries

    @property
    def access_queries(self):
        """Gets the access_queries of this PermissionsRequest.  # noqa: E501


        :return: The access_queries of this PermissionsRequest.  # noqa: E501
        :rtype: list[AccessLevelQuery]
        """
        return self._access_queries

    @access_queries.setter
    def access_queries(self, access_queries):
        """Sets the access_queries of this PermissionsRequest.


        :param access_queries: The access_queries of this PermissionsRequest.  # noqa: E501
        :type: list[AccessLevelQuery]
        """

        self._access_queries = access_queries

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
        if not isinstance(other, PermissionsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PermissionsRequest):
            return True

        return self.to_dict() != other.to_dict()
