# coding: utf-8
"""
    Amphora Data

                 Connect information in real time with Amphora Data.                          Learn more at https://docs.amphoradata.com  # noqa: E501

    The version of the OpenAPI document: 0.10.1
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from amphora_api_client.api_client import ApiClient
from amphora_api_client.exceptions import (ApiTypeError, ApiValueError)


class SearchApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def search_search_amphorae(self, **kwargs):  # noqa: E501
        """Searches for Amphorae.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_search_amphorae(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str term: General search term for text comparison.
        :param str labels: Comma separated labels that must be included in results.
        :param float lat: Latitude (center of search area).
        :param float lon: Longitude (center of search area).
        :param float dist: Distance from center of search area (describing a circle).
        :param str x_amphoradata_version: API Version Number
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[BasicAmphora]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.search_search_amphorae_with_http_info(**
                                                          kwargs)  # noqa: E501

    def search_search_amphorae_with_http_info(self, **kwargs):  # noqa: E501
        """Searches for Amphorae.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_search_amphorae_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str term: General search term for text comparison.
        :param str labels: Comma separated labels that must be included in results.
        :param float lat: Latitude (center of search area).
        :param float lon: Longitude (center of search area).
        :param float dist: Distance from center of search area (describing a circle).
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
        :return: tuple(list[BasicAmphora], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'term', 'labels', 'lat', 'lon', 'dist', 'x_amphoradata_version'
        ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'"
                                   " to method search_search_amphorae" % key)
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'term' in local_var_params and local_var_params[
                'term'] is not None:  # noqa: E501
            query_params.append(
                ('term', local_var_params['term']))  # noqa: E501
        if 'labels' in local_var_params and local_var_params[
                'labels'] is not None:  # noqa: E501
            query_params.append(
                ('labels', local_var_params['labels']))  # noqa: E501
        if 'lat' in local_var_params and local_var_params[
                'lat'] is not None:  # noqa: E501
            query_params.append(('lat', local_var_params['lat']))  # noqa: E501
        if 'lon' in local_var_params and local_var_params[
                'lon'] is not None:  # noqa: E501
            query_params.append(('lon', local_var_params['lon']))  # noqa: E501
        if 'dist' in local_var_params and local_var_params[
                'dist'] is not None:  # noqa: E501
            query_params.append(
                ('dist', local_var_params['dist']))  # noqa: E501

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
            '/api/search/amphorae',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BasicAmphora]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_search_amphorae_by_location(self, **kwargs):  # noqa: E501
        """Searches for Amphorae by loction.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_search_amphorae_by_location(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param float lat: Latitude.
        :param float lon: Longitude.
        :param float dist: Distance from Latitude and Longitude in which to search.
        :param str x_amphoradata_version: API Version Number
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[BasicAmphora]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.search_search_amphorae_by_location_with_http_info(
            **kwargs)  # noqa: E501

    def search_search_amphorae_by_location_with_http_info(
            self, **kwargs):  # noqa: E501
        """Searches for Amphorae by loction.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_search_amphorae_by_location_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param float lat: Latitude.
        :param float lon: Longitude.
        :param float dist: Distance from Latitude and Longitude in which to search.
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
        :return: tuple(list[BasicAmphora], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['lat', 'lon', 'dist',
                      'x_amphoradata_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_search_amphorae_by_location" % key)
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'lat' in local_var_params and local_var_params[
                'lat'] is not None:  # noqa: E501
            query_params.append(('lat', local_var_params['lat']))  # noqa: E501
        if 'lon' in local_var_params and local_var_params[
                'lon'] is not None:  # noqa: E501
            query_params.append(('lon', local_var_params['lon']))  # noqa: E501
        if 'dist' in local_var_params and local_var_params[
                'dist'] is not None:  # noqa: E501
            query_params.append(
                ('dist', local_var_params['dist']))  # noqa: E501

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
            '/api/search/amphorae/byLocation',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BasicAmphora]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_search_amphorae_by_organisation(self, **kwargs):  # noqa: E501
        """Searches for Amphorae in an Organisation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_search_amphorae_by_organisation(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str org_id: Organisation Id.
        :param str x_amphoradata_version: API Version Number
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[BasicAmphora]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.search_search_amphorae_by_organisation_with_http_info(
            **kwargs)  # noqa: E501

    def search_search_amphorae_by_organisation_with_http_info(
            self, **kwargs):  # noqa: E501
        """Searches for Amphorae in an Organisation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_search_amphorae_by_organisation_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str org_id: Organisation Id.
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
        :return: tuple(list[BasicAmphora], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['org_id', 'x_amphoradata_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_search_amphorae_by_organisation" % key)
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'org_id' in local_var_params and local_var_params[
                'org_id'] is not None:  # noqa: E501
            query_params.append(
                ('orgId', local_var_params['org_id']))  # noqa: E501

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
            '/api/search/amphorae/byOrganisation',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BasicAmphora]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_search_organisations(self, **kwargs):  # noqa: E501
        """Searches for Organisations with fuzzy search.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_search_organisations(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str term: Search Term.
        :param str x_amphoradata_version: API Version Number
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[Organisation]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.search_search_organisations_with_http_info(
            **kwargs)  # noqa: E501

    def search_search_organisations_with_http_info(self,
                                                   **kwargs):  # noqa: E501
        """Searches for Organisations with fuzzy search.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_search_organisations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str term: Search Term.
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
        :return: tuple(list[Organisation], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['term', 'x_amphoradata_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'"
                                   " to method search_search_organisations" %
                                   key)
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'term' in local_var_params and local_var_params[
                'term'] is not None:  # noqa: E501
            query_params.append(
                ('term', local_var_params['term']))  # noqa: E501

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
            '/api/search/organisations',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Organisation]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
