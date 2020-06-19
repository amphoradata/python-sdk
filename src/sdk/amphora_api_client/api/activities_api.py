# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.6
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from amphora_api_client.api_client import ApiClient
from amphora_api_client.exceptions import (ApiTypeError, ApiValueError)


class ActivitiesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def activities_create_activity(self, create_activity,
                                   **kwargs):  # noqa: E501
        """Creates a new activity.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activities_create_activity(create_activity, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreateActivity create_activity: Metadata of the new activity. (required)
        :param str x_amphoradata_version: API Version Number
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Activity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.activities_create_activity_with_http_info(
            create_activity, **kwargs)  # noqa: E501

    def activities_create_activity_with_http_info(self, create_activity,
                                                  **kwargs):  # noqa: E501
        """Creates a new activity.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activities_create_activity_with_http_info(create_activity, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreateActivity create_activity: Metadata of the new activity. (required)
        :param str x_amphoradata_version: API Version Number
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Activity, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['create_activity', 'x_amphoradata_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'"
                                   " to method activities_create_activity" %
                                   key)
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'create_activity' is set
        if self.api_client.client_side_validation and (
                'create_activity' not in local_var_params or  # noqa: E501
                local_var_params['create_activity'] is None):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `create_activity` when calling `activities_create_activity`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_amphoradata_version' in local_var_params:
            header_params['x-amphoradata-version'] = local_var_params[
                'x_amphoradata_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_activity' in local_var_params:
            body_params = local_var_params['create_activity']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            'Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
                ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/activities',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Activity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def activities_delete_activity(self, id, **kwargs):  # noqa: E501
        """Deletes an activity.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activities_delete_activity(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: The activity Id. (required)
        :param str x_amphoradata_version: API Version Number
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.activities_delete_activity_with_http_info(
            id, **kwargs)  # noqa: E501

    def activities_delete_activity_with_http_info(self, id,
                                                  **kwargs):  # noqa: E501
        """Deletes an activity.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activities_delete_activity_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: The activity Id. (required)
        :param str x_amphoradata_version: API Version Number
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(file, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'x_amphoradata_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'"
                                   " to method activities_delete_activity" %
                                   key)
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_amphoradata_version' in local_var_params:
            header_params['x-amphoradata-version'] = local_var_params[
                'x_amphoradata_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/activities/{id}',
            'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def activities_read_activity(self, id, **kwargs):  # noqa: E501
        """Gets the metadata of an activity.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activities_read_activity(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: The activity Id. (required)
        :param str x_amphoradata_version: API Version Number
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Activity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.activities_read_activity_with_http_info(
            id, **kwargs)  # noqa: E501

    def activities_read_activity_with_http_info(self, id,
                                                **kwargs):  # noqa: E501
        """Gets the metadata of an activity.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activities_read_activity_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: The activity Id. (required)
        :param str x_amphoradata_version: API Version Number
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Activity, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'x_amphoradata_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'"
                                   " to method activities_read_activity" % key)
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_amphoradata_version' in local_var_params:
            header_params['x-amphoradata-version'] = local_var_params[
                'x_amphoradata_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/activities/{id}',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Activity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def activities_reference_amphora(self, id, run_id, amphora_id,
                                     amphora_reference,
                                     **kwargs):  # noqa: E501
        """References an Amphora during a run.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activities_reference_amphora(id, run_id, amphora_id, amphora_reference, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: The activity Id. (required)
        :param str run_id: The run Id. (required)
        :param str amphora_id: The Id of the Amphora to reference. (required)
        :param AmphoraReference amphora_reference: Information about the reference. (required)
        :param str x_amphoradata_version: API Version Number
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AmphoraReference
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.activities_reference_amphora_with_http_info(
            id, run_id, amphora_id, amphora_reference, **kwargs)  # noqa: E501

    def activities_reference_amphora_with_http_info(self, id, run_id,
                                                    amphora_id,
                                                    amphora_reference,
                                                    **kwargs):  # noqa: E501
        """References an Amphora during a run.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activities_reference_amphora_with_http_info(id, run_id, amphora_id, amphora_reference, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: The activity Id. (required)
        :param str run_id: The run Id. (required)
        :param str amphora_id: The Id of the Amphora to reference. (required)
        :param AmphoraReference amphora_reference: Information about the reference. (required)
        :param str x_amphoradata_version: API Version Number
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AmphoraReference, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id', 'run_id', 'amphora_id', 'amphora_reference',
            'x_amphoradata_version'
        ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'"
                                   " to method activities_reference_amphora" %
                                   key)
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'amphora_reference' is set
        if self.api_client.client_side_validation and (
                'amphora_reference' not in local_var_params or  # noqa: E501
                local_var_params['amphora_reference'] is None):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `amphora_reference` when calling `activities_reference_amphora`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'run_id' in local_var_params:
            path_params['runId'] = local_var_params['run_id']  # noqa: E501
        if 'amphora_id' in local_var_params:
            path_params['amphoraId'] = local_var_params[
                'amphora_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_amphoradata_version' in local_var_params:
            header_params['x-amphoradata-version'] = local_var_params[
                'x_amphoradata_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'amphora_reference' in local_var_params:
            body_params = local_var_params['amphora_reference']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            'Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
                ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/activities/{id}/Runs/{runId}/amphorae/{amphoraId}',
            'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AmphoraReference',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def activities_start_run(self, id, **kwargs):  # noqa: E501
        """Starts a new run of an activity.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activities_start_run(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: The activity id in which to start a run. (required)
        :param str x_amphoradata_version: API Version Number
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Run
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.activities_start_run_with_http_info(id,
                                                        **kwargs)  # noqa: E501

    def activities_start_run_with_http_info(self, id, **kwargs):  # noqa: E501
        """Starts a new run of an activity.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activities_start_run_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: The activity id in which to start a run. (required)
        :param str x_amphoradata_version: API Version Number
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Run, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'x_amphoradata_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'"
                                   " to method activities_start_run" % key)
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_amphoradata_version' in local_var_params:
            header_params['x-amphoradata-version'] = local_var_params[
                'x_amphoradata_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/activities/{id}/Runs',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Run',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def activities_update_run(self, id, run_id, update_run,
                              **kwargs):  # noqa: E501
        """Updates and completes a run.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activities_update_run(id, run_id, update_run, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: The activity Id. (required)
        :param str run_id: The run Id. (required)
        :param UpdateRun update_run: Information about the update. (required)
        :param str x_amphoradata_version: API Version Number
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Run
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.activities_update_run_with_http_info(
            id, run_id, update_run, **kwargs)  # noqa: E501

    def activities_update_run_with_http_info(self, id, run_id, update_run,
                                             **kwargs):  # noqa: E501
        """Updates and completes a run.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activities_update_run_with_http_info(id, run_id, update_run, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: The activity Id. (required)
        :param str run_id: The run Id. (required)
        :param UpdateRun update_run: Information about the update. (required)
        :param str x_amphoradata_version: API Version Number
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Run, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'run_id', 'update_run',
                      'x_amphoradata_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'"
                                   " to method activities_update_run" % key)
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'update_run' is set
        if self.api_client.client_side_validation and (
                'update_run' not in local_var_params or  # noqa: E501
                local_var_params['update_run'] is None):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `update_run` when calling `activities_update_run`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'run_id' in local_var_params:
            path_params['runId'] = local_var_params['run_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_amphoradata_version' in local_var_params:
            header_params['x-amphoradata-version'] = local_var_params[
                'x_amphoradata_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_run' in local_var_params:
            body_params = local_var_params['update_run']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            'Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
                ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/activities/{id}/Runs/{runId}',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Run',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)