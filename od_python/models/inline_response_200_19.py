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


class InlineResponse20019(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, match_id=None, player_slot=None, radiant_win=None, duration=None, game_mode=None, lobby_type=None, hero_id=None, start_time=None, version=None, kills=None, deaths=None, assists=None, skill=None, lane=None, lane_role=None, is_roaming=None, cluster=None, leaver_status=None, party_size=None):
        """
        InlineResponse20019 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'match_id': 'int',
            'player_slot': 'int',
            'radiant_win': 'bool',
            'duration': 'int',
            'game_mode': 'int',
            'lobby_type': 'int',
            'hero_id': 'int',
            'start_time': 'int',
            'version': 'int',
            'kills': 'int',
            'deaths': 'int',
            'assists': 'int',
            'skill': 'int',
            'lane': 'int',
            'lane_role': 'int',
            'is_roaming': 'bool',
            'cluster': 'int',
            'leaver_status': 'int',
            'party_size': 'int'
        }

        self.attribute_map = {
            'match_id': 'match_id',
            'player_slot': 'player_slot',
            'radiant_win': 'radiant_win',
            'duration': 'duration',
            'game_mode': 'game_mode',
            'lobby_type': 'lobby_type',
            'hero_id': 'hero_id',
            'start_time': 'start_time',
            'version': 'version',
            'kills': 'kills',
            'deaths': 'deaths',
            'assists': 'assists',
            'skill': 'skill',
            'lane': 'lane',
            'lane_role': 'lane_role',
            'is_roaming': 'is_roaming',
            'cluster': 'cluster',
            'leaver_status': 'leaver_status',
            'party_size': 'party_size'
        }

        self._match_id = match_id
        self._player_slot = player_slot
        self._radiant_win = radiant_win
        self._duration = duration
        self._game_mode = game_mode
        self._lobby_type = lobby_type
        self._hero_id = hero_id
        self._start_time = start_time
        self._version = version
        self._kills = kills
        self._deaths = deaths
        self._assists = assists
        self._skill = skill
        self._lane = lane
        self._lane_role = lane_role
        self._is_roaming = is_roaming
        self._cluster = cluster
        self._leaver_status = leaver_status
        self._party_size = party_size

    @property
    def match_id(self):
        """
        Gets the match_id of this InlineResponse20019.
        Match ID

        :return: The match_id of this InlineResponse20019.
        :rtype: int
        """
        return self._match_id

    @match_id.setter
    def match_id(self, match_id):
        """
        Sets the match_id of this InlineResponse20019.
        Match ID

        :param match_id: The match_id of this InlineResponse20019.
        :type: int
        """

        self._match_id = match_id

    @property
    def player_slot(self):
        """
        Gets the player_slot of this InlineResponse20019.
        Which slot the player is in. 0-127 are Radiant, 128-255 are Dire

        :return: The player_slot of this InlineResponse20019.
        :rtype: int
        """
        return self._player_slot

    @player_slot.setter
    def player_slot(self, player_slot):
        """
        Sets the player_slot of this InlineResponse20019.
        Which slot the player is in. 0-127 are Radiant, 128-255 are Dire

        :param player_slot: The player_slot of this InlineResponse20019.
        :type: int
        """

        self._player_slot = player_slot

    @property
    def radiant_win(self):
        """
        Gets the radiant_win of this InlineResponse20019.
        Boolean indicating whether Radiant won the match

        :return: The radiant_win of this InlineResponse20019.
        :rtype: bool
        """
        return self._radiant_win

    @radiant_win.setter
    def radiant_win(self, radiant_win):
        """
        Sets the radiant_win of this InlineResponse20019.
        Boolean indicating whether Radiant won the match

        :param radiant_win: The radiant_win of this InlineResponse20019.
        :type: bool
        """

        self._radiant_win = radiant_win

    @property
    def duration(self):
        """
        Gets the duration of this InlineResponse20019.
        Duration of the game in seconds

        :return: The duration of this InlineResponse20019.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this InlineResponse20019.
        Duration of the game in seconds

        :param duration: The duration of this InlineResponse20019.
        :type: int
        """

        self._duration = duration

    @property
    def game_mode(self):
        """
        Gets the game_mode of this InlineResponse20019.
        Integer corresponding to game mode played. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/game_mode.json

        :return: The game_mode of this InlineResponse20019.
        :rtype: int
        """
        return self._game_mode

    @game_mode.setter
    def game_mode(self, game_mode):
        """
        Sets the game_mode of this InlineResponse20019.
        Integer corresponding to game mode played. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/game_mode.json

        :param game_mode: The game_mode of this InlineResponse20019.
        :type: int
        """

        self._game_mode = game_mode

    @property
    def lobby_type(self):
        """
        Gets the lobby_type of this InlineResponse20019.
        Integer corresponding to lobby type of match. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/lobby_type.json

        :return: The lobby_type of this InlineResponse20019.
        :rtype: int
        """
        return self._lobby_type

    @lobby_type.setter
    def lobby_type(self, lobby_type):
        """
        Sets the lobby_type of this InlineResponse20019.
        Integer corresponding to lobby type of match. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/lobby_type.json

        :param lobby_type: The lobby_type of this InlineResponse20019.
        :type: int
        """

        self._lobby_type = lobby_type

    @property
    def hero_id(self):
        """
        Gets the hero_id of this InlineResponse20019.
        The ID value of the hero played

        :return: The hero_id of this InlineResponse20019.
        :rtype: int
        """
        return self._hero_id

    @hero_id.setter
    def hero_id(self, hero_id):
        """
        Sets the hero_id of this InlineResponse20019.
        The ID value of the hero played

        :param hero_id: The hero_id of this InlineResponse20019.
        :type: int
        """

        self._hero_id = hero_id

    @property
    def start_time(self):
        """
        Gets the start_time of this InlineResponse20019.
        Start time of the match in seconds elapsed since 1970

        :return: The start_time of this InlineResponse20019.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this InlineResponse20019.
        Start time of the match in seconds elapsed since 1970

        :param start_time: The start_time of this InlineResponse20019.
        :type: int
        """

        self._start_time = start_time

    @property
    def version(self):
        """
        Gets the version of this InlineResponse20019.
        version

        :return: The version of this InlineResponse20019.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this InlineResponse20019.
        version

        :param version: The version of this InlineResponse20019.
        :type: int
        """

        self._version = version

    @property
    def kills(self):
        """
        Gets the kills of this InlineResponse20019.
        Total kills the player had at the end of the match

        :return: The kills of this InlineResponse20019.
        :rtype: int
        """
        return self._kills

    @kills.setter
    def kills(self, kills):
        """
        Sets the kills of this InlineResponse20019.
        Total kills the player had at the end of the match

        :param kills: The kills of this InlineResponse20019.
        :type: int
        """

        self._kills = kills

    @property
    def deaths(self):
        """
        Gets the deaths of this InlineResponse20019.
        Total deaths the player had at the end of the match

        :return: The deaths of this InlineResponse20019.
        :rtype: int
        """
        return self._deaths

    @deaths.setter
    def deaths(self, deaths):
        """
        Sets the deaths of this InlineResponse20019.
        Total deaths the player had at the end of the match

        :param deaths: The deaths of this InlineResponse20019.
        :type: int
        """

        self._deaths = deaths

    @property
    def assists(self):
        """
        Gets the assists of this InlineResponse20019.
        Total assists the player had at the end of the match

        :return: The assists of this InlineResponse20019.
        :rtype: int
        """
        return self._assists

    @assists.setter
    def assists(self, assists):
        """
        Sets the assists of this InlineResponse20019.
        Total assists the player had at the end of the match

        :param assists: The assists of this InlineResponse20019.
        :type: int
        """

        self._assists = assists

    @property
    def skill(self):
        """
        Gets the skill of this InlineResponse20019.
        Skill bracket assigned by Valve (Normal, High, Very High)

        :return: The skill of this InlineResponse20019.
        :rtype: int
        """
        return self._skill

    @skill.setter
    def skill(self, skill):
        """
        Sets the skill of this InlineResponse20019.
        Skill bracket assigned by Valve (Normal, High, Very High)

        :param skill: The skill of this InlineResponse20019.
        :type: int
        """

        self._skill = skill

    @property
    def lane(self):
        """
        Gets the lane of this InlineResponse20019.
        Integer corresponding to which lane the player laned in for the match

        :return: The lane of this InlineResponse20019.
        :rtype: int
        """
        return self._lane

    @lane.setter
    def lane(self, lane):
        """
        Sets the lane of this InlineResponse20019.
        Integer corresponding to which lane the player laned in for the match

        :param lane: The lane of this InlineResponse20019.
        :type: int
        """

        self._lane = lane

    @property
    def lane_role(self):
        """
        Gets the lane_role of this InlineResponse20019.
        lane_role

        :return: The lane_role of this InlineResponse20019.
        :rtype: int
        """
        return self._lane_role

    @lane_role.setter
    def lane_role(self, lane_role):
        """
        Sets the lane_role of this InlineResponse20019.
        lane_role

        :param lane_role: The lane_role of this InlineResponse20019.
        :type: int
        """

        self._lane_role = lane_role

    @property
    def is_roaming(self):
        """
        Gets the is_roaming of this InlineResponse20019.
        Boolean describing whether or not the player roamed

        :return: The is_roaming of this InlineResponse20019.
        :rtype: bool
        """
        return self._is_roaming

    @is_roaming.setter
    def is_roaming(self, is_roaming):
        """
        Sets the is_roaming of this InlineResponse20019.
        Boolean describing whether or not the player roamed

        :param is_roaming: The is_roaming of this InlineResponse20019.
        :type: bool
        """

        self._is_roaming = is_roaming

    @property
    def cluster(self):
        """
        Gets the cluster of this InlineResponse20019.
        cluster

        :return: The cluster of this InlineResponse20019.
        :rtype: int
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """
        Sets the cluster of this InlineResponse20019.
        cluster

        :param cluster: The cluster of this InlineResponse20019.
        :type: int
        """

        self._cluster = cluster

    @property
    def leaver_status(self):
        """
        Gets the leaver_status of this InlineResponse20019.
        Integer describing whether or not the player left the game. 0: didn't leave. 1: left safely. 2+: Abandoned

        :return: The leaver_status of this InlineResponse20019.
        :rtype: int
        """
        return self._leaver_status

    @leaver_status.setter
    def leaver_status(self, leaver_status):
        """
        Sets the leaver_status of this InlineResponse20019.
        Integer describing whether or not the player left the game. 0: didn't leave. 1: left safely. 2+: Abandoned

        :param leaver_status: The leaver_status of this InlineResponse20019.
        :type: int
        """

        self._leaver_status = leaver_status

    @property
    def party_size(self):
        """
        Gets the party_size of this InlineResponse20019.
        Size of the players party. If not in a party, will return 1.

        :return: The party_size of this InlineResponse20019.
        :rtype: int
        """
        return self._party_size

    @party_size.setter
    def party_size(self, party_size):
        """
        Sets the party_size of this InlineResponse20019.
        Size of the players party. If not in a party, will return 1.

        :param party_size: The party_size of this InlineResponse20019.
        :type: int
        """

        self._party_size = party_size

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
