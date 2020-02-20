# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.7.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from amphora_client.configuration import Configuration


class Entity(object):
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
        'created_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'is_deleted': 'isDeleted',
        'created_date': 'createdDate'
    }

    def __init__(self, id=None, is_deleted=None, created_date=None, local_vars_configuration=None):  # noqa: E501
        """Entity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._is_deleted = None
        self._created_date = None
        self.discriminator = None

        self.id = id
        self.is_deleted = is_deleted
        self.created_date = created_date

    @property
    def id(self):
        """Gets the id of this Entity.  # noqa: E501


        :return: The id of this Entity.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Entity.


        :param id: The id of this Entity.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_deleted(self):
        """Gets the is_deleted of this Entity.  # noqa: E501


        :return: The is_deleted of this Entity.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this Entity.


        :param is_deleted: The is_deleted of this Entity.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def created_date(self):
        """Gets the created_date of this Entity.  # noqa: E501


        :return: The created_date of this Entity.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this Entity.


        :param created_date: The created_date of this Entity.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

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
        if not isinstance(other, Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Entity):
            return True

        return self.to_dict() != other.to_dict()
