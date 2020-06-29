# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.8
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class Address(object):
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
        'street_number': 'str',
        'street_name': 'str',
        'municipality_subdivision': 'str',
        'municipality': 'str',
        'country_secondary_subdivision': 'str',
        'country_subdivision': 'str',
        'postal_code': 'str',
        'country_code': 'str',
        'country': 'str',
        'country_code_iso3': 'str',
        'freeform_address': 'str',
        'local_name': 'str'
    }

    attribute_map = {
        'street_number': 'streetNumber',
        'street_name': 'streetName',
        'municipality_subdivision': 'municipalitySubdivision',
        'municipality': 'municipality',
        'country_secondary_subdivision': 'countrySecondarySubdivision',
        'country_subdivision': 'countrySubdivision',
        'postal_code': 'postalCode',
        'country_code': 'countryCode',
        'country': 'country',
        'country_code_iso3': 'countryCodeIso3',
        'freeform_address': 'freeformAddress',
        'local_name': 'localName'
    }

    def __init__(self,
                 street_number=None,
                 street_name=None,
                 municipality_subdivision=None,
                 municipality=None,
                 country_secondary_subdivision=None,
                 country_subdivision=None,
                 postal_code=None,
                 country_code=None,
                 country=None,
                 country_code_iso3=None,
                 freeform_address=None,
                 local_name=None,
                 local_vars_configuration=None):  # noqa: E501
        """Address - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._street_number = None
        self._street_name = None
        self._municipality_subdivision = None
        self._municipality = None
        self._country_secondary_subdivision = None
        self._country_subdivision = None
        self._postal_code = None
        self._country_code = None
        self._country = None
        self._country_code_iso3 = None
        self._freeform_address = None
        self._local_name = None
        self.discriminator = None

        self.street_number = street_number
        self.street_name = street_name
        self.municipality_subdivision = municipality_subdivision
        self.municipality = municipality
        self.country_secondary_subdivision = country_secondary_subdivision
        self.country_subdivision = country_subdivision
        self.postal_code = postal_code
        self.country_code = country_code
        self.country = country
        self.country_code_iso3 = country_code_iso3
        self.freeform_address = freeform_address
        self.local_name = local_name

    @property
    def street_number(self):
        """Gets the street_number of this Address.  # noqa: E501


        :return: The street_number of this Address.  # noqa: E501
        :rtype: str
        """
        return self._street_number

    @street_number.setter
    def street_number(self, street_number):
        """Sets the street_number of this Address.


        :param street_number: The street_number of this Address.  # noqa: E501
        :type: str
        """

        self._street_number = street_number

    @property
    def street_name(self):
        """Gets the street_name of this Address.  # noqa: E501


        :return: The street_name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """Sets the street_name of this Address.


        :param street_name: The street_name of this Address.  # noqa: E501
        :type: str
        """

        self._street_name = street_name

    @property
    def municipality_subdivision(self):
        """Gets the municipality_subdivision of this Address.  # noqa: E501


        :return: The municipality_subdivision of this Address.  # noqa: E501
        :rtype: str
        """
        return self._municipality_subdivision

    @municipality_subdivision.setter
    def municipality_subdivision(self, municipality_subdivision):
        """Sets the municipality_subdivision of this Address.


        :param municipality_subdivision: The municipality_subdivision of this Address.  # noqa: E501
        :type: str
        """

        self._municipality_subdivision = municipality_subdivision

    @property
    def municipality(self):
        """Gets the municipality of this Address.  # noqa: E501


        :return: The municipality of this Address.  # noqa: E501
        :rtype: str
        """
        return self._municipality

    @municipality.setter
    def municipality(self, municipality):
        """Sets the municipality of this Address.


        :param municipality: The municipality of this Address.  # noqa: E501
        :type: str
        """

        self._municipality = municipality

    @property
    def country_secondary_subdivision(self):
        """Gets the country_secondary_subdivision of this Address.  # noqa: E501


        :return: The country_secondary_subdivision of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country_secondary_subdivision

    @country_secondary_subdivision.setter
    def country_secondary_subdivision(self, country_secondary_subdivision):
        """Sets the country_secondary_subdivision of this Address.


        :param country_secondary_subdivision: The country_secondary_subdivision of this Address.  # noqa: E501
        :type: str
        """

        self._country_secondary_subdivision = country_secondary_subdivision

    @property
    def country_subdivision(self):
        """Gets the country_subdivision of this Address.  # noqa: E501


        :return: The country_subdivision of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country_subdivision

    @country_subdivision.setter
    def country_subdivision(self, country_subdivision):
        """Sets the country_subdivision of this Address.


        :param country_subdivision: The country_subdivision of this Address.  # noqa: E501
        :type: str
        """

        self._country_subdivision = country_subdivision

    @property
    def postal_code(self):
        """Gets the postal_code of this Address.  # noqa: E501


        :return: The postal_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Address.


        :param postal_code: The postal_code of this Address.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country_code(self):
        """Gets the country_code of this Address.  # noqa: E501


        :return: The country_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Address.


        :param country_code: The country_code of this Address.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def country(self):
        """Gets the country of this Address.  # noqa: E501


        :return: The country of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Address.


        :param country: The country of this Address.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def country_code_iso3(self):
        """Gets the country_code_iso3 of this Address.  # noqa: E501


        :return: The country_code_iso3 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country_code_iso3

    @country_code_iso3.setter
    def country_code_iso3(self, country_code_iso3):
        """Sets the country_code_iso3 of this Address.


        :param country_code_iso3: The country_code_iso3 of this Address.  # noqa: E501
        :type: str
        """

        self._country_code_iso3 = country_code_iso3

    @property
    def freeform_address(self):
        """Gets the freeform_address of this Address.  # noqa: E501


        :return: The freeform_address of this Address.  # noqa: E501
        :rtype: str
        """
        return self._freeform_address

    @freeform_address.setter
    def freeform_address(self, freeform_address):
        """Sets the freeform_address of this Address.


        :param freeform_address: The freeform_address of this Address.  # noqa: E501
        :type: str
        """

        self._freeform_address = freeform_address

    @property
    def local_name(self):
        """Gets the local_name of this Address.  # noqa: E501


        :return: The local_name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._local_name

    @local_name.setter
    def local_name(self, local_name):
        """Sets the local_name of this Address.


        :param local_name: The local_name of this Address.  # noqa: E501
        :type: str
        """

        self._local_name = local_name

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
        if not isinstance(other, Address):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Address):
            return True

        return self.to_dict() != other.to_dict()
