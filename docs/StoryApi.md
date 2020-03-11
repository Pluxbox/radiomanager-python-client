# radiomanager_sdk.StoryApi

All URIs are relative to *https://radiomanager.io/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_story**](StoryApi.md#create_story) | **POST** /stories | Create story.
[**delete_story_by_id**](StoryApi.md#delete_story_by_id) | **DELETE** /stories/{id} | Delete story by id
[**get_story_by_id**](StoryApi.md#get_story_by_id) | **GET** /stories/{id} | Get story by id
[**list_stories**](StoryApi.md#list_stories) | **GET** /stories | Get all stories.
[**update_story_by_id**](StoryApi.md#update_story_by_id) | **PATCH** /stories/{id} | Update story by id


# **create_story**
> PostSuccess create_story(data)

Create story.

Create story.

### Example

* Api Key Authentication (API-Key):
```python
from __future__ import print_function
import time
import radiomanager_sdk
from radiomanager_sdk.rest import ApiException
from pprint import pprint
configuration = radiomanager_sdk.Configuration()
# Configure API key authorization: API-Key
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Defining host is optional and default to https://radiomanager.io/api/v2
configuration.host = "https://radiomanager.io/api/v2"
# Enter a context with an instance of the API client
with radiomanager_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = radiomanager_sdk.StoryApi(api_client)
    data = radiomanager_sdk.StoryDataInput() # StoryDataInput | Data **(Required)**

    try:
        # Create story.
        api_response = api_instance.create_story(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StoryApi->create_story: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**StoryDataInput**](StoryDataInput.md)| Data **(Required)** | 

### Return type

[**PostSuccess**](PostSuccess.md)

### Authorization

[API-Key](../README.md#API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a story |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_story_by_id**
> Success delete_story_by_id(id)

Delete story by id

Delete story by id

### Example

* Api Key Authentication (API-Key):
```python
from __future__ import print_function
import time
import radiomanager_sdk
from radiomanager_sdk.rest import ApiException
from pprint import pprint
configuration = radiomanager_sdk.Configuration()
# Configure API key authorization: API-Key
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Defining host is optional and default to https://radiomanager.io/api/v2
configuration.host = "https://radiomanager.io/api/v2"
# Enter a context with an instance of the API client
with radiomanager_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = radiomanager_sdk.StoryApi(api_client)
    id = 0 # int | ID of Story **(Required)** (default to 0)

    try:
        # Delete story by id
        api_response = api_instance.delete_story_by_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StoryApi->delete_story_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Story **(Required)** | [default to 0]

### Return type

[**Success**](Success.md)

### Authorization

[API-Key](../README.md#API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted Story by id |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_story_by_id**
> StoryResult get_story_by_id(id, external_station_id=external_station_id)

Get story by id

Get story by id

### Example

* Api Key Authentication (API-Key):
```python
from __future__ import print_function
import time
import radiomanager_sdk
from radiomanager_sdk.rest import ApiException
from pprint import pprint
configuration = radiomanager_sdk.Configuration()
# Configure API key authorization: API-Key
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Defining host is optional and default to https://radiomanager.io/api/v2
configuration.host = "https://radiomanager.io/api/v2"
# Enter a context with an instance of the API client
with radiomanager_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = radiomanager_sdk.StoryApi(api_client)
    id = 0 # int | ID of Story **(Required)** (default to 0)
external_station_id = 56 # int | Query on a different (content providing) station *(Optional)* (optional)

    try:
        # Get story by id
        api_response = api_instance.get_story_by_id(id, external_station_id=external_station_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StoryApi->get_story_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Story **(Required)** | [default to 0]
 **external_station_id** | **int**| Query on a different (content providing) station *(Optional)* | [optional] 

### Return type

[**StoryResult**](StoryResult.md)

### Authorization

[API-Key](../README.md#API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully got Story by id |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stories**
> StoryResults list_stories(page=page, item_id=item_id, model_type_id=model_type_id, tag_id=tag_id, limit=limit, order_by=order_by, order_direction=order_direction, external_station_id=external_station_id)

Get all stories.

List all stories.

### Example

* Api Key Authentication (API-Key):
```python
from __future__ import print_function
import time
import radiomanager_sdk
from radiomanager_sdk.rest import ApiException
from pprint import pprint
configuration = radiomanager_sdk.Configuration()
# Configure API key authorization: API-Key
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Defining host is optional and default to https://radiomanager.io/api/v2
configuration.host = "https://radiomanager.io/api/v2"
# Enter a context with an instance of the API client
with radiomanager_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = radiomanager_sdk.StoryApi(api_client)
    page = 1 # int | Current page *(Optional)* (optional) (default to 1)
item_id = 56 # int | Search on Item ID *(Optional)* `(Relation)` (optional)
model_type_id = 56 # int | Search on ModelType ID *(Optional)* `(Relation)` (optional)
tag_id = 56 # int | Search on Tag ID *(Optional)* `(Relation)` (optional)
limit = 56 # int | Results per page *(Optional)* (optional)
order_by = 'order_by_example' # str | Field to order the results *(Optional)* (optional)
order_direction = 'order_direction_example' # str | Direction of ordering *(Optional)* (optional)
external_station_id = 56 # int | Query on a different (content providing) station *(Optional)* (optional)

    try:
        # Get all stories.
        api_response = api_instance.list_stories(page=page, item_id=item_id, model_type_id=model_type_id, tag_id=tag_id, limit=limit, order_by=order_by, order_direction=order_direction, external_station_id=external_station_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StoryApi->list_stories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Current page *(Optional)* | [optional] [default to 1]
 **item_id** | **int**| Search on Item ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **model_type_id** | **int**| Search on ModelType ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **tag_id** | **int**| Search on Tag ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **limit** | **int**| Results per page *(Optional)* | [optional] 
 **order_by** | **str**| Field to order the results *(Optional)* | [optional] 
 **order_direction** | **str**| Direction of ordering *(Optional)* | [optional] 
 **external_station_id** | **int**| Query on a different (content providing) station *(Optional)* | [optional] 

### Return type

[**StoryResults**](StoryResults.md)

### Authorization

[API-Key](../README.md#API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully got all stories |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_story_by_id**
> Success update_story_by_id(id, data=data)

Update story by id

Update story by id

### Example

* Api Key Authentication (API-Key):
```python
from __future__ import print_function
import time
import radiomanager_sdk
from radiomanager_sdk.rest import ApiException
from pprint import pprint
configuration = radiomanager_sdk.Configuration()
# Configure API key authorization: API-Key
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Defining host is optional and default to https://radiomanager.io/api/v2
configuration.host = "https://radiomanager.io/api/v2"
# Enter a context with an instance of the API client
with radiomanager_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = radiomanager_sdk.StoryApi(api_client)
    id = 0 # int | ID of Story **(Required)** (default to 0)
data = radiomanager_sdk.StoryDataInput() # StoryDataInput | Data *(Optional)* (optional)

    try:
        # Update story by id
        api_response = api_instance.update_story_by_id(id, data=data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StoryApi->update_story_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Story **(Required)** | [default to 0]
 **data** | [**StoryDataInput**](StoryDataInput.md)| Data *(Optional)* | [optional] 

### Return type

[**Success**](Success.md)

### Authorization

[API-Key](../README.md#API-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated Story by id |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

