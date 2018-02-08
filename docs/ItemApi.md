# radiomanager_sdk.ItemApi

All URIs are relative to *https://staging.radiomanager.io/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item**](ItemApi.md#create_item) | **POST** /items | Create an new item.
[**current_item_post_structure**](ItemApi.md#current_item_post_structure) | **POST** /items/current/structure | Post a current playing item, keep structure
[**current_item_post_timing**](ItemApi.md#current_item_post_timing) | **POST** /items/current/timing | Post a current playing item
[**delete_item_by_id**](ItemApi.md#delete_item_by_id) | **DELETE** /items/{id} | Delete item by ID.
[**get_item_by_id**](ItemApi.md#get_item_by_id) | **GET** /items/{id} | Get extended item details by ID.
[**list_items**](ItemApi.md#list_items) | **GET** /items | Get a list of all the items currently in your station.
[**playlist_post_structure**](ItemApi.md#playlist_post_structure) | **POST** /items/playlist/structure | Post a playlist, keep current structure
[**playlist_post_timing**](ItemApi.md#playlist_post_timing) | **POST** /items/playlist/timing | Post a playlist
[**update_item_by_id**](ItemApi.md#update_item_by_id) | **PATCH** /items/{id} | Update extended item details by ID.


# **create_item**
> PostSuccess create_item(data=data)

Create an new item.

Create item.

### Example 
```python
from __future__ import print_function
import time
import radiomanager_sdk
from radiomanager_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
radiomanager_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# radiomanager_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = radiomanager_sdk.ItemApi()
data = radiomanager_sdk.ItemDataInput() # ItemDataInput | Data *(Optional)* (optional)

try: 
    # Create an new item.
    api_response = api_instance.create_item(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->create_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ItemDataInput**](ItemDataInput.md)| Data *(Optional)* | [optional] 

### Return type

[**PostSuccess**](PostSuccess.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **current_item_post_structure**
> Success current_item_post_structure(data=data)

Post a current playing item, keep structure

Post a current playing item, keep structure

### Example 
```python
from __future__ import print_function
import time
import radiomanager_sdk
from radiomanager_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
radiomanager_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# radiomanager_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = radiomanager_sdk.ItemApi()
data = radiomanager_sdk.ImportItem() # ImportItem | Data *(Optional)* (optional)

try: 
    # Post a current playing item, keep structure
    api_response = api_instance.current_item_post_structure(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->current_item_post_structure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ImportItem**](ImportItem.md)| Data *(Optional)* | [optional] 

### Return type

[**Success**](Success.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **current_item_post_timing**
> Success current_item_post_timing(data=data)

Post a current playing item

Post a current playing item

### Example 
```python
from __future__ import print_function
import time
import radiomanager_sdk
from radiomanager_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
radiomanager_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# radiomanager_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = radiomanager_sdk.ItemApi()
data = radiomanager_sdk.ImportItem() # ImportItem | Data *(Optional)* (optional)

try: 
    # Post a current playing item
    api_response = api_instance.current_item_post_timing(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->current_item_post_timing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ImportItem**](ImportItem.md)| Data *(Optional)* | [optional] 

### Return type

[**Success**](Success.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_by_id**
> Success delete_item_by_id(id)

Delete item by ID.

Delete item by id.

### Example 
```python
from __future__ import print_function
import time
import radiomanager_sdk
from radiomanager_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
radiomanager_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# radiomanager_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = radiomanager_sdk.ItemApi()
id = 789 # int | ID of Item **(Required)**

try: 
    # Delete item by ID.
    api_response = api_instance.delete_item_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->delete_item_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Item **(Required)** | 

### Return type

[**Success**](Success.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_by_id**
> ItemResult get_item_by_id(id, external_station_id=external_station_id)

Get extended item details by ID.

Read item by id.

### Example 
```python
from __future__ import print_function
import time
import radiomanager_sdk
from radiomanager_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
radiomanager_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# radiomanager_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = radiomanager_sdk.ItemApi()
id = 789 # int | ID of Item **(Required)**
external_station_id = 789 # int | Query on a different (content providing) station *(Optional)* (optional)

try: 
    # Get extended item details by ID.
    api_response = api_instance.get_item_by_id(id, external_station_id=external_station_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->get_item_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Item **(Required)** | 
 **external_station_id** | **int**| Query on a different (content providing) station *(Optional)* | [optional] 

### Return type

[**ItemResult**](ItemResult.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_items**
> ItemResults list_items(page=page, block_id=block_id, broadcast_id=broadcast_id, model_type_id=model_type_id, tag_id=tag_id, campaign_id=campaign_id, contact_id=contact_id, program_draft_id=program_draft_id, user_draft_id=user_draft_id, station_draft_id=station_draft_id, program_id=program_id, start_min=start_min, start_max=start_max, duration_min=duration_min, duration_max=duration_max, status=status, limit=limit, order_by=order_by, order_direction=order_direction, external_station_id=external_station_id)

Get a list of all the items currently in your station.

Get a list of all the items currently in your station. This feature supports pagination and will give a maximum results of 50 items back.

### Example 
```python
from __future__ import print_function
import time
import radiomanager_sdk
from radiomanager_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
radiomanager_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# radiomanager_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = radiomanager_sdk.ItemApi()
page = 789 # int | Current page *(Optional)* (optional)
block_id = 789 # int | Search on Block ID *(Optional)* `(Relation)` (optional)
broadcast_id = 789 # int | Search on Broadcast ID *(Optional)* `(Relation)` (optional)
model_type_id = 789 # int | Search on ModelType ID *(Optional)* `(Relation)` (optional)
tag_id = 789 # int | Search on Tag ID *(Optional)* `(Relation)` (optional)
campaign_id = 789 # int | Search on Campaign ID *(Optional)* `(Relation)` (optional)
contact_id = 789 # int | Search on Contact ID *(Optional)* `(Relation)` (optional)
program_draft_id = 789 # int | Search on Program Draft ID *(Optional)* (optional)
user_draft_id = 789 # int | Search on User Draft ID *(Optional)* (optional)
station_draft_id = 789 # int | Search on Station Draft ID *(Optional)* (optional)
program_id = 789 # int | Search on Program ID *(Optional)* `(Relation)` (optional)
start_min = '2013-10-20T19:20:30+01:00' # datetime | Minimum start date *(Optional)* (optional)
start_max = '2013-10-20T19:20:30+01:00' # datetime | Maximum start date *(Optional)* (optional)
duration_min = 56 # int | Minimum duration (seconds) *(Optional)* (optional)
duration_max = 56 # int | Maximum duration (seconds) *(Optional)* (optional)
status = 'status_example' # str | Play Status of item *(Optional)* (optional)
limit = 789 # int | Results per page *(Optional)* (optional)
order_by = 'order_by_example' # str | Field to order the results *(Optional)* (optional)
order_direction = 'order_direction_example' # str | Direction of ordering *(Optional)* (optional)
external_station_id = 789 # int | Query on a different (content providing) station *(Optional)* (optional)

try: 
    # Get a list of all the items currently in your station.
    api_response = api_instance.list_items(page=page, block_id=block_id, broadcast_id=broadcast_id, model_type_id=model_type_id, tag_id=tag_id, campaign_id=campaign_id, contact_id=contact_id, program_draft_id=program_draft_id, user_draft_id=user_draft_id, station_draft_id=station_draft_id, program_id=program_id, start_min=start_min, start_max=start_max, duration_min=duration_min, duration_max=duration_max, status=status, limit=limit, order_by=order_by, order_direction=order_direction, external_station_id=external_station_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->list_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Current page *(Optional)* | [optional] 
 **block_id** | **int**| Search on Block ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **broadcast_id** | **int**| Search on Broadcast ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **model_type_id** | **int**| Search on ModelType ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **tag_id** | **int**| Search on Tag ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **campaign_id** | **int**| Search on Campaign ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **contact_id** | **int**| Search on Contact ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **program_draft_id** | **int**| Search on Program Draft ID *(Optional)* | [optional] 
 **user_draft_id** | **int**| Search on User Draft ID *(Optional)* | [optional] 
 **station_draft_id** | **int**| Search on Station Draft ID *(Optional)* | [optional] 
 **program_id** | **int**| Search on Program ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **start_min** | **datetime**| Minimum start date *(Optional)* | [optional] 
 **start_max** | **datetime**| Maximum start date *(Optional)* | [optional] 
 **duration_min** | **int**| Minimum duration (seconds) *(Optional)* | [optional] 
 **duration_max** | **int**| Maximum duration (seconds) *(Optional)* | [optional] 
 **status** | **str**| Play Status of item *(Optional)* | [optional] 
 **limit** | **int**| Results per page *(Optional)* | [optional] 
 **order_by** | **str**| Field to order the results *(Optional)* | [optional] 
 **order_direction** | **str**| Direction of ordering *(Optional)* | [optional] 
 **external_station_id** | **int**| Query on a different (content providing) station *(Optional)* | [optional] 

### Return type

[**ItemResults**](ItemResults.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlist_post_structure**
> InlineResponse202 playlist_post_structure(data=data)

Post a playlist, keep current structure

Post a playlist, keep current structure

### Example 
```python
from __future__ import print_function
import time
import radiomanager_sdk
from radiomanager_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
radiomanager_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# radiomanager_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = radiomanager_sdk.ItemApi()
data = radiomanager_sdk.Data1() # Data1 | Data *(Optional)* (optional)

try: 
    # Post a playlist, keep current structure
    api_response = api_instance.playlist_post_structure(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->playlist_post_structure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data1**](Data1.md)| Data *(Optional)* | [optional] 

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **playlist_post_timing**
> InlineResponse202 playlist_post_timing(data=data)

Post a playlist

Post a playlist

### Example 
```python
from __future__ import print_function
import time
import radiomanager_sdk
from radiomanager_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
radiomanager_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# radiomanager_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = radiomanager_sdk.ItemApi()
data = radiomanager_sdk.Data() # Data | Data *(Optional)* (optional)

try: 
    # Post a playlist
    api_response = api_instance.playlist_post_timing(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->playlist_post_timing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data**](Data.md)| Data *(Optional)* | [optional] 

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_by_id**
> Success update_item_by_id(id, data=data)

Update extended item details by ID.

Update item by id.

### Example 
```python
from __future__ import print_function
import time
import radiomanager_sdk
from radiomanager_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
radiomanager_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# radiomanager_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = radiomanager_sdk.ItemApi()
id = 789 # int | ID of Item **(Required)**
data = radiomanager_sdk.ItemDataInput() # ItemDataInput | Data *(Optional)* (optional)

try: 
    # Update extended item details by ID.
    api_response = api_instance.update_item_by_id(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->update_item_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Item **(Required)** | 
 **data** | [**ItemDataInput**](ItemDataInput.md)| Data *(Optional)* | [optional] 

### Return type

[**Success**](Success.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

