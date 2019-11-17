# coding: utf-8

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.2.0dev1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from amphora_client.api_client import ApiClient
from amphora_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class UsersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def users_create(self, x_amphoradata_version, user_dto, **kwargs):  # noqa: E501
        """Creates a new User. Returns the password.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_create(x_amphoradata_version, user_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_amphoradata_version: API Version Number (required)
        :param UserDto user_dto: User parameters (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.users_create_with_http_info(x_amphoradata_version, user_dto, **kwargs)  # noqa: E501

    def users_create_with_http_info(self, x_amphoradata_version, user_dto, **kwargs):  # noqa: E501
        """Creates a new User. Returns the password.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_create_with_http_info(x_amphoradata_version, user_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_amphoradata_version: API Version Number (required)
        :param UserDto user_dto: User parameters (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['x_amphoradata_version', 'user_dto']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method users_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'x_amphoradata_version' is set
        if self.api_client.client_side_validation and ('x_amphoradata_version' not in local_var_params or  # noqa: E501
                                                        local_var_params['x_amphoradata_version'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `x_amphoradata_version` when calling `users_create`")  # noqa: E501
        # verify the required parameter 'user_dto' is set
        if self.api_client.client_side_validation and ('user_dto' not in local_var_params or  # noqa: E501
                                                        local_var_params['user_dto'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_dto` when calling `users_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_amphoradata_version' in local_var_params:
            header_params['x-amphoradata-version'] = local_var_params['x_amphoradata_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_dto' in local_var_params:
            body_params = local_var_params['user_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def users_read_self(self, x_amphoradata_version, **kwargs):  # noqa: E501
        """Get's logged in users information.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_read_self(x_amphoradata_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_amphoradata_version: API Version Number (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: UserDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.users_read_self_with_http_info(x_amphoradata_version, **kwargs)  # noqa: E501

    def users_read_self_with_http_info(self, x_amphoradata_version, **kwargs):  # noqa: E501
        """Get's logged in users information.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_read_self_with_http_info(x_amphoradata_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_amphoradata_version: API Version Number (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(UserDto, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['x_amphoradata_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method users_read_self" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'x_amphoradata_version' is set
        if self.api_client.client_side_validation and ('x_amphoradata_version' not in local_var_params or  # noqa: E501
                                                        local_var_params['x_amphoradata_version'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `x_amphoradata_version` when calling `users_read_self`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_amphoradata_version' in local_var_params:
            header_params['x-amphoradata-version'] = local_var_params['x_amphoradata_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/users/self', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
