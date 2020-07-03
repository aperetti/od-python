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


class InlineResponse200Result(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, gold_per_min=None, xp_per_min=None, kills_per_min=None, last_hits_per_min=None, hero_damage_per_min=None, hero_healing_per_min=None, tower_damage=None):
        """
        InlineResponse200Result - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'gold_per_min': 'list[InlineResponse200ResultGoldPerMin]',
            'xp_per_min': 'list[InlineResponse200ResultGoldPerMin]',
            'kills_per_min': 'list[InlineResponse200ResultGoldPerMin]',
            'last_hits_per_min': 'list[InlineResponse200ResultGoldPerMin]',
            'hero_damage_per_min': 'list[InlineResponse200ResultGoldPerMin]',
            'hero_healing_per_min': 'list[InlineResponse200ResultGoldPerMin]',
            'tower_damage': 'list[InlineResponse200ResultGoldPerMin]'
        }

        self.attribute_map = {
            'gold_per_min': 'gold_per_min',
            'xp_per_min': 'xp_per_min',
            'kills_per_min': 'kills_per_min',
            'last_hits_per_min': 'last_hits_per_min',
            'hero_damage_per_min': 'hero_damage_per_min',
            'hero_healing_per_min': 'hero_healing_per_min',
            'tower_damage': 'tower_damage'
        }

        self._gold_per_min = gold_per_min
        self._xp_per_min = xp_per_min
        self._kills_per_min = kills_per_min
        self._last_hits_per_min = last_hits_per_min
        self._hero_damage_per_min = hero_damage_per_min
        self._hero_healing_per_min = hero_healing_per_min
        self._tower_damage = tower_damage

    @property
    def gold_per_min(self):
        """
        Gets the gold_per_min of this InlineResponse200Result.


        :return: The gold_per_min of this InlineResponse200Result.
        :rtype: list[InlineResponse200ResultGoldPerMin]
        """
        return self._gold_per_min

    @gold_per_min.setter
    def gold_per_min(self, gold_per_min):
        """
        Sets the gold_per_min of this InlineResponse200Result.


        :param gold_per_min: The gold_per_min of this InlineResponse200Result.
        :type: list[InlineResponse200ResultGoldPerMin]
        """

        self._gold_per_min = gold_per_min

    @property
    def xp_per_min(self):
        """
        Gets the xp_per_min of this InlineResponse200Result.


        :return: The xp_per_min of this InlineResponse200Result.
        :rtype: list[InlineResponse200ResultGoldPerMin]
        """
        return self._xp_per_min

    @xp_per_min.setter
    def xp_per_min(self, xp_per_min):
        """
        Sets the xp_per_min of this InlineResponse200Result.


        :param xp_per_min: The xp_per_min of this InlineResponse200Result.
        :type: list[InlineResponse200ResultGoldPerMin]
        """

        self._xp_per_min = xp_per_min

    @property
    def kills_per_min(self):
        """
        Gets the kills_per_min of this InlineResponse200Result.


        :return: The kills_per_min of this InlineResponse200Result.
        :rtype: list[InlineResponse200ResultGoldPerMin]
        """
        return self._kills_per_min

    @kills_per_min.setter
    def kills_per_min(self, kills_per_min):
        """
        Sets the kills_per_min of this InlineResponse200Result.


        :param kills_per_min: The kills_per_min of this InlineResponse200Result.
        :type: list[InlineResponse200ResultGoldPerMin]
        """

        self._kills_per_min = kills_per_min

    @property
    def last_hits_per_min(self):
        """
        Gets the last_hits_per_min of this InlineResponse200Result.


        :return: The last_hits_per_min of this InlineResponse200Result.
        :rtype: list[InlineResponse200ResultGoldPerMin]
        """
        return self._last_hits_per_min

    @last_hits_per_min.setter
    def last_hits_per_min(self, last_hits_per_min):
        """
        Sets the last_hits_per_min of this InlineResponse200Result.


        :param last_hits_per_min: The last_hits_per_min of this InlineResponse200Result.
        :type: list[InlineResponse200ResultGoldPerMin]
        """

        self._last_hits_per_min = last_hits_per_min

    @property
    def hero_damage_per_min(self):
        """
        Gets the hero_damage_per_min of this InlineResponse200Result.


        :return: The hero_damage_per_min of this InlineResponse200Result.
        :rtype: list[InlineResponse200ResultGoldPerMin]
        """
        return self._hero_damage_per_min

    @hero_damage_per_min.setter
    def hero_damage_per_min(self, hero_damage_per_min):
        """
        Sets the hero_damage_per_min of this InlineResponse200Result.


        :param hero_damage_per_min: The hero_damage_per_min of this InlineResponse200Result.
        :type: list[InlineResponse200ResultGoldPerMin]
        """

        self._hero_damage_per_min = hero_damage_per_min

    @property
    def hero_healing_per_min(self):
        """
        Gets the hero_healing_per_min of this InlineResponse200Result.


        :return: The hero_healing_per_min of this InlineResponse200Result.
        :rtype: list[InlineResponse200ResultGoldPerMin]
        """
        return self._hero_healing_per_min

    @hero_healing_per_min.setter
    def hero_healing_per_min(self, hero_healing_per_min):
        """
        Sets the hero_healing_per_min of this InlineResponse200Result.


        :param hero_healing_per_min: The hero_healing_per_min of this InlineResponse200Result.
        :type: list[InlineResponse200ResultGoldPerMin]
        """

        self._hero_healing_per_min = hero_healing_per_min

    @property
    def tower_damage(self):
        """
        Gets the tower_damage of this InlineResponse200Result.


        :return: The tower_damage of this InlineResponse200Result.
        :rtype: list[InlineResponse200ResultGoldPerMin]
        """
        return self._tower_damage

    @tower_damage.setter
    def tower_damage(self, tower_damage):
        """
        Sets the tower_damage of this InlineResponse200Result.


        :param tower_damage: The tower_damage of this InlineResponse200Result.
        :type: list[InlineResponse200ResultGoldPerMin]
        """

        self._tower_damage = tower_damage

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
