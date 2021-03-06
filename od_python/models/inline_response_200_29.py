# coding: utf-8

"""
    OpenDota API

    # Introduction The OpenDota API provides Dota 2 related data including advanced match data extracted from match replays.  You can find data that can be used to convert hero and ability IDs and other information provided by the API from the [dotaconstants](https://github.com/odota/dotaconstants) repository.  **Beginning 2018-04-22, the OpenDota API is limited to 50,000 free calls per month and 60 requests/minute** We offer a Premium Tier with unlimited API calls and higher rate limits. Check out the [API page](https://www.opendota.com/api-keys) to learn more. 

    OpenAPI spec version: 18.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class InlineResponse20029(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, match_id=None, cluster=None, replay_salt=None):
        """
        InlineResponse20029 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'match_id': 'int',
            'cluster': 'int',
            'replay_salt': 'int'
        }

        self.attribute_map = {
            'match_id': 'match_id',
            'cluster': 'cluster',
            'replay_salt': 'replay_salt'
        }

        self._match_id = match_id
        self._cluster = cluster
        self._replay_salt = replay_salt

    @property
    def match_id(self):
        """
        Gets the match_id of this InlineResponse20029.
        match_id

        :return: The match_id of this InlineResponse20029.
        :rtype: int
        """
        return self._match_id

    @match_id.setter
    def match_id(self, match_id):
        """
        Sets the match_id of this InlineResponse20029.
        match_id

        :param match_id: The match_id of this InlineResponse20029.
        :type: int
        """

        self._match_id = match_id

    @property
    def cluster(self):
        """
        Gets the cluster of this InlineResponse20029.
        cluster

        :return: The cluster of this InlineResponse20029.
        :rtype: int
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """
        Sets the cluster of this InlineResponse20029.
        cluster

        :param cluster: The cluster of this InlineResponse20029.
        :type: int
        """

        self._cluster = cluster

    @property
    def replay_salt(self):
        """
        Gets the replay_salt of this InlineResponse20029.
        replay_salt

        :return: The replay_salt of this InlineResponse20029.
        :rtype: int
        """
        return self._replay_salt

    @replay_salt.setter
    def replay_salt(self, replay_salt):
        """
        Sets the replay_salt of this InlineResponse20029.
        replay_salt

        :param replay_salt: The replay_salt of this InlineResponse20029.
        :type: int
        """

        self._replay_salt = replay_salt

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
