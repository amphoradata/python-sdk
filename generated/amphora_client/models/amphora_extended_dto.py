# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.0.2
    Contact: rian@amphoradata.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AmphoraExtendedDto(object):
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
        'id': 'str',
        'organisation_id': 'str',
        'description': 'str',
        'lat': 'float',
        'lon': 'float',
        'name': 'str',
        'price': 'float'
    }

    attribute_map = {
        'id': 'id',
        'organisation_id': 'organisationId',
        'description': 'description',
        'lat': 'lat',
        'lon': 'lon',
        'name': 'name',
        'price': 'price'
    }

    def __init__(self, id=None, organisation_id=None, description=None, lat=None, lon=None, name=None, price=None):  # noqa: E501
        """AmphoraExtendedDto - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._organisation_id = None
        self._description = None
        self._lat = None
        self._lon = None
        self._name = None
        self._price = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if organisation_id is not None:
            self.organisation_id = organisation_id
        self.description = description
        self.lat = lat
        self.lon = lon
        self.name = name
        self.price = price

    @property
    def id(self):
        """Gets the id of this AmphoraExtendedDto.  # noqa: E501


        :return: The id of this AmphoraExtendedDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AmphoraExtendedDto.


        :param id: The id of this AmphoraExtendedDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def organisation_id(self):
        """Gets the organisation_id of this AmphoraExtendedDto.  # noqa: E501


        :return: The organisation_id of this AmphoraExtendedDto.  # noqa: E501
        :rtype: str
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this AmphoraExtendedDto.


        :param organisation_id: The organisation_id of this AmphoraExtendedDto.  # noqa: E501
        :type: str
        """

        self._organisation_id = organisation_id

    @property
    def description(self):
        """Gets the description of this AmphoraExtendedDto.  # noqa: E501


        :return: The description of this AmphoraExtendedDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AmphoraExtendedDto.


        :param description: The description of this AmphoraExtendedDto.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def lat(self):
        """Gets the lat of this AmphoraExtendedDto.  # noqa: E501


        :return: The lat of this AmphoraExtendedDto.  # noqa: E501
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this AmphoraExtendedDto.


        :param lat: The lat of this AmphoraExtendedDto.  # noqa: E501
        :type: float
        """

        self._lat = lat

    @property
    def lon(self):
        """Gets the lon of this AmphoraExtendedDto.  # noqa: E501


        :return: The lon of this AmphoraExtendedDto.  # noqa: E501
        :rtype: float
        """
        return self._lon

    @lon.setter
    def lon(self, lon):
        """Sets the lon of this AmphoraExtendedDto.


        :param lon: The lon of this AmphoraExtendedDto.  # noqa: E501
        :type: float
        """

        self._lon = lon

    @property
    def name(self):
        """Gets the name of this AmphoraExtendedDto.  # noqa: E501


        :return: The name of this AmphoraExtendedDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AmphoraExtendedDto.


        :param name: The name of this AmphoraExtendedDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def price(self):
        """Gets the price of this AmphoraExtendedDto.  # noqa: E501


        :return: The price of this AmphoraExtendedDto.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this AmphoraExtendedDto.


        :param price: The price of this AmphoraExtendedDto.  # noqa: E501
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

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
        if not isinstance(other, AmphoraExtendedDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
