# od_python.ConstantsApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**constants_resource_get**](ConstantsApi.md#constants_resource_get) | **GET** /constants/{resource} | GET /constants


# **constants_resource_get**
> constants_resource_get(resource)

GET /constants

Get static game data mirrored from the dotaconstants repository. If no resource is specified, returns an array of available resources.

### Example 
```python
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.ConstantsApi()
resource = 'resource_example' # str | Resource name e.g. `heroes`. [List of resources](https://github.com/odota/dotaconstants/tree/master/build)

try: 
    # GET /constants
    api_instance.constants_resource_get(resource)
except ApiException as e:
    print "Exception when calling ConstantsApi->constants_resource_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource name e.g. &#x60;heroes&#x60;. [List of resources](https://github.com/odota/dotaconstants/tree/master/build) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

