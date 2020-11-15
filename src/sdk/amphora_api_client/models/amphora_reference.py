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


class AmphoraReference(object):
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
        'amphora_id': 'str',
        'files_consumed': 'int',
        'files_produced': 'int',
        'signals_consumed': 'int',
        'signals_produced': 'int'
    }

    attribute_map = {
        'amphora_id': 'amphoraId',
        'files_consumed': 'filesConsumed',
        'files_produced': 'filesProduced',
        'signals_consumed': 'signalsConsumed',
        'signals_produced': 'signalsProduced'
    }

    def __init__(self,
                 amphora_id=None,
                 files_consumed=None,
                 files_produced=None,
                 signals_consumed=None,
                 signals_produced=None,
                 local_vars_configuration=None):  # noqa: E501
        """AmphoraReference - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amphora_id = None
        self._files_consumed = None
        self._files_produced = None
        self._signals_consumed = None
        self._signals_produced = None
        self.discriminator = None

        self.amphora_id = amphora_id
        self.files_consumed = files_consumed
        self.files_produced = files_produced
        self.signals_consumed = signals_consumed
        self.signals_produced = signals_produced

    @property
    def amphora_id(self):
        """Gets the amphora_id of this AmphoraReference.  # noqa: E501


        :return: The amphora_id of this AmphoraReference.  # noqa: E501
        :rtype: str
        """
        return self._amphora_id

    @amphora_id.setter
    def amphora_id(self, amphora_id):
        """Sets the amphora_id of this AmphoraReference.


        :param amphora_id: The amphora_id of this AmphoraReference.  # noqa: E501
        :type: str
        """

        self._amphora_id = amphora_id

    @property
    def files_consumed(self):
        """Gets the files_consumed of this AmphoraReference.  # noqa: E501


        :return: The files_consumed of this AmphoraReference.  # noqa: E501
        :rtype: int
        """
        return self._files_consumed

    @files_consumed.setter
    def files_consumed(self, files_consumed):
        """Sets the files_consumed of this AmphoraReference.


        :param files_consumed: The files_consumed of this AmphoraReference.  # noqa: E501
        :type: int
        """

        self._files_consumed = files_consumed

    @property
    def files_produced(self):
        """Gets the files_produced of this AmphoraReference.  # noqa: E501


        :return: The files_produced of this AmphoraReference.  # noqa: E501
        :rtype: int
        """
        return self._files_produced

    @files_produced.setter
    def files_produced(self, files_produced):
        """Sets the files_produced of this AmphoraReference.


        :param files_produced: The files_produced of this AmphoraReference.  # noqa: E501
        :type: int
        """

        self._files_produced = files_produced

    @property
    def signals_consumed(self):
        """Gets the signals_consumed of this AmphoraReference.  # noqa: E501


        :return: The signals_consumed of this AmphoraReference.  # noqa: E501
        :rtype: int
        """
        return self._signals_consumed

    @signals_consumed.setter
    def signals_consumed(self, signals_consumed):
        """Sets the signals_consumed of this AmphoraReference.


        :param signals_consumed: The signals_consumed of this AmphoraReference.  # noqa: E501
        :type: int
        """

        self._signals_consumed = signals_consumed

    @property
    def signals_produced(self):
        """Gets the signals_produced of this AmphoraReference.  # noqa: E501


        :return: The signals_produced of this AmphoraReference.  # noqa: E501
        :rtype: int
        """
        return self._signals_produced

    @signals_produced.setter
    def signals_produced(self, signals_produced):
        """Sets the signals_produced of this AmphoraReference.


        :param signals_produced: The signals_produced of this AmphoraReference.  # noqa: E501
        :type: int
        """

        self._signals_produced = signals_produced

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
        if not isinstance(other, AmphoraReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AmphoraReference):
            return True

        return self.to_dict() != other.to_dict()
