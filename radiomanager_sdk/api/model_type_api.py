# coding: utf-8

"""
    RadioManager

    RadioManager  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: support@pluxbox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from radiomanager_sdk.api_client import ApiClient


class ModelTypeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_model_type_by_id(self, id, **kwargs):  # noqa: E501
        """Get modelType by id  # noqa: E501

        Get modelType by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_model_type_by_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: ID of ModelType **(Required)** (required)
        :param int external_station_id: Query on a different (content providing) station *(Optional)*
        :return: ModelTypeResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_model_type_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_model_type_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_model_type_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get modelType by id  # noqa: E501

        Get modelType by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_model_type_by_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: ID of ModelType **(Required)** (required)
        :param int external_station_id: Query on a different (content providing) station *(Optional)*
        :return: ModelTypeResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'external_station_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_model_type_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_model_type_by_id`")  # noqa: E501

        if 'id' in params and params['id'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `id` when calling `get_model_type_by_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'external_station_id' in params:
            query_params.append(('_external_station_id', params['external_station_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key']  # noqa: E501

        return self.api_client.call_api(
            '/model_types/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelTypeResult',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_model_types(self, **kwargs):  # noqa: E501
        """Get all modelTypes.  # noqa: E501

        List all modelTypes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_model_types(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: Current page *(Optional)*
        :param int program_id: Search on Program ID *(Optional)*
        :param int broadcast_id: Search on Broadcast ID *(Optional)*
        :param int item_id: Search on Item ID *(Optional)*
        :param int campaign_id: Search on Campaign ID *(Optional)*
        :param int presenter_id: Search on Presenter ID *(Optional)*
        :param int contact_id: Search on Contact ID *(Optional)*
        :param str model: Search Modeltypes for certain Model *(Optional)*
        :param int limit: Results per page *(Optional)*
        :param str order_by: Field to order the results *(Optional)*
        :param str order_direction: Direction of ordering *(Optional)*
        :param int external_station_id: Query on a different (content providing) station *(Optional)*
        :return: ModelTypeResults
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_model_types_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_model_types_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_model_types_with_http_info(self, **kwargs):  # noqa: E501
        """Get all modelTypes.  # noqa: E501

        List all modelTypes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_model_types_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: Current page *(Optional)*
        :param int program_id: Search on Program ID *(Optional)*
        :param int broadcast_id: Search on Broadcast ID *(Optional)*
        :param int item_id: Search on Item ID *(Optional)*
        :param int campaign_id: Search on Campaign ID *(Optional)*
        :param int presenter_id: Search on Presenter ID *(Optional)*
        :param int contact_id: Search on Contact ID *(Optional)*
        :param str model: Search Modeltypes for certain Model *(Optional)*
        :param int limit: Results per page *(Optional)*
        :param str order_by: Field to order the results *(Optional)*
        :param str order_direction: Direction of ordering *(Optional)*
        :param int external_station_id: Query on a different (content providing) station *(Optional)*
        :return: ModelTypeResults
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'program_id', 'broadcast_id', 'item_id', 'campaign_id', 'presenter_id', 'contact_id', 'model', 'limit', 'order_by', 'order_direction', 'external_station_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_model_types" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page' in params and params['page'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `list_model_types`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 50:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_model_types`, must be a value less than or equal to `50`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_model_types`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'program_id' in params:
            query_params.append(('program_id', params['program_id']))  # noqa: E501
        if 'broadcast_id' in params:
            query_params.append(('broadcast_id', params['broadcast_id']))  # noqa: E501
        if 'item_id' in params:
            query_params.append(('item_id', params['item_id']))  # noqa: E501
        if 'campaign_id' in params:
            query_params.append(('campaign_id', params['campaign_id']))  # noqa: E501
        if 'presenter_id' in params:
            query_params.append(('presenter_id', params['presenter_id']))  # noqa: E501
        if 'contact_id' in params:
            query_params.append(('contact_id', params['contact_id']))  # noqa: E501
        if 'model' in params:
            query_params.append(('model', params['model']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order-by', params['order_by']))  # noqa: E501
        if 'order_direction' in params:
            query_params.append(('order-direction', params['order_direction']))  # noqa: E501
        if 'external_station_id' in params:
            query_params.append(('_external_station_id', params['external_station_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key']  # noqa: E501

        return self.api_client.call_api(
            '/model_types', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelTypeResults',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)