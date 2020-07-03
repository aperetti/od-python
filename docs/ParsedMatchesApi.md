# od_python.ParsedMatchesApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parsed_matches_get**](ParsedMatchesApi.md#parsed_matches_get) | **GET** /parsedMatches | GET /parsedMatches


# **parsed_matches_get**
> list[InlineResponse20011] parsed_matches_get(less_than_match_id=less_than_match_id)

GET /parsedMatches

Get list of parsed match IDs

### Example 
```python
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.ParsedMatchesApi()
less_than_match_id = 56 # int | Get matches with a match ID lower than this value (optional)

try: 
    # GET /parsedMatches
    api_response = api_instance.parsed_matches_get(less_than_match_id=less_than_match_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ParsedMatchesApi->parsed_matches_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **less_than_match_id** | **int**| Get matches with a match ID lower than this value | [optional] 

### Return type

[**list[InlineResponse20011]**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

