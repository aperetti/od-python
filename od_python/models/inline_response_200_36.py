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


class InlineResponse20036(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, hero_id=None, name=None, games_played=None, wins=None):
        """
        InlineResponse20036 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'hero_id': 'int',
            'name': 'str',
            'games_played': 'int',
            'wins': 'int'
        }

        self.attribute_map = {
            'hero_id': 'hero_id',
            'name': 'name',
            'games_played': 'games_played',
            'wins': 'wins'
        }

        self._hero_id = hero_id
        self._name = name
        self._games_played = games_played
        self._wins = wins

    @property
    def hero_id(self):
        """
        Gets the hero_id of this InlineResponse20036.
        The hero ID

        :return: The hero_id of this InlineResponse20036.
        :rtype: int
        """
        return self._hero_id

    @hero_id.setter
    def hero_id(self, hero_id):
        """
        Sets the hero_id of this InlineResponse20036.
        The hero ID

        :param hero_id: The hero_id of this InlineResponse20036.
        :type: int
        """

        self._hero_id = hero_id

    @property
    def name(self):
        """
        Gets the name of this InlineResponse20036.
        The hero name

        :return: The name of this InlineResponse20036.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InlineResponse20036.
        The hero name

        :param name: The name of this InlineResponse20036.
        :type: str
        """

        self._name = name

    @property
    def games_played(self):
        """
        Gets the games_played of this InlineResponse20036.
        Number of games played

        :return: The games_played of this InlineResponse20036.
        :rtype: int
        """
        return self._games_played

    @games_played.setter
    def games_played(self, games_played):
        """
        Sets the games_played of this InlineResponse20036.
        Number of games played

        :param games_played: The games_played of this InlineResponse20036.
        :type: int
        """

        self._games_played = games_played

    @property
    def wins(self):
        """
        Gets the wins of this InlineResponse20036.
        Number of wins

        :return: The wins of this InlineResponse20036.
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """
        Sets the wins of this InlineResponse20036.
        Number of wins

        :param wins: The wins of this InlineResponse20036.
        :type: int
        """

        self._wins = wins

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
