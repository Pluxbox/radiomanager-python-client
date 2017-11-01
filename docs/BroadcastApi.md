# radiomanager_sdk.BroadcastApi

All URIs are relative to *https://staging.radiomanager.io/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_broadcast**](BroadcastApi.md#create_broadcast) | **POST** /broadcasts | Create broadcast.
[**delete_broadcast_by_id**](BroadcastApi.md#delete_broadcast_by_id) | **DELETE** /broadcasts/{id} | Delete broadcast by id
[**get_broadcast_by_id**](BroadcastApi.md#get_broadcast_by_id) | **GET** /broadcasts/{id} | Get broadcast by id
[**get_current_broadcast**](BroadcastApi.md#get_current_broadcast) | **GET** /broadcasts/current | Get current Broadcast
[**get_daily_epg**](BroadcastApi.md#get_daily_epg) | **GET** /broadcasts/epg/daily | Get daily EPG
[**get_epg_by_date**](BroadcastApi.md#get_epg_by_date) | **GET** /broadcasts/epg | Get EPG by date
[**get_next_broadcast**](BroadcastApi.md#get_next_broadcast) | **GET** /broadcasts/next | Get next Broadcast
[**get_weekly_epg**](BroadcastApi.md#get_weekly_epg) | **GET** /broadcasts/epg/weekly | Get weekly EPG
[**list_broadcasts**](BroadcastApi.md#list_broadcasts) | **GET** /broadcasts | Get all broadcasts.
[**print_broadcast_by_id**](BroadcastApi.md#print_broadcast_by_id) | **GET** /broadcasts/print/{id} | Print Broadcast by id
[**update_broadcast_by_id**](BroadcastApi.md#update_broadcast_by_id) | **PATCH** /broadcasts/{id} | Update broadcast by id


# **create_broadcast**
> PostSuccess create_broadcast(data)

Create broadcast.

Create broadcast.

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
api_instance = radiomanager_sdk.BroadcastApi()
data = radiomanager_sdk.BroadcastDataInput() # BroadcastDataInput | Data **(Required)**

try: 
    # Create broadcast.
    api_response = api_instance.create_broadcast(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BroadcastApi->create_broadcast: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**BroadcastDataInput**](BroadcastDataInput.md)| Data **(Required)** | 

### Return type

[**PostSuccess**](PostSuccess.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_broadcast_by_id**
> Success delete_broadcast_by_id(id)

Delete broadcast by id

Delete broadcast by id

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
api_instance = radiomanager_sdk.BroadcastApi()
id = 789 # int | ID of Broadcast **(Required)**

try: 
    # Delete broadcast by id
    api_response = api_instance.delete_broadcast_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BroadcastApi->delete_broadcast_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Broadcast **(Required)** | 

### Return type

[**Success**](Success.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_broadcast_by_id**
> BroadcastResult get_broadcast_by_id(id, external_station_id=external_station_id)

Get broadcast by id

Get broadcast by id

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
api_instance = radiomanager_sdk.BroadcastApi()
id = 789 # int | ID of Broadcast **(Required)**
external_station_id = 789 # int | Query on a different (content providing) station *(Optional)* (optional)

try: 
    # Get broadcast by id
    api_response = api_instance.get_broadcast_by_id(id, external_station_id=external_station_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BroadcastApi->get_broadcast_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Broadcast **(Required)** | 
 **external_station_id** | **int**| Query on a different (content providing) station *(Optional)* | [optional] 

### Return type

[**BroadcastResult**](BroadcastResult.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_broadcast**
> BroadcastResult get_current_broadcast(withunpublished=withunpublished)

Get current Broadcast

Get current Broadcast

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
api_instance = radiomanager_sdk.BroadcastApi()
withunpublished = true # bool | Show Unpublished *(Optional)* (optional)

try: 
    # Get current Broadcast
    api_response = api_instance.get_current_broadcast(withunpublished=withunpublished)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BroadcastApi->get_current_broadcast: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **withunpublished** | **bool**| Show Unpublished *(Optional)* | [optional] 

### Return type

[**BroadcastResult**](BroadcastResult.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_daily_epg**
> EPGResults get_daily_epg(date=date, withunpublished=withunpublished)

Get daily EPG

Get current Broadcast

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
api_instance = radiomanager_sdk.BroadcastApi()
date = '2013-10-20T19:20:30+01:00' # datetime | Date *(Optional)* (optional)
withunpublished = true # bool | Show Unpublished *(Optional)* (optional)

try: 
    # Get daily EPG
    api_response = api_instance.get_daily_epg(date=date, withunpublished=withunpublished)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BroadcastApi->get_daily_epg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | **datetime**| Date *(Optional)* | [optional] 
 **withunpublished** | **bool**| Show Unpublished *(Optional)* | [optional] 

### Return type

[**EPGResults**](EPGResults.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_epg_by_date**
> EPGResults get_epg_by_date(date=date, withunpublished=withunpublished)

Get EPG by date

Get EPG by date

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
api_instance = radiomanager_sdk.BroadcastApi()
date = '2013-10-20T19:20:30+01:00' # datetime | Date *(Optional)* (optional)
withunpublished = true # bool | Show Unpublished *(Optional)* (optional)

try: 
    # Get EPG by date
    api_response = api_instance.get_epg_by_date(date=date, withunpublished=withunpublished)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BroadcastApi->get_epg_by_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | **datetime**| Date *(Optional)* | [optional] 
 **withunpublished** | **bool**| Show Unpublished *(Optional)* | [optional] 

### Return type

[**EPGResults**](EPGResults.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_next_broadcast**
> BroadcastResult get_next_broadcast(withunpublished=withunpublished)

Get next Broadcast

Get next Broadcast

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
api_instance = radiomanager_sdk.BroadcastApi()
withunpublished = true # bool | Show Unpublished *(Optional)* (optional)

try: 
    # Get next Broadcast
    api_response = api_instance.get_next_broadcast(withunpublished=withunpublished)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BroadcastApi->get_next_broadcast: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **withunpublished** | **bool**| Show Unpublished *(Optional)* | [optional] 

### Return type

[**BroadcastResult**](BroadcastResult.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_weekly_epg**
> EPGResults get_weekly_epg(date=date, withunpublished=withunpublished)

Get weekly EPG

Get weekly EPG

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
api_instance = radiomanager_sdk.BroadcastApi()
date = 'date_example' # str | Date *(Optional)* (optional)
withunpublished = true # bool | Show Unpublished *(Optional)* (optional)

try: 
    # Get weekly EPG
    api_response = api_instance.get_weekly_epg(date=date, withunpublished=withunpublished)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BroadcastApi->get_weekly_epg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | **str**| Date *(Optional)* | [optional] 
 **withunpublished** | **bool**| Show Unpublished *(Optional)* | [optional] 

### Return type

[**EPGResults**](EPGResults.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_broadcasts**
> BroadcastResults list_broadcasts(page=page, program_id=program_id, block_id=block_id, model_type_id=model_type_id, tag_id=tag_id, presenter_id=presenter_id, genre_id=genre_id, item_id=item_id, start_min=start_min, start_max=start_max, limit=limit, order_by=order_by, order_direction=order_direction, external_station_id=external_station_id)

Get all broadcasts.

List all broadcasts.

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
api_instance = radiomanager_sdk.BroadcastApi()
page = 1 # int | Current page *(Optional)* (optional) (default to 1)
program_id = 789 # int | Search on Program ID *(Optional)* `(Relation)` (optional)
block_id = 789 # int | Search on Block ID *(Optional)* `(Relation)` (optional)
model_type_id = 789 # int | Search on ModelType ID *(Optional)* `(Relation)` (optional)
tag_id = 789 # int | Search on Tag ID *(Optional)* `(Relation)` (optional)
presenter_id = 789 # int | Search on Presenter ID *(Optional)* `(Relation)` (optional)
genre_id = 789 # int | Search on Genre ID *(Optional)* `(Relation)` (optional)
item_id = 789 # int | Search on Item ID *(Optional)* `(Relation)` (optional)
start_min = '2013-10-20T19:20:30+01:00' # datetime | Minimum start date *(Optional)* (optional)
start_max = '2013-10-20T19:20:30+01:00' # datetime | Maximum start date *(Optional)* (optional)
limit = 789 # int | Results per page *(Optional)* (optional)
order_by = 'order_by_example' # str | Field to order the results *(Optional)* (optional)
order_direction = 'order_direction_example' # str | Direction of ordering *(Optional)* (optional)
external_station_id = 789 # int | Query on a different (content providing) station *(Optional)* (optional)

try: 
    # Get all broadcasts.
    api_response = api_instance.list_broadcasts(page=page, program_id=program_id, block_id=block_id, model_type_id=model_type_id, tag_id=tag_id, presenter_id=presenter_id, genre_id=genre_id, item_id=item_id, start_min=start_min, start_max=start_max, limit=limit, order_by=order_by, order_direction=order_direction, external_station_id=external_station_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BroadcastApi->list_broadcasts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Current page *(Optional)* | [optional] [default to 1]
 **program_id** | **int**| Search on Program ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **block_id** | **int**| Search on Block ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **model_type_id** | **int**| Search on ModelType ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **tag_id** | **int**| Search on Tag ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **presenter_id** | **int**| Search on Presenter ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **genre_id** | **int**| Search on Genre ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **item_id** | **int**| Search on Item ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **start_min** | **datetime**| Minimum start date *(Optional)* | [optional] 
 **start_max** | **datetime**| Maximum start date *(Optional)* | [optional] 
 **limit** | **int**| Results per page *(Optional)* | [optional] 
 **order_by** | **str**| Field to order the results *(Optional)* | [optional] 
 **order_direction** | **str**| Direction of ordering *(Optional)* | [optional] 
 **external_station_id** | **int**| Query on a different (content providing) station *(Optional)* | [optional] 

### Return type

[**BroadcastResults**](BroadcastResults.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **print_broadcast_by_id**
> EPGResults print_broadcast_by_id(id, program_id=program_id, presenter_id=presenter_id, tag_id=tag_id)

Print Broadcast by id

Print Broadcast by id

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
api_instance = radiomanager_sdk.BroadcastApi()
id = 789 # int | ID of Broadcast **(Required)**
program_id = 789 # int | Search on Program ID *(Optional)* `(Relation)` (optional)
presenter_id = 789 # int | Search on Presenter ID *(Optional)* `(Relation)` (optional)
tag_id = 789 # int | Search on Tag ID *(Optional)* `(Relation)` (optional)

try: 
    # Print Broadcast by id
    api_response = api_instance.print_broadcast_by_id(id, program_id=program_id, presenter_id=presenter_id, tag_id=tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BroadcastApi->print_broadcast_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Broadcast **(Required)** | 
 **program_id** | **int**| Search on Program ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **presenter_id** | **int**| Search on Presenter ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **tag_id** | **int**| Search on Tag ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 

### Return type

[**EPGResults**](EPGResults.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_broadcast_by_id**
> Success update_broadcast_by_id(id, data=data)

Update broadcast by id

Update broadcast by id

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
api_instance = radiomanager_sdk.BroadcastApi()
id = 789 # int | ID of Broadcast **(Required)**
data = radiomanager_sdk.BroadcastDataInput() # BroadcastDataInput | Data *(Optional)* (optional)

try: 
    # Update broadcast by id
    api_response = api_instance.update_broadcast_by_id(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BroadcastApi->update_broadcast_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Broadcast **(Required)** | 
 **data** | [**BroadcastDataInput**](BroadcastDataInput.md)| Data *(Optional)* | [optional] 

### Return type

[**Success**](Success.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

