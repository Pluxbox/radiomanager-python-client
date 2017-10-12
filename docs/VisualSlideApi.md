# radiomanager_sdk.VisualSlideApi

All URIs are relative to *https://radiomanager.pb/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_visual_slide**](VisualSlideApi.md#get_visual_slide) | **GET** /visual | Get Visual Slide Image as Base64


# **get_visual_slide**
> VisualResult get_visual_slide()

Get Visual Slide Image as Base64

Get Visual Slide Image as Base64

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
api_instance = radiomanager_sdk.VisualSlideApi()

try: 
    # Get Visual Slide Image as Base64
    api_response = api_instance.get_visual_slide()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisualSlideApi->get_visual_slide: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VisualResult**](VisualResult.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

