# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.2.0dev1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AmphoraExtendedDtoAllOf(object):
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
        'organisation_id': 'str',
        'terms_and_conditions_id': 'str',
        'description': 'str',
        'lat': 'float',
        'lon': 'float'
    }

    attribute_map = {
        'organisation_id': 'organisationId',
        'terms_and_conditions_id': 'termsAndConditionsId',
        'description': 'description',
        'lat': 'lat',
        'lon': 'lon'
    }

    def __init__(self, organisation_id=None, terms_and_conditions_id=None, description=None, lat=None, lon=None):  # noqa: E501
        """AmphoraExtendedDtoAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._organisation_id = None
        self._terms_and_conditions_id = None
        self._description = None
        self._lat = None
        self._lon = None
        self.discriminator = None

        self.organisation_id = organisation_id
        self.terms_and_conditions_id = terms_and_conditions_id
        self.description = description
        self.lat = lat
        self.lon = lon

    @property
    def organisation_id(self):
        """Gets the organisation_id of this AmphoraExtendedDtoAllOf.  # noqa: E501


        :return: The organisation_id of this AmphoraExtendedDtoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this AmphoraExtendedDtoAllOf.


        :param organisation_id: The organisation_id of this AmphoraExtendedDtoAllOf.  # noqa: E501
        :type: str
        """

        self._organisation_id = organisation_id

    @property
    def terms_and_conditions_id(self):
        """Gets the terms_and_conditions_id of this AmphoraExtendedDtoAllOf.  # noqa: E501


        :return: The terms_and_conditions_id of this AmphoraExtendedDtoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._terms_and_conditions_id

    @terms_and_conditions_id.setter
    def terms_and_conditions_id(self, terms_and_conditions_id):
        """Sets the terms_and_conditions_id of this AmphoraExtendedDtoAllOf.


        :param terms_and_conditions_id: The terms_and_conditions_id of this AmphoraExtendedDtoAllOf.  # noqa: E501
        :type: str
        """

        self._terms_and_conditions_id = terms_and_conditions_id

    @property
    def description(self):
        """Gets the description of this AmphoraExtendedDtoAllOf.  # noqa: E501


        :return: The description of this AmphoraExtendedDtoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AmphoraExtendedDtoAllOf.


        :param description: The description of this AmphoraExtendedDtoAllOf.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def lat(self):
        """Gets the lat of this AmphoraExtendedDtoAllOf.  # noqa: E501


        :return: The lat of this AmphoraExtendedDtoAllOf.  # noqa: E501
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this AmphoraExtendedDtoAllOf.


        :param lat: The lat of this AmphoraExtendedDtoAllOf.  # noqa: E501
        :type: float
        """

        self._lat = lat

    @property
    def lon(self):
        """Gets the lon of this AmphoraExtendedDtoAllOf.  # noqa: E501


        :return: The lon of this AmphoraExtendedDtoAllOf.  # noqa: E501
        :rtype: float
        """
        return self._lon

    @lon.setter
    def lon(self, lon):
        """Sets the lon of this AmphoraExtendedDtoAllOf.


        :param lon: The lon of this AmphoraExtendedDtoAllOf.  # noqa: E501
        :type: float
        """

        self._lon = lon

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
        if not isinstance(other, AmphoraExtendedDtoAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
