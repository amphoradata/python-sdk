# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.28
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class CreateInvoice(object):
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
        'month': 'datetime',
        'organisation_id': 'str',
        'preview': 'bool',
        'regenerate': 'bool'
    }

    attribute_map = {
        'month': 'month',
        'organisation_id': 'organisationId',
        'preview': 'preview',
        'regenerate': 'regenerate'
    }

    def __init__(self,
                 month=None,
                 organisation_id=None,
                 preview=None,
                 regenerate=None,
                 local_vars_configuration=None):  # noqa: E501
        """CreateInvoice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._month = None
        self._organisation_id = None
        self._preview = None
        self._regenerate = None
        self.discriminator = None

        if month is not None:
            self.month = month
        self.organisation_id = organisation_id
        self.preview = preview
        self.regenerate = regenerate

    @property
    def month(self):
        """Gets the month of this CreateInvoice.  # noqa: E501


        :return: The month of this CreateInvoice.  # noqa: E501
        :rtype: datetime
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this CreateInvoice.


        :param month: The month of this CreateInvoice.  # noqa: E501
        :type: datetime
        """

        self._month = month

    @property
    def organisation_id(self):
        """Gets the organisation_id of this CreateInvoice.  # noqa: E501


        :return: The organisation_id of this CreateInvoice.  # noqa: E501
        :rtype: str
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this CreateInvoice.


        :param organisation_id: The organisation_id of this CreateInvoice.  # noqa: E501
        :type: str
        """

        self._organisation_id = organisation_id

    @property
    def preview(self):
        """Gets the preview of this CreateInvoice.  # noqa: E501


        :return: The preview of this CreateInvoice.  # noqa: E501
        :rtype: bool
        """
        return self._preview

    @preview.setter
    def preview(self, preview):
        """Sets the preview of this CreateInvoice.


        :param preview: The preview of this CreateInvoice.  # noqa: E501
        :type: bool
        """

        self._preview = preview

    @property
    def regenerate(self):
        """Gets the regenerate of this CreateInvoice.  # noqa: E501


        :return: The regenerate of this CreateInvoice.  # noqa: E501
        :rtype: bool
        """
        return self._regenerate

    @regenerate.setter
    def regenerate(self, regenerate):
        """Sets the regenerate of this CreateInvoice.


        :param regenerate: The regenerate of this CreateInvoice.  # noqa: E501
        :type: bool
        """

        self._regenerate = regenerate

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
        if not isinstance(other, CreateInvoice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateInvoice):
            return True

        return self.to_dict() != other.to_dict()
