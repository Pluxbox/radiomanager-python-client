# radiomanager_sdk.UserApi

All URIs are relative to *https://staging.radiomanager.io/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_by_id**](UserApi.md#delete_user_by_id) | **DELETE** /users/{id} | Remove user from station by Id
[**get_user_by_id**](UserApi.md#get_user_by_id) | **GET** /users/{id} | Get user by id
[**invite_user_by_mail**](UserApi.md#invite_user_by_mail) | **POST** /users/invite | Invite user by mail
[**list_users**](UserApi.md#list_users) | **GET** /users | Get all users.


# **delete_user_by_id**
> Success delete_user_by_id(id)

Remove user from station by Id

Remove user from station by Id

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
api_instance = radiomanager_sdk.UserApi(radiomanager_sdk.ApiClient(configuration))
id = 789 # int | id of User

try:
    # Remove user from station by Id
    api_response = api_instance.delete_user_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of User | 

### Return type

[**Success**](Success.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> UserResult get_user_by_id(id)

Get user by id

Get user by id

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
api_instance = radiomanager_sdk.UserApi(radiomanager_sdk.ApiClient(configuration))
id = 789 # int | id of User

try:
    # Get user by id
    api_response = api_instance.get_user_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of User | 

### Return type

[**UserResult**](UserResult.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_user_by_mail**
> InviteUserSuccess invite_user_by_mail(data)

Invite user by mail

Invite user by mail

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
api_instance = radiomanager_sdk.UserApi(radiomanager_sdk.ApiClient(configuration))
data = radiomanager_sdk.InviteUserData() # InviteUserData | Data **(Required)**

try:
    # Invite user by mail
    api_response = api_instance.invite_user_by_mail(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->invite_user_by_mail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InviteUserData**](InviteUserData.md)| Data **(Required)** | 

### Return type

[**InviteUserSuccess**](InviteUserSuccess.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> UserResults list_users(page=page, role_id=role_id, limit=limit, order_by=order_by, order_direction=order_direction)

Get all users.

List all users.

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
api_instance = radiomanager_sdk.UserApi(radiomanager_sdk.ApiClient(configuration))
page = 1 # int | Current page *(Optional)* (optional) (default to 1)
role_id = 789 # int | Search on Role ID *(Optional)* (optional)
limit = 789 # int | Results per page *(Optional)* (optional)
order_by = 'order_by_example' # str | Field to order the results *(Optional)* (optional)
order_direction = 'order_direction_example' # str | Direction of ordering *(Optional)* (optional)

try:
    # Get all users.
    api_response = api_instance.list_users(page=page, role_id=role_id, limit=limit, order_by=order_by, order_direction=order_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Current page *(Optional)* | [optional] [default to 1]
 **role_id** | **int**| Search on Role ID *(Optional)* | [optional] 
 **limit** | **int**| Results per page *(Optional)* | [optional] 
 **order_by** | **str**| Field to order the results *(Optional)* | [optional] 
 **order_direction** | **str**| Direction of ordering *(Optional)* | [optional] 

### Return type

[**UserResults**](UserResults.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

