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


class TermsOfUse(object):
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
    openapi_types = {'name': 'str', 'contents': 'str', 'id': 'str'}

    attribute_map = {'name': 'name', 'contents': 'contents', 'id': 'id'}

    def __init__(self,
                 name=None,
                 contents=None,
                 id=None,
                 local_vars_configuration=None):  # noqa: E501
        """TermsOfUse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._contents = None
        self._id = None
        self.discriminator = None

        self.name = name
        self.contents = contents
        self.id = id

    @property
    def name(self):
        """Gets the name of this TermsOfUse.  # noqa: E501


        :return: The name of this TermsOfUse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TermsOfUse.


        :param name: The name of this TermsOfUse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError(
                "Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation
                and name is not None and len(name) < 1):
            raise ValueError(
                "Invalid value for `name`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._name = name

    @property
    def contents(self):
        """Gets the contents of this TermsOfUse.  # noqa: E501


        :return: The contents of this TermsOfUse.  # noqa: E501
        :rtype: str
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this TermsOfUse.


        :param contents: The contents of this TermsOfUse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and contents is None:  # noqa: E501
            raise ValueError("Invalid value for `contents`, must not be `None`"
                             )  # noqa: E501
        if (self.local_vars_configuration.client_side_validation
                and contents is not None and len(contents) < 1):
            raise ValueError(
                "Invalid value for `contents`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._contents = contents

    @property
    def id(self):
        """Gets the id of this TermsOfUse.  # noqa: E501


        :return: The id of this TermsOfUse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TermsOfUse.


        :param id: The id of this TermsOfUse.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, TermsOfUse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TermsOfUse):
            return True

        return self.to_dict() != other.to_dict()
