# coding: utf-8

"""
    Pluxbox Radiomanager Client

    Pluxbox RadioManager gives you the power, flexibility and speed you always wanted in a lightweight and easy-to-use web-based radio solution. With Pluxbox RadioManager you can organise your radio workflow and automate your omnichannel communication with your listeners. We offer wide range specialised services for the radio and connections like Hybrid Radio, Visual Radio, your website and social media without losing focus on your broadcast. For more information visit https://pluxbox.com

    OpenAPI spec version: 2.0
    Contact: support@pluxbox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class BlockApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_block_by_id(self, id, **kwargs):
        """
        Get block by id
        Get block by id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_block_by_id(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of Block **(Required)** (required)
        :param int external_station_id: Query on a different (content providing) station *(Optional)*
        :return: BlockResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_block_by_id_with_http_info(id, **kwargs)
        else:
            (data) = self.get_block_by_id_with_http_info(id, **kwargs)
            return data

    def get_block_by_id_with_http_info(self, id, **kwargs):
        """
        Get block by id
        Get block by id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_block_by_id_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of Block **(Required)** (required)
        :param int external_station_id: Query on a different (content providing) station *(Optional)*
        :return: BlockResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'external_station_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_block_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_block_by_id`")

        if 'id' in params and params['id'] < 0:
            raise ValueError("Invalid value for parameter `id` when calling `get_block_by_id`, must be a value greater than or equal to `0`")

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []
        if 'external_station_id' in params:
            query_params.append(('_external_station_id', params['external_station_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['API Key']

        return self.api_client.call_api('/blocks/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BlockResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_current_block(self, **kwargs):
        """
        Get current Block
        Get current Block
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_current_block(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: BlockResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_current_block_with_http_info(**kwargs)
        else:
            (data) = self.get_current_block_with_http_info(**kwargs)
            return data

    def get_current_block_with_http_info(self, **kwargs):
        """
        Get current Block
        Get current Block
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_current_block_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: BlockResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_current_block" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['API Key']

        return self.api_client.call_api('/blocks/current', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BlockResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_next_block(self, **kwargs):
        """
        Get next Block
        Get next Block
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_next_block(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: BlockResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_next_block_with_http_info(**kwargs)
        else:
            (data) = self.get_next_block_with_http_info(**kwargs)
            return data

    def get_next_block_with_http_info(self, **kwargs):
        """
        Get next Block
        Get next Block
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_next_block_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: BlockResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_next_block" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['API Key']

        return self.api_client.call_api('/blocks/next', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BlockResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_blocks(self, **kwargs):
        """
        Get a list of all blocks currently in your station.
        Get a list of all blocks currently in your station. This feature supports pagination and will give a maximum of 50 blocks back.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_blocks(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page: Current page *(Optional)*
        :param datetime start_min: Minimum start date *(Optional)*
        :param datetime start_max: Maximum start date *(Optional)*
        :param int broadcast_id: Search on Broadcast ID *(Optional)* `(Relation)`
        :param int program_id: Search on Program ID *(Optional)* `(Relation)`
        :param int item_id: Search on Item ID *(Optional)* `(Relation)`
        :param int external_station_id: Query on a different (content providing) station *(Optional)*
        :return: BlockResults
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_blocks_with_http_info(**kwargs)
        else:
            (data) = self.list_blocks_with_http_info(**kwargs)
            return data

    def list_blocks_with_http_info(self, **kwargs):
        """
        Get a list of all blocks currently in your station.
        Get a list of all blocks currently in your station. This feature supports pagination and will give a maximum of 50 blocks back.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_blocks_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page: Current page *(Optional)*
        :param datetime start_min: Minimum start date *(Optional)*
        :param datetime start_max: Maximum start date *(Optional)*
        :param int broadcast_id: Search on Broadcast ID *(Optional)* `(Relation)`
        :param int program_id: Search on Program ID *(Optional)* `(Relation)`
        :param int item_id: Search on Item ID *(Optional)* `(Relation)`
        :param int external_station_id: Query on a different (content providing) station *(Optional)*
        :return: BlockResults
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'start_min', 'start_max', 'broadcast_id', 'program_id', 'item_id', 'external_station_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_blocks" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page' in params and params['page'] < 0:
            raise ValueError("Invalid value for parameter `page` when calling `list_blocks`, must be a value greater than or equal to `0`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))
        if 'start_min' in params:
            query_params.append(('start-min', params['start_min']))
        if 'start_max' in params:
            query_params.append(('start_max', params['start_max']))
        if 'broadcast_id' in params:
            query_params.append(('broadcast_id', params['broadcast_id']))
        if 'program_id' in params:
            query_params.append(('program_id', params['program_id']))
        if 'item_id' in params:
            query_params.append(('item_id', params['item_id']))
        if 'external_station_id' in params:
            query_params.append(('_external_station_id', params['external_station_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['API Key']

        return self.api_client.call_api('/blocks', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BlockResults',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
