# radiomanager_sdk.GenreApi

All URIs are relative to *https://radiomanager.io/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_genre_by_id**](GenreApi.md#get_genre_by_id) | **GET** /genres/{id} | Get genre by id
[**list_genres**](GenreApi.md#list_genres) | **GET** /genres | List all genres.


# **get_genre_by_id**
> GenreResult get_genre_by_id(id, external_station_id=external_station_id)

Get genre by id

Get genre by id

### Example
```python
from __future__ import print_function
import time
import radiomanager_sdk
from radiomanager_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
configuration = radiomanager_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = radiomanager_sdk.GenreApi(radiomanager_sdk.ApiClient(configuration))
id = 789 # int | ID of Genre **(Required)**
external_station_id = 789 # int | Query on a different (content providing) station *(Optional)* (optional)

try:
    # Get genre by id
    api_response = api_instance.get_genre_by_id(id, external_station_id=external_station_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenreApi->get_genre_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Genre **(Required)** | 
 **external_station_id** | **int**| Query on a different (content providing) station *(Optional)* | [optional] 

### Return type

[**GenreResult**](GenreResult.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_genres**
> GenreResults list_genres(page=page, parent_id=parent_id, program_id=program_id, broadcast_id=broadcast_id, limit=limit, order_by=order_by, order_direction=order_direction, external_station_id=external_station_id)

List all genres.

List all genres.

### Example
```python
from __future__ import print_function
import time
import radiomanager_sdk
from radiomanager_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
configuration = radiomanager_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = radiomanager_sdk.GenreApi(radiomanager_sdk.ApiClient(configuration))
page = 789 # int | Current page *(Optional)* (optional)
parent_id = 789 # int | Search on Parent ID of Genre *(Optional)* (optional)
program_id = 789 # int | Search on Program ID *(Optional)* `(Relation)` (optional)
broadcast_id = 789 # int | Search on Broadcast ID *(Optional)* `(Relation)` (optional)
limit = 789 # int | Results per page *(Optional)* (optional)
order_by = 'order_by_example' # str | Field to order the results *(Optional)* (optional)
order_direction = 'order_direction_example' # str | Direction of ordering *(Optional)* (optional)
external_station_id = 789 # int | Query on a different (content providing) station *(Optional)* (optional)

try:
    # List all genres.
    api_response = api_instance.list_genres(page=page, parent_id=parent_id, program_id=program_id, broadcast_id=broadcast_id, limit=limit, order_by=order_by, order_direction=order_direction, external_station_id=external_station_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenreApi->list_genres: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Current page *(Optional)* | [optional] 
 **parent_id** | **int**| Search on Parent ID of Genre *(Optional)* | [optional] 
 **program_id** | **int**| Search on Program ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **broadcast_id** | **int**| Search on Broadcast ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **limit** | **int**| Results per page *(Optional)* | [optional] 
 **order_by** | **str**| Field to order the results *(Optional)* | [optional] 
 **order_direction** | **str**| Direction of ordering *(Optional)* | [optional] 
 **external_station_id** | **int**| Query on a different (content providing) station *(Optional)* | [optional] 

### Return type

[**GenreResults**](GenreResults.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

