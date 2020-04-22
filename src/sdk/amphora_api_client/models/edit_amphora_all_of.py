# coding: utf-8
"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.9.7
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class EditAmphoraAllOf(object):
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
        'description': 'str',
        'lat': 'float',
        'lon': 'float',
        'terms_and_conditions_id': 'str',
        'file_attributes': 'dict(str, AttributeStore)'
    }

    attribute_map = {
        'description': 'description',
        'lat': 'lat',
        'lon': 'lon',
        'terms_and_conditions_id': 'termsAndConditionsId',
        'file_attributes': 'fileAttributes'
    }

    def __init__(self,
                 description=None,
                 lat=None,
                 lon=None,
                 terms_and_conditions_id=None,
                 file_attributes=None,
                 local_vars_configuration=None):  # noqa: E501
        """EditAmphoraAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._lat = None
        self._lon = None
        self._terms_and_conditions_id = None
        self._file_attributes = None
        self.discriminator = None

        self.description = description
        self.lat = lat
        self.lon = lon
        self.terms_and_conditions_id = terms_and_conditions_id
        self.file_attributes = file_attributes

    @property
    def description(self):
        """Gets the description of this EditAmphoraAllOf.  # noqa: E501


        :return: The description of this EditAmphoraAllOf.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EditAmphoraAllOf.


        :param description: The description of this EditAmphoraAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError(
                "Invalid value for `description`, must not be `None`"
            )  # noqa: E501
        if (self.local_vars_configuration.client_side_validation
                and description is not None and len(description) < 1):
            raise ValueError(
                "Invalid value for `description`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._description = description

    @property
    def lat(self):
        """Gets the lat of this EditAmphoraAllOf.  # noqa: E501


        :return: The lat of this EditAmphoraAllOf.  # noqa: E501
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this EditAmphoraAllOf.


        :param lat: The lat of this EditAmphoraAllOf.  # noqa: E501
        :type: float
        """

        self._lat = lat

    @property
    def lon(self):
        """Gets the lon of this EditAmphoraAllOf.  # noqa: E501


        :return: The lon of this EditAmphoraAllOf.  # noqa: E501
        :rtype: float
        """
        return self._lon

    @lon.setter
    def lon(self, lon):
        """Sets the lon of this EditAmphoraAllOf.


        :param lon: The lon of this EditAmphoraAllOf.  # noqa: E501
        :type: float
        """

        self._lon = lon

    @property
    def terms_and_conditions_id(self):
        """Gets the terms_and_conditions_id of this EditAmphoraAllOf.  # noqa: E501


        :return: The terms_and_conditions_id of this EditAmphoraAllOf.  # noqa: E501
        :rtype: str
        """
        return self._terms_and_conditions_id

    @terms_and_conditions_id.setter
    def terms_and_conditions_id(self, terms_and_conditions_id):
        """Sets the terms_and_conditions_id of this EditAmphoraAllOf.


        :param terms_and_conditions_id: The terms_and_conditions_id of this EditAmphoraAllOf.  # noqa: E501
        :type: str
        """

        self._terms_and_conditions_id = terms_and_conditions_id

    @property
    def file_attributes(self):
        """Gets the file_attributes of this EditAmphoraAllOf.  # noqa: E501


        :return: The file_attributes of this EditAmphoraAllOf.  # noqa: E501
        :rtype: dict(str, AttributeStore)
        """
        return self._file_attributes

    @file_attributes.setter
    def file_attributes(self, file_attributes):
        """Sets the file_attributes of this EditAmphoraAllOf.


        :param file_attributes: The file_attributes of this EditAmphoraAllOf.  # noqa: E501
        :type: dict(str, AttributeStore)
        """

        self._file_attributes = file_attributes

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
        if not isinstance(other, EditAmphoraAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EditAmphoraAllOf):
            return True

        return self.to_dict() != other.to_dict()
