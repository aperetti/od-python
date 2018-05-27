# coding: utf-8

"""
    OpenDota API

    # Introduction The OpenDota API provides Dota 2 related data including advanced match data extracted from match replays. Please keep request rate to approximately 1/s.  **Begining 4/22/2018, the OpenDota API will be limited to 50,000 free calls per month.** We'll be offering a Premium Tier with unlimited API calls and higher rate limits. Check out the [API page](https://www.opendota.com/api-keys) to learn more. 

    OpenAPI spec version: 17.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse20031(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'hero_id': 'int',
        'lane_role': 'int',
        'time': 'int',
        'games': 'str',
        'wins': 'str'
    }

    attribute_map = {
        'hero_id': 'hero_id',
        'lane_role': 'lane_role',
        'time': 'time',
        'games': 'games',
        'wins': 'wins'
    }

    def __init__(self, hero_id=None, lane_role=None, time=None, games=None, wins=None):
        """
        InlineResponse20031 - a model defined in Swagger
        """

        self._hero_id = None
        self._lane_role = None
        self._time = None
        self._games = None
        self._wins = None

        if hero_id is not None:
          self.hero_id = hero_id
        if lane_role is not None:
          self.lane_role = lane_role
        if time is not None:
          self.time = time
        if games is not None:
          self.games = games
        if wins is not None:
          self.wins = wins

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
        if not isinstance(other, InlineResponse20031):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
