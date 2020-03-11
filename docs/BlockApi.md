# radiomanager_sdk.BlockApi

All URIs are relative to *https://radiomanager.io/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_block_by_id**](BlockApi.md#get_block_by_id) | **GET** /blocks/{id} | Get block by id
[**get_current_block**](BlockApi.md#get_current_block) | **GET** /blocks/current | Get current Block
[**get_next_block**](BlockApi.md#get_next_block) | **GET** /blocks/next | Get upcoming Block
[**list_blocks**](BlockApi.md#list_blocks) | **GET** /blocks | Get a list of all blocks currently in your station.


# **get_block_by_id**
> BlockResult get_block_by_id(id, external_station_id=external_station_id)

Get block by id

Get block by id

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
    api_instance = radiomanager_sdk.BlockApi(api_client)
    id = 0 # int | ID of Block **(Required)** (default to 0)
external_station_id = 56 # int | Query on a different (content providing) station *(Optional)* (optional)

    try:
        # Get block by id
        api_response = api_instance.get_block_by_id(id, external_station_id=external_station_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BlockApi->get_block_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Block **(Required)** | [default to 0]
 **external_station_id** | **int**| Query on a different (content providing) station *(Optional)* | [optional] 

### Return type

[**BlockResult**](BlockResult.md)

### Authorization

[API-Key](../README.md#API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully got Block by id |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_block**
> BlockResult get_current_block()

Get current Block

Get current Block

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
    api_instance = radiomanager_sdk.BlockApi(api_client)
    
    try:
        # Get current Block
        api_response = api_instance.get_current_block()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BlockApi->get_current_block: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BlockResult**](BlockResult.md)

### Authorization

[API-Key](../README.md#API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully got current Block |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_next_block**
> BlockResult get_next_block()

Get upcoming Block

Get upcoming Block

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
    api_instance = radiomanager_sdk.BlockApi(api_client)
    
    try:
        # Get upcoming Block
        api_response = api_instance.get_next_block()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BlockApi->get_next_block: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BlockResult**](BlockResult.md)

### Authorization

[API-Key](../README.md#API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully got upcoming Block |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_blocks**
> BlockResults list_blocks(page=page, broadcast_id=broadcast_id, item_id=item_id, program_id=program_id, start_min=start_min, start_max=start_max, limit=limit, order_by=order_by, order_direction=order_direction, external_station_id=external_station_id)

Get a list of all blocks currently in your station.

Get a list of all blocks currently in your station. This feature supports pagination and will give a maximum of 50 blocks back.

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
    api_instance = radiomanager_sdk.BlockApi(api_client)
    page = 1 # int | Current page *(Optional)* (optional) (default to 1)
broadcast_id = 56 # int | Search on Broadcast ID *(Optional)* `(Relation)` (optional)
item_id = 56 # int | Search on Item ID *(Optional)* `(Relation)` (optional)
program_id = 56 # int | Search on Program ID *(Optional)* `(Relation)` (optional)
start_min = '2013-10-20T19:20:30+01:00' # datetime | Minimum start date *(Optional)* (optional)
start_max = '2013-10-20T19:20:30+01:00' # datetime | Maximum start date *(Optional)* (optional)
limit = 56 # int | Results per page *(Optional)* (optional)
order_by = 'order_by_example' # str | Field to order the results *(Optional)* (optional)
order_direction = 'order_direction_example' # str | Direction of ordering *(Optional)* (optional)
external_station_id = 56 # int | Query on a different (content providing) station *(Optional)* (optional)

    try:
        # Get a list of all blocks currently in your station.
        api_response = api_instance.list_blocks(page=page, broadcast_id=broadcast_id, item_id=item_id, program_id=program_id, start_min=start_min, start_max=start_max, limit=limit, order_by=order_by, order_direction=order_direction, external_station_id=external_station_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BlockApi->list_blocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Current page *(Optional)* | [optional] [default to 1]
 **broadcast_id** | **int**| Search on Broadcast ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **item_id** | **int**| Search on Item ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **program_id** | **int**| Search on Program ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **start_min** | **datetime**| Minimum start date *(Optional)* | [optional] 
 **start_max** | **datetime**| Maximum start date *(Optional)* | [optional] 
 **limit** | **int**| Results per page *(Optional)* | [optional] 
 **order_by** | **str**| Field to order the results *(Optional)* | [optional] 
 **order_direction** | **str**| Direction of ordering *(Optional)* | [optional] 
 **external_station_id** | **int**| Query on a different (content providing) station *(Optional)* | [optional] 

### Return type

[**BlockResults**](BlockResults.md)

### Authorization

[API-Key](../README.md#API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully got all blocks |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

