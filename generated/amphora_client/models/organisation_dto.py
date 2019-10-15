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


class OrganisationDto(object):
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
        'name': 'str',
        'about': 'str',
        'website_url': 'str',
        'address': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'about': 'about',
        'website_url': 'websiteUrl',
        'address': 'address'
    }

    def __init__(self, id=None, name=None, about=None, website_url=None, address=None):  # noqa: E501
        """OrganisationDto - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._about = None
        self._website_url = None
        self._address = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if about is not None:
            self.about = about
        if website_url is not None:
            self.website_url = website_url
        if address is not None:
            self.address = address

    @property
    def id(self):
        """Gets the id of this OrganisationDto.  # noqa: E501


        :return: The id of this OrganisationDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganisationDto.


        :param id: The id of this OrganisationDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this OrganisationDto.  # noqa: E501


        :return: The name of this OrganisationDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganisationDto.


        :param name: The name of this OrganisationDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def about(self):
        """Gets the about of this OrganisationDto.  # noqa: E501


        :return: The about of this OrganisationDto.  # noqa: E501
        :rtype: str
        """
        return self._about

    @about.setter
    def about(self, about):
        """Sets the about of this OrganisationDto.


        :param about: The about of this OrganisationDto.  # noqa: E501
        :type: str
        """

        self._about = about

    @property
    def website_url(self):
        """Gets the website_url of this OrganisationDto.  # noqa: E501


        :return: The website_url of this OrganisationDto.  # noqa: E501
        :rtype: str
        """
        return self._website_url

    @website_url.setter
    def website_url(self, website_url):
        """Sets the website_url of this OrganisationDto.


        :param website_url: The website_url of this OrganisationDto.  # noqa: E501
        :type: str
        """

        self._website_url = website_url

    @property
    def address(self):
        """Gets the address of this OrganisationDto.  # noqa: E501


        :return: The address of this OrganisationDto.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this OrganisationDto.


        :param address: The address of this OrganisationDto.  # noqa: E501
        :type: str
        """

        self._address = address

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
        if not isinstance(other, OrganisationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
