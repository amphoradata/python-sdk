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


class AllAccessRule(object):
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
    openapi_types = {'id': 'str', 'allow_or_deny': 'str', 'priority': 'int'}

    attribute_map = {
        'id': 'id',
        'allow_or_deny': 'allowOrDeny',
        'priority': 'priority'
    }

    def __init__(self,
                 id=None,
                 allow_or_deny=None,
                 priority=None,
                 local_vars_configuration=None):  # noqa: E501
        """AllAccessRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._allow_or_deny = None
        self._priority = None
        self.discriminator = None

        self.id = id
        self.allow_or_deny = allow_or_deny
        if priority is not None:
            self.priority = priority

    @property
    def id(self):
        """Gets the id of this AllAccessRule.  # noqa: E501


        :return: The id of this AllAccessRule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AllAccessRule.


        :param id: The id of this AllAccessRule.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def allow_or_deny(self):
        """Gets the allow_or_deny of this AllAccessRule.  # noqa: E501


        :return: The allow_or_deny of this AllAccessRule.  # noqa: E501
        :rtype: str
        """
        return self._allow_or_deny

    @allow_or_deny.setter
    def allow_or_deny(self, allow_or_deny):
        """Sets the allow_or_deny of this AllAccessRule.


        :param allow_or_deny: The allow_or_deny of this AllAccessRule.  # noqa: E501
        :type: str
        """

        self._allow_or_deny = allow_or_deny

    @property
    def priority(self):
        """Gets the priority of this AllAccessRule.  # noqa: E501


        :return: The priority of this AllAccessRule.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this AllAccessRule.


        :param priority: The priority of this AllAccessRule.  # noqa: E501
        :type: int
        """

        self._priority = priority

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
        if not isinstance(other, AllAccessRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AllAccessRule):
            return True

        return self.to_dict() != other.to_dict()
