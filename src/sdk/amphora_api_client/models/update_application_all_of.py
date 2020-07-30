# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.14
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class UpdateApplicationAllOf(object):
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
    openapi_types = {'id': 'str', 'locations': 'list[CreateAppLocation]'}

    attribute_map = {'id': 'id', 'locations': 'locations'}

    def __init__(self,
                 id=None,
                 locations=None,
                 local_vars_configuration=None):  # noqa: E501
        """UpdateApplicationAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._locations = None
        self.discriminator = None

        self.id = id
        self.locations = locations

    @property
    def id(self):
        """Gets the id of this UpdateApplicationAllOf.  # noqa: E501


        :return: The id of this UpdateApplicationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateApplicationAllOf.


        :param id: The id of this UpdateApplicationAllOf.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def locations(self):
        """Gets the locations of this UpdateApplicationAllOf.  # noqa: E501

        Gets or sets a collection of locations your application will run.  # noqa: E501

        :return: The locations of this UpdateApplicationAllOf.  # noqa: E501
        :rtype: list[CreateAppLocation]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this UpdateApplicationAllOf.

        Gets or sets a collection of locations your application will run.  # noqa: E501

        :param locations: The locations of this UpdateApplicationAllOf.  # noqa: E501
        :type: list[CreateAppLocation]
        """

        self._locations = locations

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
        if not isinstance(other, UpdateApplicationAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateApplicationAllOf):
            return True

        return self.to_dict() != other.to_dict()
