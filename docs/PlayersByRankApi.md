# od_python.PlayersByRankApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**players_by_rank_get**](PlayersByRankApi.md#players_by_rank_get) | **GET** /playersByRank | GET /playersByRank


# **players_by_rank_get**
> InlineResponse20024 players_by_rank_get()

GET /playersByRank

Players ordered by rank/medal tier

### Example 
```python
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.PlayersByRankApi()

try: 
    # GET /playersByRank
    api_response = api_instance.players_by_rank_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PlayersByRankApi->players_by_rank_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

