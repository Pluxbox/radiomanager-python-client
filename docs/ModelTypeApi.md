# radiomanager_sdk.ModelTypeApi

All URIs are relative to *https://radiomanager.io/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_model_type_by_id**](ModelTypeApi.md#get_model_type_by_id) | **GET** /model_types/{id} | Get modelType by id
[**list_model_types**](ModelTypeApi.md#list_model_types) | **GET** /model_types | Get all modelTypes.


# **get_model_type_by_id**
> ModelTypeResult get_model_type_by_id(id, external_station_id=external_station_id)

Get modelType by id

Get modelType by id

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
api_instance = radiomanager_sdk.ModelTypeApi()
id = 789 # int | ID of ModelType **(Required)**
external_station_id = 789 # int | Query on a different (content providing) station *(Optional)* (optional)

try: 
    # Get modelType by id
    api_response = api_instance.get_model_type_by_id(id, external_station_id=external_station_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelTypeApi->get_model_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of ModelType **(Required)** | 
 **external_station_id** | **int**| Query on a different (content providing) station *(Optional)* | [optional] 

### Return type

[**ModelTypeResult**](ModelTypeResult.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_model_types**
> ModelTypeResults list_model_types(page=page, program_id=program_id, broadcast_id=broadcast_id, item_id=item_id, campaign_id=campaign_id, presenter_id=presenter_id, contact_id=contact_id, model=model, limit=limit, order_by=order_by, order_direction=order_direction, external_station_id=external_station_id)

Get all modelTypes.

List all modelTypes.

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
api_instance = radiomanager_sdk.ModelTypeApi()
page = 789 # int | Current page *(Optional)* (optional)
program_id = 789 # int | Search on Program ID *(Optional)* (optional)
broadcast_id = 789 # int | Search on Broadcast ID *(Optional)* (optional)
item_id = 789 # int | Search on Item ID *(Optional)* (optional)
campaign_id = 789 # int | Search on Campaign ID *(Optional)* (optional)
presenter_id = 789 # int | Search on Presenter ID *(Optional)* (optional)
contact_id = 789 # int | Search on Contact ID *(Optional)* (optional)
model = 'model_example' # str | Search Modeltypes for certain Model *(Optional)* (optional)
limit = 789 # int | Results per page *(Optional)* (optional)
order_by = 'order_by_example' # str | Field to order the results *(Optional)* (optional)
order_direction = 'order_direction_example' # str | Direction of ordering *(Optional)* (optional)
external_station_id = 789 # int | Query on a different (content providing) station *(Optional)* (optional)

try: 
    # Get all modelTypes.
    api_response = api_instance.list_model_types(page=page, program_id=program_id, broadcast_id=broadcast_id, item_id=item_id, campaign_id=campaign_id, presenter_id=presenter_id, contact_id=contact_id, model=model, limit=limit, order_by=order_by, order_direction=order_direction, external_station_id=external_station_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelTypeApi->list_model_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Current page *(Optional)* | [optional] 
 **program_id** | **int**| Search on Program ID *(Optional)* | [optional] 
 **broadcast_id** | **int**| Search on Broadcast ID *(Optional)* | [optional] 
 **item_id** | **int**| Search on Item ID *(Optional)* | [optional] 
 **campaign_id** | **int**| Search on Campaign ID *(Optional)* | [optional] 
 **presenter_id** | **int**| Search on Presenter ID *(Optional)* | [optional] 
 **contact_id** | **int**| Search on Contact ID *(Optional)* | [optional] 
 **model** | **str**| Search Modeltypes for certain Model *(Optional)* | [optional] 
 **limit** | **int**| Results per page *(Optional)* | [optional] 
 **order_by** | **str**| Field to order the results *(Optional)* | [optional] 
 **order_direction** | **str**| Direction of ordering *(Optional)* | [optional] 
 **external_station_id** | **int**| Query on a different (content providing) station *(Optional)* | [optional] 

### Return type

[**ModelTypeResults**](ModelTypeResults.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

