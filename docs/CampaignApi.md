# radiomanager_sdk.CampaignApi

All URIs are relative to *http://radiomanager.pb/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_campaign**](CampaignApi.md#create_campaign) | **POST** /campaigns | Create campaign.
[**delete_campaign_by_id**](CampaignApi.md#delete_campaign_by_id) | **DELETE** /campaigns/{id} | Delete campaign by id
[**get_campaign_by_id**](CampaignApi.md#get_campaign_by_id) | **GET** /campaigns/{id} | Get campaign by id
[**list_campaigns**](CampaignApi.md#list_campaigns) | **GET** /campaigns | Get all campaigns.
[**update_campaign_by_id**](CampaignApi.md#update_campaign_by_id) | **PATCH** /campaigns/{id} | Update campaign by id


# **create_campaign**
> PostSuccess create_campaign(data)

Create campaign.

Create campaign.

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
api_instance = radiomanager_sdk.CampaignApi(radiomanager_sdk.ApiClient(configuration))
data = radiomanager_sdk.CampaignDataInput() # CampaignDataInput | Data **(Required)**

try: 
    # Create campaign.
    api_response = api_instance.create_campaign(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignApi->create_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CampaignDataInput**](CampaignDataInput.md)| Data **(Required)** | 

### Return type

[**PostSuccess**](PostSuccess.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_campaign_by_id**
> Success delete_campaign_by_id(id)

Delete campaign by id

Delete campaign by id

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
api_instance = radiomanager_sdk.CampaignApi(radiomanager_sdk.ApiClient(configuration))
id = 789 # int | ID of Campaign **(Required)**

try: 
    # Delete campaign by id
    api_response = api_instance.delete_campaign_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignApi->delete_campaign_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Campaign **(Required)** | 

### Return type

[**Success**](Success.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_by_id**
> CampaignResult get_campaign_by_id(id, external_station_id=external_station_id)

Get campaign by id

Get campaign by id

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
api_instance = radiomanager_sdk.CampaignApi(radiomanager_sdk.ApiClient(configuration))
id = 789 # int | ID of Campaign **(Required)**
external_station_id = 789 # int | Query on a different (content providing) station *(Optional)* (optional)

try: 
    # Get campaign by id
    api_response = api_instance.get_campaign_by_id(id, external_station_id=external_station_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignApi->get_campaign_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Campaign **(Required)** | 
 **external_station_id** | **int**| Query on a different (content providing) station *(Optional)* | [optional] 

### Return type

[**CampaignResult**](CampaignResult.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_campaigns**
> CampaignResults list_campaigns(page=page, model_type_id=model_type_id, item_id=item_id, start_min=start_min, start_max=start_max, external_station_id=external_station_id)

Get all campaigns.

List all campaigns.

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
api_instance = radiomanager_sdk.CampaignApi(radiomanager_sdk.ApiClient(configuration))
page = 789 # int | Current page *(Optional)* (optional)
model_type_id = 789 # int | Search on ModelType ID *(Optional)* (optional)
item_id = 789 # int | Search on Item ID *(Optional)* `(Relation)` (optional)
start_min = '2013-10-20T19:20:30+01:00' # datetime | Minimum start date *(Optional)* (optional)
start_max = '2013-10-20T19:20:30+01:00' # datetime | Maximum start date *(Optional)* (optional)
external_station_id = 789 # int | Query on a different (content providing) station *(Optional)* (optional)

try: 
    # Get all campaigns.
    api_response = api_instance.list_campaigns(page=page, model_type_id=model_type_id, item_id=item_id, start_min=start_min, start_max=start_max, external_station_id=external_station_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignApi->list_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Current page *(Optional)* | [optional] 
 **model_type_id** | **int**| Search on ModelType ID *(Optional)* | [optional] 
 **item_id** | **int**| Search on Item ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **start_min** | **datetime**| Minimum start date *(Optional)* | [optional] 
 **start_max** | **datetime**| Maximum start date *(Optional)* | [optional] 
 **external_station_id** | **int**| Query on a different (content providing) station *(Optional)* | [optional] 

### Return type

[**CampaignResults**](CampaignResults.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_by_id**
> Success update_campaign_by_id(id, data=data)

Update campaign by id

Update campaign by id

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
api_instance = radiomanager_sdk.CampaignApi(radiomanager_sdk.ApiClient(configuration))
id = 789 # int | ID of Campaign **(Required)**
data = radiomanager_sdk.CampaignDataInput() # CampaignDataInput | Data *(Optional)* (optional)

try: 
    # Update campaign by id
    api_response = api_instance.update_campaign_by_id(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignApi->update_campaign_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Campaign **(Required)** | 
 **data** | [**CampaignDataInput**](CampaignDataInput.md)| Data *(Optional)* | [optional] 

### Return type

[**Success**](Success.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

