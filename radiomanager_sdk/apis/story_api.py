# coding: utf-8

"""
    RadioManager

    RadioManager

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

from ..api_client import ApiClient


class StoryApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_story(self, data, **kwargs):
        """
        Create story.
        Create story.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_story(data, async=True)
        >>> result = thread.get()

        :param async bool
        :param StoryDataInput data: Data **(Required)** (required)
        :return: PostSuccess
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_story_with_http_info(data, **kwargs)
        else:
            (data) = self.create_story_with_http_info(data, **kwargs)
            return data

    def create_story_with_http_info(self, data, **kwargs):
        """
        Create story.
        Create story.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_story_with_http_info(data, async=True)
        >>> result = thread.get()

        :param async bool
        :param StoryDataInput data: Data **(Required)** (required)
        :return: PostSuccess
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_story" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params) or (params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `create_story`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['API Key']

        return self.api_client.call_api('/stories', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PostSuccess',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_story_by_id(self, id, **kwargs):
        """
        Delete story by id
        Delete story by id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_story_by_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: ID of Story **(Required)** (required)
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_story_by_id_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_story_by_id_with_http_info(id, **kwargs)
            return data

    def delete_story_by_id_with_http_info(self, id, **kwargs):
        """
        Delete story by id
        Delete story by id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_story_by_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: ID of Story **(Required)** (required)
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_story_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_story_by_id`")

        if 'id' in params and params['id'] < 0:
            raise ValueError("Invalid value for parameter `id` when calling `delete_story_by_id`, must be a value greater than or equal to `0`")

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

        return self.api_client.call_api('/stories/{id}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Success',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_story_by_id(self, id, **kwargs):
        """
        Get story by id
        Get story by id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_story_by_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: ID of Story **(Required)** (required)
        :param int external_station_id: Query on a different (content providing) station *(Optional)*
        :return: StoryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_story_by_id_with_http_info(id, **kwargs)
        else:
            (data) = self.get_story_by_id_with_http_info(id, **kwargs)
            return data

    def get_story_by_id_with_http_info(self, id, **kwargs):
        """
        Get story by id
        Get story by id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_story_by_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: ID of Story **(Required)** (required)
        :param int external_station_id: Query on a different (content providing) station *(Optional)*
        :return: StoryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'external_station_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_story_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_story_by_id`")

        if 'id' in params and params['id'] < 0:
            raise ValueError("Invalid value for parameter `id` when calling `get_story_by_id`, must be a value greater than or equal to `0`")

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

        return self.api_client.call_api('/stories/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='StoryResult',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_stories(self, **kwargs):
        """
        Get all stories.
        List all stories.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_stories(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: Current page *(Optional)*
        :param int model_type_id: Search on ModelType ID *(Optional)*
        :param int tag_id: Search on Tag ID *(Optional)* `(Relation)`
        :param int item_id: Search on Item ID *(Optional)* `(Relation)`
        :param int external_station_id: Query on a different (content providing) station *(Optional)*
        :return: StoryResults
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_stories_with_http_info(**kwargs)
        else:
            (data) = self.list_stories_with_http_info(**kwargs)
            return data

    def list_stories_with_http_info(self, **kwargs):
        """
        Get all stories.
        List all stories.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_stories_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: Current page *(Optional)*
        :param int model_type_id: Search on ModelType ID *(Optional)*
        :param int tag_id: Search on Tag ID *(Optional)* `(Relation)`
        :param int item_id: Search on Item ID *(Optional)* `(Relation)`
        :param int external_station_id: Query on a different (content providing) station *(Optional)*
        :return: StoryResults
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'model_type_id', 'tag_id', 'item_id', 'external_station_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_stories" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page' in params and params['page'] < 0:
            raise ValueError("Invalid value for parameter `page` when calling `list_stories`, must be a value greater than or equal to `0`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))
        if 'model_type_id' in params:
            query_params.append(('model_type_id', params['model_type_id']))
        if 'tag_id' in params:
            query_params.append(('tag_id', params['tag_id']))
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

        return self.api_client.call_api('/stories', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='StoryResults',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_story_by_id(self, id, **kwargs):
        """
        Update story by id
        Update story by id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_story_by_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: ID of Story **(Required)** (required)
        :param StoryDataInput data: Data *(Optional)*
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_story_by_id_with_http_info(id, **kwargs)
        else:
            (data) = self.update_story_by_id_with_http_info(id, **kwargs)
            return data

    def update_story_by_id_with_http_info(self, id, **kwargs):
        """
        Update story by id
        Update story by id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_story_by_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: ID of Story **(Required)** (required)
        :param StoryDataInput data: Data *(Optional)*
        :return: Success
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'data']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_story_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_story_by_id`")

        if 'id' in params and params['id'] < 0:
            raise ValueError("Invalid value for parameter `id` when calling `update_story_by_id`, must be a value greater than or equal to `0`")

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['API Key']

        return self.api_client.call_api('/stories/{id}', 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Success',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
