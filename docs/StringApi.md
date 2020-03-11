# radiomanager_sdk.StringApi

All URIs are relative to *https://radiomanager.io/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_strings_by_name**](StringApi.md#get_strings_by_name) | **GET** /strings/{name} | Get Strings (formatted)


# **get_strings_by_name**
> TextString get_strings_by_name(name, full_model)

Get Strings (formatted)

Get Strings (formatted)

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
    api_instance = radiomanager_sdk.StringApi(api_client)
    name = 'name_example' # str | Name of Strings **(Required)**
full_model = True # bool | Full model or content only **(Required)** (default to True)

    try:
        # Get Strings (formatted)
        api_response = api_instance.get_strings_by_name(name, full_model)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StringApi->get_strings_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of Strings **(Required)** | 
 **full_model** | **bool**| Full model or content only **(Required)** | [default to True]

### Return type

[**TextString**](TextString.md)

### Authorization

[API-Key](../README.md#API-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully got Strings (formatted) |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

