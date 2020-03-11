# radiomanager_sdk.PresenterApi

All URIs are relative to *https://radiomanager.io/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_presenter**](PresenterApi.md#create_presenter) | **POST** /presenters | Create presenter.
[**delete_presenter_by_id**](PresenterApi.md#delete_presenter_by_id) | **DELETE** /presenters/{id} | Delete presenter by id
[**get_presenter_by_id**](PresenterApi.md#get_presenter_by_id) | **GET** /presenters/{id} | Get presenter by id
[**list_presenters**](PresenterApi.md#list_presenters) | **GET** /presenters | Get all presenters.
[**update_presenter_by_id**](PresenterApi.md#update_presenter_by_id) | **PATCH** /presenters/{id} | Update presenter by id


# **create_presenter**
> PostSuccess create_presenter(data)

Create presenter.

Create presenter.

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
    api_instance = radiomanager_sdk.PresenterApi(api_client)
    data = radiomanager_sdk.PresenterDataInput() # PresenterDataInput | Data **(Required)**

    try:
        # Create presenter.
        api_response = api_instance.create_presenter(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PresenterApi->create_presenter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PresenterDataInput**](PresenterDataInput.md)| Data **(Required)** | 

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
**200** | Successfully created a presenter |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_presenter_by_id**
> Success delete_presenter_by_id(id)

Delete presenter by id

Delete presenter by id

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
    api_instance = radiomanager_sdk.PresenterApi(api_client)
    id = 0 # int | id of presenter (default to 0)

    try:
        # Delete presenter by id
        api_response = api_instance.delete_presenter_by_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PresenterApi->delete_presenter_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of presenter | [default to 0]

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
**200** | Successfully deleted presenter by id |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_presenter_by_id**
> PresenterResult get_presenter_by_id(id, external_station_id=external_station_id)

Get presenter by id

Get presenter by id

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
    api_instance = radiomanager_sdk.PresenterApi(api_client)
    id = 0 # int | id of Presenter (default to 0)
external_station_id = 56 # int | Query on a different (content providing) station *(Optional)* (optional)

    try:
        # Get presenter by id
        api_response = api_instance.get_presenter_by_id(id, external_station_id=external_station_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PresenterApi->get_presenter_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of Presenter | [default to 0]
 **external_station_id** | **int**| Query on a different (content providing) station *(Optional)* | [optional] 

### Return type

[**PresenterResult**](PresenterResult.md)

### Authorization

[API-Key](../README.md#API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully got Presenter by id |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_presenters**
> PresenterResults list_presenters(page=page, program_id=program_id, broadcast_id=broadcast_id, model_type_id=model_type_id, limit=limit, order_by=order_by, order_direction=order_direction, external_station_id=external_station_id)

Get all presenters.

List all presenters.

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
    api_instance = radiomanager_sdk.PresenterApi(api_client)
    page = 56 # int | Current page *(Optional)* (optional)
program_id = 56 # int | Search on Program ID *(Optional)* `(Relation)` (optional)
broadcast_id = 56 # int | Search on Broadcast ID *(Optional)* `(Relation)` (optional)
model_type_id = 56 # int | Search on ModelType ID (Optional) (optional)
limit = 56 # int | Results per page *(Optional)* (optional)
order_by = 'order_by_example' # str | Field to order the results *(Optional)* (optional)
order_direction = 'order_direction_example' # str | Direction of ordering *(Optional)* (optional)
external_station_id = 56 # int | Query on a different (content providing) station *(Optional)* (optional)

    try:
        # Get all presenters.
        api_response = api_instance.list_presenters(page=page, program_id=program_id, broadcast_id=broadcast_id, model_type_id=model_type_id, limit=limit, order_by=order_by, order_direction=order_direction, external_station_id=external_station_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PresenterApi->list_presenters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Current page *(Optional)* | [optional] 
 **program_id** | **int**| Search on Program ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **broadcast_id** | **int**| Search on Broadcast ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **model_type_id** | **int**| Search on ModelType ID (Optional) | [optional] 
 **limit** | **int**| Results per page *(Optional)* | [optional] 
 **order_by** | **str**| Field to order the results *(Optional)* | [optional] 
 **order_direction** | **str**| Direction of ordering *(Optional)* | [optional] 
 **external_station_id** | **int**| Query on a different (content providing) station *(Optional)* | [optional] 

### Return type

[**PresenterResults**](PresenterResults.md)

### Authorization

[API-Key](../README.md#API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully got all presenters |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_presenter_by_id**
> Success update_presenter_by_id(id, data=data)

Update presenter by id

Update presenter by id

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
    api_instance = radiomanager_sdk.PresenterApi(api_client)
    id = 0 # int | id of Presenter (default to 0)
data = radiomanager_sdk.PresenterDataInput() # PresenterDataInput | Data *(Optional)* (optional)

    try:
        # Update presenter by id
        api_response = api_instance.update_presenter_by_id(id, data=data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PresenterApi->update_presenter_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of Presenter | [default to 0]
 **data** | [**PresenterDataInput**](PresenterDataInput.md)| Data *(Optional)* | [optional] 

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
**200** | Successfully updated Presenter by id |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

