# radiomanager_sdk.StationApi

All URIs are relative to *https://radiomanager.io/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_station**](StationApi.md#get_station) | **GET** /station | Get own station only


# **get_station**
> StationResult get_station()

Get own station only

Get own station only

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
api_instance = radiomanager_sdk.StationApi()

try: 
    # Get own station only
    api_response = api_instance.get_station()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StationApi->get_station: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StationResult**](StationResult.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

