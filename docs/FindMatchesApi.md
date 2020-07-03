# od_python.FindMatchesApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_matches_get**](FindMatchesApi.md#find_matches_get) | **GET** /findMatches | GET /


# **find_matches_get**
> object find_matches_get(team_a=team_a, team_b=team_b)

GET /

Finds recent matches by heroes played

### Example 
```python
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.FindMatchesApi()
team_a = 56 # int | Hero IDs on first team (array) (optional)
team_b = 56 # int | Hero IDs on second team (array) (optional)

try: 
    # GET /
    api_response = api_instance.find_matches_get(team_a=team_a, team_b=team_b)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FindMatchesApi->find_matches_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_a** | **int**| Hero IDs on first team (array) | [optional] 
 **team_b** | **int**| Hero IDs on second team (array) | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

