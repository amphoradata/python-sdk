# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.14
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class Run(object):
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
        'version_info': 'OneOfVersionInfo',
        'started_by': 'str',
        'success': 'bool',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'amphora_references': 'list[AmphoraReference]'
    }

    attribute_map = {
        'id': 'id',
        'version_info': 'versionInfo',
        'started_by': 'startedBy',
        'success': 'success',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'amphora_references': 'amphoraReferences'
    }

    def __init__(self,
                 id=None,
                 version_info=None,
                 started_by=None,
                 success=None,
                 start_time=None,
                 end_time=None,
                 amphora_references=None,
                 local_vars_configuration=None):  # noqa: E501
        """Run - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._version_info = None
        self._started_by = None
        self._success = None
        self._start_time = None
        self._end_time = None
        self._amphora_references = None
        self.discriminator = None

        self.id = id
        self.version_info = version_info
        self.started_by = started_by
        self.success = success
        self.start_time = start_time
        self.end_time = end_time
        self.amphora_references = amphora_references

    @property
    def id(self):
        """Gets the id of this Run.  # noqa: E501


        :return: The id of this Run.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Run.


        :param id: The id of this Run.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def version_info(self):
        """Gets the version_info of this Run.  # noqa: E501


        :return: The version_info of this Run.  # noqa: E501
        :rtype: OneOfVersionInfo
        """
        return self._version_info

    @version_info.setter
    def version_info(self, version_info):
        """Sets the version_info of this Run.


        :param version_info: The version_info of this Run.  # noqa: E501
        :type: OneOfVersionInfo
        """

        self._version_info = version_info

    @property
    def started_by(self):
        """Gets the started_by of this Run.  # noqa: E501


        :return: The started_by of this Run.  # noqa: E501
        :rtype: str
        """
        return self._started_by

    @started_by.setter
    def started_by(self, started_by):
        """Sets the started_by of this Run.


        :param started_by: The started_by of this Run.  # noqa: E501
        :type: str
        """

        self._started_by = started_by

    @property
    def success(self):
        """Gets the success of this Run.  # noqa: E501


        :return: The success of this Run.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this Run.


        :param success: The success of this Run.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def start_time(self):
        """Gets the start_time of this Run.  # noqa: E501


        :return: The start_time of this Run.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Run.


        :param start_time: The start_time of this Run.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this Run.  # noqa: E501


        :return: The end_time of this Run.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Run.


        :param end_time: The end_time of this Run.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def amphora_references(self):
        """Gets the amphora_references of this Run.  # noqa: E501


        :return: The amphora_references of this Run.  # noqa: E501
        :rtype: list[AmphoraReference]
        """
        return self._amphora_references

    @amphora_references.setter
    def amphora_references(self, amphora_references):
        """Sets the amphora_references of this Run.


        :param amphora_references: The amphora_references of this Run.  # noqa: E501
        :type: list[AmphoraReference]
        """

        self._amphora_references = amphora_references

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
        if not isinstance(other, Run):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Run):
            return True

        return self.to_dict() != other.to_dict()
