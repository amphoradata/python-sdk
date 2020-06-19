# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.6
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from amphora_api_client.configuration import Configuration


class AppLocation(object):
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
        'origin': 'str',
        'allowed_redirect_paths': 'list[str]',
        'post_logout_redirects': 'list[str]',
        'id': 'str'
    }

    attribute_map = {
        'origin': 'origin',
        'allowed_redirect_paths': 'allowedRedirectPaths',
        'post_logout_redirects': 'postLogoutRedirects',
        'id': 'id'
    }

    def __init__(self,
                 origin=None,
                 allowed_redirect_paths=None,
                 post_logout_redirects=None,
                 id=None,
                 local_vars_configuration=None):  # noqa: E501
        """AppLocation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._origin = None
        self._allowed_redirect_paths = None
        self._post_logout_redirects = None
        self._id = None
        self.discriminator = None

        self.origin = origin
        self.allowed_redirect_paths = allowed_redirect_paths
        self.post_logout_redirects = post_logout_redirects
        self.id = id

    @property
    def origin(self):
        """Gets the origin of this AppLocation.  # noqa: E501

        Gets or sets the expected origin from a XMLHttpRequest Must not end in '/'.  # noqa: E501

        :return: The origin of this AppLocation.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this AppLocation.

        Gets or sets the expected origin from a XMLHttpRequest Must not end in '/'.  # noqa: E501

        :param origin: The origin of this AppLocation.  # noqa: E501
        :type: str
        """

        self._origin = origin

    @property
    def allowed_redirect_paths(self):
        """Gets the allowed_redirect_paths of this AppLocation.  # noqa: E501

        Gets or sets allowed redirects after login, relative to Origin. Must begin with a '/'.  # noqa: E501

        :return: The allowed_redirect_paths of this AppLocation.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_redirect_paths

    @allowed_redirect_paths.setter
    def allowed_redirect_paths(self, allowed_redirect_paths):
        """Sets the allowed_redirect_paths of this AppLocation.

        Gets or sets allowed redirects after login, relative to Origin. Must begin with a '/'.  # noqa: E501

        :param allowed_redirect_paths: The allowed_redirect_paths of this AppLocation.  # noqa: E501
        :type: list[str]
        """

        self._allowed_redirect_paths = allowed_redirect_paths

    @property
    def post_logout_redirects(self):
        """Gets the post_logout_redirects of this AppLocation.  # noqa: E501

        Gets or sets the allowed redirect after logout. Must be an absolute url.  # noqa: E501

        :return: The post_logout_redirects of this AppLocation.  # noqa: E501
        :rtype: list[str]
        """
        return self._post_logout_redirects

    @post_logout_redirects.setter
    def post_logout_redirects(self, post_logout_redirects):
        """Sets the post_logout_redirects of this AppLocation.

        Gets or sets the allowed redirect after logout. Must be an absolute url.  # noqa: E501

        :param post_logout_redirects: The post_logout_redirects of this AppLocation.  # noqa: E501
        :type: list[str]
        """

        self._post_logout_redirects = post_logout_redirects

    @property
    def id(self):
        """Gets the id of this AppLocation.  # noqa: E501


        :return: The id of this AppLocation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppLocation.


        :param id: The id of this AppLocation.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, AppLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppLocation):
            return True

        return self.to_dict() != other.to_dict()
