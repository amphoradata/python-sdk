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


class OrganisationAllOf(object):
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
        'name': 'str',
        'about': 'str',
        'website_url': 'str',
        'address': 'str'
    }

    attribute_map = {
        'name': 'name',
        'about': 'about',
        'website_url': 'websiteUrl',
        'address': 'address'
    }

    def __init__(self,
                 name=None,
                 about=None,
                 website_url=None,
                 address=None,
                 local_vars_configuration=None):  # noqa: E501
        """OrganisationAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._about = None
        self._website_url = None
        self._address = None
        self.discriminator = None

        self.name = name
        self.about = about
        self.website_url = website_url
        self.address = address

    @property
    def name(self):
        """Gets the name of this OrganisationAllOf.  # noqa: E501


        :return: The name of this OrganisationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganisationAllOf.


        :param name: The name of this OrganisationAllOf.  # noqa: E501
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
    def about(self):
        """Gets the about of this OrganisationAllOf.  # noqa: E501


        :return: The about of this OrganisationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._about

    @about.setter
    def about(self, about):
        """Sets the about of this OrganisationAllOf.


        :param about: The about of this OrganisationAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and about is None:  # noqa: E501
            raise ValueError(
                "Invalid value for `about`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation
                and about is not None and len(about) < 1):
            raise ValueError(
                "Invalid value for `about`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._about = about

    @property
    def website_url(self):
        """Gets the website_url of this OrganisationAllOf.  # noqa: E501


        :return: The website_url of this OrganisationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._website_url

    @website_url.setter
    def website_url(self, website_url):
        """Sets the website_url of this OrganisationAllOf.


        :param website_url: The website_url of this OrganisationAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and website_url is None:  # noqa: E501
            raise ValueError(
                "Invalid value for `website_url`, must not be `None`"
            )  # noqa: E501
        if (self.local_vars_configuration.client_side_validation
                and website_url is not None and len(website_url) < 1):
            raise ValueError(
                "Invalid value for `website_url`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._website_url = website_url

    @property
    def address(self):
        """Gets the address of this OrganisationAllOf.  # noqa: E501


        :return: The address of this OrganisationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this OrganisationAllOf.


        :param address: The address of this OrganisationAllOf.  # noqa: E501
        :type: str
        """

        self._address = address

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
        if not isinstance(other, OrganisationAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganisationAllOf):
            return True

        return self.to_dict() != other.to_dict()
