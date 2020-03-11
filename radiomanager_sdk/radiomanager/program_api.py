# coding: utf-8

"""
    RadioManager

    RadioManager  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@pluxbox.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from radiomanager_sdk.api_client import ApiClient
from radiomanager_sdk.exceptions import (
    ApiTypeError,
    ApiValueError
)


class ProgramApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_program(self, data, **kwargs):  # noqa: E501
        """Create program.  # noqa: E501

        Create program.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_program(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ProgramDataInput data: Data **(Required)** (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PostSuccess
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_program_with_http_info(data, **kwargs)  # noqa: E501

    def create_program_with_http_info(self, data, **kwargs):  # noqa: E501
        """Create program.  # noqa: E501

        Create program.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_program_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ProgramDataInput data: Data **(Required)** (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PostSuccess, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_program" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data' is set
        if self.api_client.client_side_validation and ('data' not in local_var_params or  # noqa: E501
                                                        local_var_params['data'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data` when calling `create_program`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in local_var_params:
            body_params = local_var_params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API-Key']  # noqa: E501

        return self.api_client.call_api(
            '/programs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostSuccess',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_program_by_id(self, id, **kwargs):  # noqa: E501
        """Delete program by id  # noqa: E501

        Delete program by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_program_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: ID of program **(Required)** (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_program_by_id_with_http_info(id, **kwargs)  # noqa: E501

    def delete_program_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete program by id  # noqa: E501

        Delete program by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_program_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: ID of program **(Required)** (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Success, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_program_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `delete_program_by_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'id' in local_var_params and local_var_params['id'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `id` when calling `delete_program_by_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API-Key']  # noqa: E501

        return self.api_client.call_api(
            '/programs/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Success',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_program_by_id(self, id, **kwargs):  # noqa: E501
        """Get program by id  # noqa: E501

        Get program by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_program_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: ID of Program **(Required)** (required)
        :param int external_station_id: Query on a different (content providing) station *(Optional)*
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ProgramResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_program_by_id_with_http_info(id, **kwargs)  # noqa: E501

    def get_program_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get program by id  # noqa: E501

        Get program by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_program_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: ID of Program **(Required)** (required)
        :param int external_station_id: Query on a different (content providing) station *(Optional)*
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ProgramResult, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'external_station_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_program_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_program_by_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'id' in local_var_params and local_var_params['id'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `id` when calling `get_program_by_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'external_station_id' in local_var_params and local_var_params['external_station_id'] is not None:  # noqa: E501
            query_params.append(('_external_station_id', local_var_params['external_station_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API-Key']  # noqa: E501

        return self.api_client.call_api(
            '/programs/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProgramResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_programs(self, **kwargs):  # noqa: E501
        """Get all programs.  # noqa: E501

        List all programs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_programs(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page: Current page *(Optional)*
        :param int broadcast_id: Search on Broadcast ID *(Optional)* `(Relation)`
        :param int model_type_id: Search on ModelType ID *(Optional)* `(Relation)`
        :param int tag_id: Search on Tag ID *(Optional)* `(Relation)`
        :param int presenter_id: Search on Presenter ID *(Optional)* `(Relation)`
        :param int genre_id: Search on Genre ID *(Optional)*
        :param int block_id: Search on Block ID *(Optional)* `(Relation)`
        :param int item_id: Search on Item ID *(Optional)* `(Relation)`
        :param int disabled: Search on Disabled status *(Optional)*
        :param int limit: Results per page *(Optional)*
        :param str order_by: Field to order the results *(Optional)*
        :param str order_direction: Direction of ordering *(Optional)*
        :param int external_station_id: Query on a different (content providing) station *(Optional)*
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ProgramResults
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_programs_with_http_info(**kwargs)  # noqa: E501

    def list_programs_with_http_info(self, **kwargs):  # noqa: E501
        """Get all programs.  # noqa: E501

        List all programs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_programs_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page: Current page *(Optional)*
        :param int broadcast_id: Search on Broadcast ID *(Optional)* `(Relation)`
        :param int model_type_id: Search on ModelType ID *(Optional)* `(Relation)`
        :param int tag_id: Search on Tag ID *(Optional)* `(Relation)`
        :param int presenter_id: Search on Presenter ID *(Optional)* `(Relation)`
        :param int genre_id: Search on Genre ID *(Optional)*
        :param int block_id: Search on Block ID *(Optional)* `(Relation)`
        :param int item_id: Search on Item ID *(Optional)* `(Relation)`
        :param int disabled: Search on Disabled status *(Optional)*
        :param int limit: Results per page *(Optional)*
        :param str order_by: Field to order the results *(Optional)*
        :param str order_direction: Direction of ordering *(Optional)*
        :param int external_station_id: Query on a different (content providing) station *(Optional)*
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ProgramResults, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['page', 'broadcast_id', 'model_type_id', 'tag_id', 'presenter_id', 'genre_id', 'block_id', 'item_id', 'disabled', 'limit', 'order_by', 'order_direction', 'external_station_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_programs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `list_programs`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'disabled' in local_var_params and local_var_params['disabled'] > 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `disabled` when calling `list_programs`, must be a value less than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'disabled' in local_var_params and local_var_params['disabled'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `disabled` when calling `list_programs`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 50:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_programs`, must be a value less than or equal to `50`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_programs`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'broadcast_id' in local_var_params and local_var_params['broadcast_id'] is not None:  # noqa: E501
            query_params.append(('broadcast_id', local_var_params['broadcast_id']))  # noqa: E501
        if 'model_type_id' in local_var_params and local_var_params['model_type_id'] is not None:  # noqa: E501
            query_params.append(('model_type_id', local_var_params['model_type_id']))  # noqa: E501
        if 'tag_id' in local_var_params and local_var_params['tag_id'] is not None:  # noqa: E501
            query_params.append(('tag_id', local_var_params['tag_id']))  # noqa: E501
        if 'presenter_id' in local_var_params and local_var_params['presenter_id'] is not None:  # noqa: E501
            query_params.append(('presenter_id', local_var_params['presenter_id']))  # noqa: E501
        if 'genre_id' in local_var_params and local_var_params['genre_id'] is not None:  # noqa: E501
            query_params.append(('genre_id', local_var_params['genre_id']))  # noqa: E501
        if 'block_id' in local_var_params and local_var_params['block_id'] is not None:  # noqa: E501
            query_params.append(('block_id', local_var_params['block_id']))  # noqa: E501
        if 'item_id' in local_var_params and local_var_params['item_id'] is not None:  # noqa: E501
            query_params.append(('item_id', local_var_params['item_id']))  # noqa: E501
        if 'disabled' in local_var_params and local_var_params['disabled'] is not None:  # noqa: E501
            query_params.append(('disabled', local_var_params['disabled']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'order_by' in local_var_params and local_var_params['order_by'] is not None:  # noqa: E501
            query_params.append(('order-by', local_var_params['order_by']))  # noqa: E501
        if 'order_direction' in local_var_params and local_var_params['order_direction'] is not None:  # noqa: E501
            query_params.append(('order-direction', local_var_params['order_direction']))  # noqa: E501
        if 'external_station_id' in local_var_params and local_var_params['external_station_id'] is not None:  # noqa: E501
            query_params.append(('_external_station_id', local_var_params['external_station_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API-Key']  # noqa: E501

        return self.api_client.call_api(
            '/programs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProgramResults',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_program_by_id(self, id, **kwargs):  # noqa: E501
        """Update program by id  # noqa: E501

        Update program by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_program_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: ID of Program **(Required)** (required)
        :param ProgramDataInput data: Data *(Optional)*
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_program_by_id_with_http_info(id, **kwargs)  # noqa: E501

    def update_program_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update program by id  # noqa: E501

        Update program by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_program_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: ID of Program **(Required)** (required)
        :param ProgramDataInput data: Data *(Optional)*
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Success, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_program_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `update_program_by_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'id' in local_var_params and local_var_params['id'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `id` when calling `update_program_by_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in local_var_params:
            body_params = local_var_params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API-Key']  # noqa: E501

        return self.api_client.call_api(
            '/programs/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Success',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
