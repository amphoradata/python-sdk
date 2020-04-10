# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.9.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class Restriction(object):
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
        'kind': 'OneOfRestrictionKind',
        'target_organisation_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'kind': 'kind',
        'target_organisation_id': 'targetOrganisationId'
    }

    def __init__(self, id=None, kind=None, target_organisation_id=None, local_vars_configuration=None):  # noqa: E501
        """Restriction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._kind = None
        self._target_organisation_id = None
        self.discriminator = None

        self.id = id
        self.kind = kind
        self.target_organisation_id = target_organisation_id

    @property
    def id(self):
        """Gets the id of this Restriction.  # noqa: E501


        :return: The id of this Restriction.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Restriction.


        :param id: The id of this Restriction.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def kind(self):
        """Gets the kind of this Restriction.  # noqa: E501

        The kind of Restriction (Allow [default] or Deny)  # noqa: E501

        :return: The kind of this Restriction.  # noqa: E501
        :rtype: OneOfRestrictionKind
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Restriction.

        The kind of Restriction (Allow [default] or Deny)  # noqa: E501

        :param kind: The kind of this Restriction.  # noqa: E501
        :type: OneOfRestrictionKind
        """

        self._kind = kind

    @property
    def target_organisation_id(self):
        """Gets the target_organisation_id of this Restriction.  # noqa: E501

        Target Organisation's Id  # noqa: E501

        :return: The target_organisation_id of this Restriction.  # noqa: E501
        :rtype: str
        """
        return self._target_organisation_id

    @target_organisation_id.setter
    def target_organisation_id(self, target_organisation_id):
        """Sets the target_organisation_id of this Restriction.

        Target Organisation's Id  # noqa: E501

        :param target_organisation_id: The target_organisation_id of this Restriction.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and target_organisation_id is None:  # noqa: E501
            raise ValueError("Invalid value for `target_organisation_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                target_organisation_id is not None and len(target_organisation_id) < 1):
            raise ValueError("Invalid value for `target_organisation_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._target_organisation_id = target_organisation_id

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
        if not isinstance(other, Restriction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Restriction):
            return True

        return self.to_dict() != other.to_dict()
