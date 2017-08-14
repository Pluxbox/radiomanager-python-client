# radiomanager_sdk.ContactApi

All URIs are relative to *http://radiomanager.pb/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact**](ContactApi.md#create_contact) | **POST** /contacts | Create contact.
[**delete_contact_by_id**](ContactApi.md#delete_contact_by_id) | **DELETE** /contacts/{id} | Delete contact by id
[**get_contact_by_id**](ContactApi.md#get_contact_by_id) | **GET** /contacts/{id} | Get contact by id
[**list_contacts**](ContactApi.md#list_contacts) | **GET** /contacts | Get all contacts.
[**update_contact_by_id**](ContactApi.md#update_contact_by_id) | **PATCH** /contacts/{id} | Update contact by id


# **create_contact**
> PostSuccess create_contact(data)

Create contact.

Create contact.

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
api_instance = radiomanager_sdk.ContactApi()
data = radiomanager_sdk.ContactDataInput() # ContactDataInput | Data **(Required)**

try: 
    # Create contact.
    api_response = api_instance.create_contact(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->create_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ContactDataInput**](ContactDataInput.md)| Data **(Required)** | 

### Return type

[**PostSuccess**](PostSuccess.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_by_id**
> Success delete_contact_by_id(id)

Delete contact by id

Delete contact by id

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
api_instance = radiomanager_sdk.ContactApi()
id = 789 # int | ID of Contact **(Required)**

try: 
    # Delete contact by id
    api_response = api_instance.delete_contact_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->delete_contact_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Contact **(Required)** | 

### Return type

[**Success**](Success.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_by_id**
> ContactResult get_contact_by_id(id, external_station_id=external_station_id)

Get contact by id

Get contact by id

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
api_instance = radiomanager_sdk.ContactApi()
id = 789 # int | ID of Contact **(Required)**
external_station_id = 789 # int | Query on a different (content providing) station *(Optional)* (optional)

try: 
    # Get contact by id
    api_response = api_instance.get_contact_by_id(id, external_station_id=external_station_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->get_contact_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Contact **(Required)** | 
 **external_station_id** | **int**| Query on a different (content providing) station *(Optional)* | [optional] 

### Return type

[**ContactResult**](ContactResult.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contacts**
> ContactResults list_contacts(page=page, model_type_id=model_type_id, tag_id=tag_id, item_id=item_id, external_station_id=external_station_id)

Get all contacts.

List all contacts.

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
api_instance = radiomanager_sdk.ContactApi()
page = 1 # int | Current page *(Optional)* (optional) (default to 1)
model_type_id = 789 # int | Search on ModelType ID *(Optional)* (optional)
tag_id = 789 # int | Search on Tag ID *(Optional)* `(Relation)` (optional)
item_id = 789 # int | Search on Item ID *(Optional)* `(Relation)` (optional)
external_station_id = 789 # int | Query on a different (content providing) station *(Optional)* (optional)

try: 
    # Get all contacts.
    api_response = api_instance.list_contacts(page=page, model_type_id=model_type_id, tag_id=tag_id, item_id=item_id, external_station_id=external_station_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->list_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Current page *(Optional)* | [optional] [default to 1]
 **model_type_id** | **int**| Search on ModelType ID *(Optional)* | [optional] 
 **tag_id** | **int**| Search on Tag ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **item_id** | **int**| Search on Item ID *(Optional)* &#x60;(Relation)&#x60; | [optional] 
 **external_station_id** | **int**| Query on a different (content providing) station *(Optional)* | [optional] 

### Return type

[**ContactResults**](ContactResults.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact_by_id**
> Success update_contact_by_id(id, data=data)

Update contact by id

Update contact by id

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
api_instance = radiomanager_sdk.ContactApi()
id = 789 # int | ID of Contact **(Required)**
data = radiomanager_sdk.ContactDataInput() # ContactDataInput | Data *(Optional)* (optional)

try: 
    # Update contact by id
    api_response = api_instance.update_contact_by_id(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->update_contact_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Contact **(Required)** | 
 **data** | [**ContactDataInput**](ContactDataInput.md)| Data *(Optional)* | [optional] 

### Return type

[**Success**](Success.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

