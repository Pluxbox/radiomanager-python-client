# radiomanager_sdk.ExternalMessageApi

All URIs are relative to *https://staging.radiomanager.pluxbox.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queue_external_message**](ExternalMessageApi.md#queue_external_message) | **POST** /externalmessagequeue | Queue External Message.


# **queue_external_message**
> object queue_external_message(message)

Queue External Message.

Queue External Message.

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
api_instance = radiomanager_sdk.ExternalMessageApi()
message = radiomanager_sdk.ExternalMessageQueueData() # ExternalMessageQueueData | Data **(Required)**

try: 
    # Queue External Message.
    api_response = api_instance.queue_external_message(message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalMessageApi->queue_external_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | [**ExternalMessageQueueData**](ExternalMessageQueueData.md)| Data **(Required)** | 

### Return type

**object**

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

