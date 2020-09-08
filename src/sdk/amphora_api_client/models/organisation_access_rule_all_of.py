# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.21
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class OrganisationAccessRuleAllOf(object):
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
    openapi_types = {'organisation_id': 'str'}

    attribute_map = {'organisation_id': 'organisationId'}

    def __init__(self,
                 organisation_id=None,
                 local_vars_configuration=None):  # noqa: E501
        """OrganisationAccessRuleAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._organisation_id = None
        self.discriminator = None

        self.organisation_id = organisation_id

    @property
    def organisation_id(self):
        """Gets the organisation_id of this OrganisationAccessRuleAllOf.  # noqa: E501


        :return: The organisation_id of this OrganisationAccessRuleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this OrganisationAccessRuleAllOf.


        :param organisation_id: The organisation_id of this OrganisationAccessRuleAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and organisation_id is None:  # noqa: E501
            raise ValueError(
                "Invalid value for `organisation_id`, must not be `None`"
            )  # noqa: E501
        if (self.local_vars_configuration.client_side_validation
                and organisation_id is not None and len(organisation_id) < 1):
            raise ValueError(
                "Invalid value for `organisation_id`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._organisation_id = organisation_id

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
        if not isinstance(other, OrganisationAccessRuleAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganisationAccessRuleAllOf):
            return True

        return self.to_dict() != other.to_dict()
