# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.25
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class FileListOptions(object):
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
        'take': 'int',
        'skip': 'int',
        'order_by': 'str',
        'prefix': 'str'
    }

    attribute_map = {
        'take': 'take',
        'skip': 'skip',
        'order_by': 'orderBy',
        'prefix': 'prefix'
    }

    def __init__(self,
                 take=None,
                 skip=None,
                 order_by=None,
                 prefix=None,
                 local_vars_configuration=None):  # noqa: E501
        """FileListOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._take = None
        self._skip = None
        self._order_by = None
        self._prefix = None
        self.discriminator = None

        self.take = take
        self.skip = skip
        self.order_by = order_by
        self.prefix = prefix

    @property
    def take(self):
        """Gets the take of this FileListOptions.  # noqa: E501

        Gets or sets how many items to return. Defaults to 64.  # noqa: E501

        :return: The take of this FileListOptions.  # noqa: E501
        :rtype: int
        """
        return self._take

    @take.setter
    def take(self, take):
        """Sets the take of this FileListOptions.

        Gets or sets how many items to return. Defaults to 64.  # noqa: E501

        :param take: The take of this FileListOptions.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation
                and take is not None and take > 256):  # noqa: E501
            raise ValueError(
                "Invalid value for `take`, must be a value less than or equal to `256`"
            )  # noqa: E501
        if (self.local_vars_configuration.client_side_validation
                and take is not None and take < 1):  # noqa: E501
            raise ValueError(
                "Invalid value for `take`, must be a value greater than or equal to `1`"
            )  # noqa: E501

        self._take = take

    @property
    def skip(self):
        """Gets the skip of this FileListOptions.  # noqa: E501

        Gets or sets how many items to skip before returning. Defaults to 0.  # noqa: E501

        :return: The skip of this FileListOptions.  # noqa: E501
        :rtype: int
        """
        return self._skip

    @skip.setter
    def skip(self, skip):
        """Sets the skip of this FileListOptions.

        Gets or sets how many items to skip before returning. Defaults to 0.  # noqa: E501

        :param skip: The skip of this FileListOptions.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation
                and skip is not None and skip > 2147483647):  # noqa: E501
            raise ValueError(
                "Invalid value for `skip`, must be a value less than or equal to `2147483647`"
            )  # noqa: E501
        if (self.local_vars_configuration.client_side_validation
                and skip is not None and skip < 0):  # noqa: E501
            raise ValueError(
                "Invalid value for `skip`, must be a value greater than or equal to `0`"
            )  # noqa: E501

        self._skip = skip

    @property
    def order_by(self):
        """Gets the order_by of this FileListOptions.  # noqa: E501

        Gets or sets the the orderBy parameter. Options are Alphabetical or LastModified.  # noqa: E501

        :return: The order_by of this FileListOptions.  # noqa: E501
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this FileListOptions.

        Gets or sets the the orderBy parameter. Options are Alphabetical or LastModified.  # noqa: E501

        :param order_by: The order_by of this FileListOptions.  # noqa: E501
        :type: str
        """

        self._order_by = order_by

    @property
    def prefix(self):
        """Gets the prefix of this FileListOptions.  # noqa: E501

        Gets or sets a prefix filter for all file names. Is case sensitive.  # noqa: E501

        :return: The prefix of this FileListOptions.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this FileListOptions.

        Gets or sets a prefix filter for all file names. Is case sensitive.  # noqa: E501

        :param prefix: The prefix of this FileListOptions.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

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
        if not isinstance(other, FileListOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileListOptions):
            return True

        return self.to_dict() != other.to_dict()
