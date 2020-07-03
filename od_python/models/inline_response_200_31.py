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


class InlineResponse20031(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, hero_id=None, lane_role=None, time=None, games=None, wins=None):
        """
        InlineResponse20031 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'hero_id': 'int',
            'lane_role': 'int',
            'time': 'int',
            'games': 'str',
            'wins': 'str'
        }

        self.attribute_map = {
            'hero_id': 'hero_id',
            'lane_role': 'lane_role',
            'time': 'time',
            'games': 'games',
            'wins': 'wins'
        }

        self._hero_id = hero_id
        self._lane_role = lane_role
        self._time = time
        self._games = games
        self._wins = wins

    @property
    def hero_id(self):
        """
        Gets the hero_id of this InlineResponse20031.
        Hero ID

        :return: The hero_id of this InlineResponse20031.
        :rtype: int
        """
        return self._hero_id

    @hero_id.setter
    def hero_id(self, hero_id):
        """
        Sets the hero_id of this InlineResponse20031.
        Hero ID

        :param hero_id: The hero_id of this InlineResponse20031.
        :type: int
        """

        self._hero_id = hero_id

    @property
    def lane_role(self):
        """
        Gets the lane_role of this InlineResponse20031.
        The hero's lane role

        :return: The lane_role of this InlineResponse20031.
        :rtype: int
        """
        return self._lane_role

    @lane_role.setter
    def lane_role(self, lane_role):
        """
        Sets the lane_role of this InlineResponse20031.
        The hero's lane role

        :param lane_role: The lane_role of this InlineResponse20031.
        :type: int
        """

        self._lane_role = lane_role

    @property
    def time(self):
        """
        Gets the time of this InlineResponse20031.
        Maximum game length in seconds

        :return: The time of this InlineResponse20031.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this InlineResponse20031.
        Maximum game length in seconds

        :param time: The time of this InlineResponse20031.
        :type: int
        """

        self._time = time

    @property
    def games(self):
        """
        Gets the games of this InlineResponse20031.
        The number of games where the hero played in this lane role

        :return: The games of this InlineResponse20031.
        :rtype: str
        """
        return self._games

    @games.setter
    def games(self, games):
        """
        Sets the games of this InlineResponse20031.
        The number of games where the hero played in this lane role

        :param games: The games of this InlineResponse20031.
        :type: str
        """

        self._games = games

    @property
    def wins(self):
        """
        Gets the wins of this InlineResponse20031.
        The number of games won where the hero played in this lane role

        :return: The wins of this InlineResponse20031.
        :rtype: str
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """
        Sets the wins of this InlineResponse20031.
        The number of games won where the hero played in this lane role

        :param wins: The wins of this InlineResponse20031.
        :type: str
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
