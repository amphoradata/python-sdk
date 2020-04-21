# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.9.6
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class CreateAmphora(object):
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
        'is_deleted': 'bool',
        'created_date': 'datetime',
        'name': 'str',
        'price': 'float',
        'labels': 'str',
        'description': 'str',
        'lat': 'float',
        'lon': 'float',
        'terms_and_conditions_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'is_deleted': 'isDeleted',
        'created_date': 'createdDate',
        'name': 'name',
        'price': 'price',
        'labels': 'labels',
        'description': 'description',
        'lat': 'lat',
        'lon': 'lon',
        'terms_and_conditions_id': 'termsAndConditionsId'
    }

    def __init__(self, id=None, is_deleted=None, created_date=None, name=None, price=None, labels=None, description=None, lat=None, lon=None, terms_and_conditions_id=None, local_vars_configuration=None):  # noqa: E501
        """CreateAmphora - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._is_deleted = None
        self._created_date = None
        self._name = None
        self._price = None
        self._labels = None
        self._description = None
        self._lat = None
        self._lon = None
        self._terms_and_conditions_id = None
        self.discriminator = None

        self.id = id
        self.is_deleted = is_deleted
        self.created_date = created_date
        self.name = name
        self.price = price
        self.labels = labels
        self.description = description
        self.lat = lat
        self.lon = lon
        self.terms_and_conditions_id = terms_and_conditions_id

    @property
    def id(self):
        """Gets the id of this CreateAmphora.  # noqa: E501


        :return: The id of this CreateAmphora.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateAmphora.


        :param id: The id of this CreateAmphora.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_deleted(self):
        """Gets the is_deleted of this CreateAmphora.  # noqa: E501


        :return: The is_deleted of this CreateAmphora.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this CreateAmphora.


        :param is_deleted: The is_deleted of this CreateAmphora.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def created_date(self):
        """Gets the created_date of this CreateAmphora.  # noqa: E501


        :return: The created_date of this CreateAmphora.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this CreateAmphora.


        :param created_date: The created_date of this CreateAmphora.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def name(self):
        """Gets the name of this CreateAmphora.  # noqa: E501


        :return: The name of this CreateAmphora.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAmphora.


        :param name: The name of this CreateAmphora.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def price(self):
        """Gets the price of this CreateAmphora.  # noqa: E501


        :return: The price of this CreateAmphora.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this CreateAmphora.


        :param price: The price of this CreateAmphora.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and price is None:  # noqa: E501
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def labels(self):
        """Gets the labels of this CreateAmphora.  # noqa: E501


        :return: The labels of this CreateAmphora.  # noqa: E501
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this CreateAmphora.


        :param labels: The labels of this CreateAmphora.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                labels is not None and not re.search(r'^(([-\w ]{0,12})[, ]?){1,6}$', labels)):  # noqa: E501
            raise ValueError(r"Invalid value for `labels`, must be a follow pattern or equal to `/^(([-\w ]{0,12})[, ]?){1,6}$/`")  # noqa: E501

        self._labels = labels

    @property
    def description(self):
        """Gets the description of this CreateAmphora.  # noqa: E501


        :return: The description of this CreateAmphora.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateAmphora.


        :param description: The description of this CreateAmphora.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def lat(self):
        """Gets the lat of this CreateAmphora.  # noqa: E501


        :return: The lat of this CreateAmphora.  # noqa: E501
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this CreateAmphora.


        :param lat: The lat of this CreateAmphora.  # noqa: E501
        :type: float
        """

        self._lat = lat

    @property
    def lon(self):
        """Gets the lon of this CreateAmphora.  # noqa: E501


        :return: The lon of this CreateAmphora.  # noqa: E501
        :rtype: float
        """
        return self._lon

    @lon.setter
    def lon(self, lon):
        """Sets the lon of this CreateAmphora.


        :param lon: The lon of this CreateAmphora.  # noqa: E501
        :type: float
        """

        self._lon = lon

    @property
    def terms_and_conditions_id(self):
        """Gets the terms_and_conditions_id of this CreateAmphora.  # noqa: E501


        :return: The terms_and_conditions_id of this CreateAmphora.  # noqa: E501
        :rtype: str
        """
        return self._terms_and_conditions_id

    @terms_and_conditions_id.setter
    def terms_and_conditions_id(self, terms_and_conditions_id):
        """Sets the terms_and_conditions_id of this CreateAmphora.


        :param terms_and_conditions_id: The terms_and_conditions_id of this CreateAmphora.  # noqa: E501
        :type: str
        """

        self._terms_and_conditions_id = terms_and_conditions_id

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
        if not isinstance(other, CreateAmphora):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateAmphora):
            return True

        return self.to_dict() != other.to_dict()
