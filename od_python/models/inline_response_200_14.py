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


class InlineResponse20014(object):
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
        'match_id': 'int',
        'duration': 'int',
        'start_time': 'int',
        'radiant_team_id': 'int',
        'radiant_name': 'str',
        'dire_team_id': 'int',
        'dire_name': 'str',
        'leagueid': 'int',
        'league_name': 'str',
        'series_id': 'int',
        'series_type': 'int',
        'radiant_score': 'int',
        'dire_score': 'int',
        'radiant_win': 'bool',
        'radiant': 'bool'
    }

    attribute_map = {
        'match_id': 'match_id',
        'duration': 'duration',
        'start_time': 'start_time',
        'radiant_team_id': 'radiant_team_id',
        'radiant_name': 'radiant_name',
        'dire_team_id': 'dire_team_id',
        'dire_name': 'dire_name',
        'leagueid': 'leagueid',
        'league_name': 'league_name',
        'series_id': 'series_id',
        'series_type': 'series_type',
        'radiant_score': 'radiant_score',
        'dire_score': 'dire_score',
        'radiant_win': 'radiant_win',
        'radiant': 'radiant'
    }

    def __init__(self, match_id=None, duration=None, start_time=None, radiant_team_id=None, radiant_name=None, dire_team_id=None, dire_name=None, leagueid=None, league_name=None, series_id=None, series_type=None, radiant_score=None, dire_score=None, radiant_win=None, radiant=None):
        """
        InlineResponse20014 - a model defined in Swagger
        """

        self._match_id = None
        self._duration = None
        self._start_time = None
        self._radiant_team_id = None
        self._radiant_name = None
        self._dire_team_id = None
        self._dire_name = None
        self._leagueid = None
        self._league_name = None
        self._series_id = None
        self._series_type = None
        self._radiant_score = None
        self._dire_score = None
        self._radiant_win = None
        self._radiant = None

        if match_id is not None:
          self.match_id = match_id
        if duration is not None:
          self.duration = duration
        if start_time is not None:
          self.start_time = start_time
        if radiant_team_id is not None:
          self.radiant_team_id = radiant_team_id
        if radiant_name is not None:
          self.radiant_name = radiant_name
        if dire_team_id is not None:
          self.dire_team_id = dire_team_id
        if dire_name is not None:
          self.dire_name = dire_name
        if leagueid is not None:
          self.leagueid = leagueid
        if league_name is not None:
          self.league_name = league_name
        if series_id is not None:
          self.series_id = series_id
        if series_type is not None:
          self.series_type = series_type
        if radiant_score is not None:
          self.radiant_score = radiant_score
        if dire_score is not None:
          self.dire_score = dire_score
        if radiant_win is not None:
          self.radiant_win = radiant_win
        if radiant is not None:
          self.radiant = radiant

    @property
    def match_id(self):
        """
        Gets the match_id of this InlineResponse20014.
        Used to identify individual matches, e.g. 3703866531

        :return: The match_id of this InlineResponse20014.
        :rtype: int
        """
        return self._match_id

    @match_id.setter
    def match_id(self, match_id):
        """
        Sets the match_id of this InlineResponse20014.
        Used to identify individual matches, e.g. 3703866531

        :param match_id: The match_id of this InlineResponse20014.
        :type: int
        """

        self._match_id = match_id

    @property
    def duration(self):
        """
        Gets the duration of this InlineResponse20014.
        Length of the match

        :return: The duration of this InlineResponse20014.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this InlineResponse20014.
        Length of the match

        :param duration: The duration of this InlineResponse20014.
        :type: int
        """

        self._duration = duration

    @property
    def start_time(self):
        """
        Gets the start_time of this InlineResponse20014.
        Unix timestamp of when the match began

        :return: The start_time of this InlineResponse20014.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this InlineResponse20014.
        Unix timestamp of when the match began

        :param start_time: The start_time of this InlineResponse20014.
        :type: int
        """

        self._start_time = start_time

    @property
    def radiant_team_id(self):
        """
        Gets the radiant_team_id of this InlineResponse20014.
        The Radiant's team_id

        :return: The radiant_team_id of this InlineResponse20014.
        :rtype: int
        """
        return self._radiant_team_id

    @radiant_team_id.setter
    def radiant_team_id(self, radiant_team_id):
        """
        Sets the radiant_team_id of this InlineResponse20014.
        The Radiant's team_id

        :param radiant_team_id: The radiant_team_id of this InlineResponse20014.
        :type: int
        """

        self._radiant_team_id = radiant_team_id

    @property
    def radiant_name(self):
        """
        Gets the radiant_name of this InlineResponse20014.
        The Radiant's team name

        :return: The radiant_name of this InlineResponse20014.
        :rtype: str
        """
        return self._radiant_name

    @radiant_name.setter
    def radiant_name(self, radiant_name):
        """
        Sets the radiant_name of this InlineResponse20014.
        The Radiant's team name

        :param radiant_name: The radiant_name of this InlineResponse20014.
        :type: str
        """

        self._radiant_name = radiant_name

    @property
    def dire_team_id(self):
        """
        Gets the dire_team_id of this InlineResponse20014.
        The Dire's team_id

        :return: The dire_team_id of this InlineResponse20014.
        :rtype: int
        """
        return self._dire_team_id

    @dire_team_id.setter
    def dire_team_id(self, dire_team_id):
        """
        Sets the dire_team_id of this InlineResponse20014.
        The Dire's team_id

        :param dire_team_id: The dire_team_id of this InlineResponse20014.
        :type: int
        """

        self._dire_team_id = dire_team_id

    @property
    def dire_name(self):
        """
        Gets the dire_name of this InlineResponse20014.
        The Dire's team name

        :return: The dire_name of this InlineResponse20014.
        :rtype: str
        """
        return self._dire_name

    @dire_name.setter
    def dire_name(self, dire_name):
        """
        Sets the dire_name of this InlineResponse20014.
        The Dire's team name

        :param dire_name: The dire_name of this InlineResponse20014.
        :type: str
        """

        self._dire_name = dire_name

    @property
    def leagueid(self):
        """
        Gets the leagueid of this InlineResponse20014.
        Identifier for the league the match took place in

        :return: The leagueid of this InlineResponse20014.
        :rtype: int
        """
        return self._leagueid

    @leagueid.setter
    def leagueid(self, leagueid):
        """
        Sets the leagueid of this InlineResponse20014.
        Identifier for the league the match took place in

        :param leagueid: The leagueid of this InlineResponse20014.
        :type: int
        """

        self._leagueid = leagueid

    @property
    def league_name(self):
        """
        Gets the league_name of this InlineResponse20014.
        Name of league the match took place in

        :return: The league_name of this InlineResponse20014.
        :rtype: str
        """
        return self._league_name

    @league_name.setter
    def league_name(self, league_name):
        """
        Sets the league_name of this InlineResponse20014.
        Name of league the match took place in

        :param league_name: The league_name of this InlineResponse20014.
        :type: str
        """

        self._league_name = league_name

    @property
    def series_id(self):
        """
        Gets the series_id of this InlineResponse20014.
        Identifier for the series of the match

        :return: The series_id of this InlineResponse20014.
        :rtype: int
        """
        return self._series_id

    @series_id.setter
    def series_id(self, series_id):
        """
        Sets the series_id of this InlineResponse20014.
        Identifier for the series of the match

        :param series_id: The series_id of this InlineResponse20014.
        :type: int
        """

        self._series_id = series_id

    @property
    def series_type(self):
        """
        Gets the series_type of this InlineResponse20014.
        Type of series the match was

        :return: The series_type of this InlineResponse20014.
        :rtype: int
        """
        return self._series_type

    @series_type.setter
    def series_type(self, series_type):
        """
        Sets the series_type of this InlineResponse20014.
        Type of series the match was

        :param series_type: The series_type of this InlineResponse20014.
        :type: int
        """

        self._series_type = series_type

    @property
    def radiant_score(self):
        """
        Gets the radiant_score of this InlineResponse20014.
        Number of kills the Radiant team had when the match ended

        :return: The radiant_score of this InlineResponse20014.
        :rtype: int
        """
        return self._radiant_score

    @radiant_score.setter
    def radiant_score(self, radiant_score):
        """
        Sets the radiant_score of this InlineResponse20014.
        Number of kills the Radiant team had when the match ended

        :param radiant_score: The radiant_score of this InlineResponse20014.
        :type: int
        """

        self._radiant_score = radiant_score

    @property
    def dire_score(self):
        """
        Gets the dire_score of this InlineResponse20014.
        Number of kills the Dire team had when the match ended

        :return: The dire_score of this InlineResponse20014.
        :rtype: int
        """
        return self._dire_score

    @dire_score.setter
    def dire_score(self, dire_score):
        """
        Sets the dire_score of this InlineResponse20014.
        Number of kills the Dire team had when the match ended

        :param dire_score: The dire_score of this InlineResponse20014.
        :type: int
        """

        self._dire_score = dire_score

    @property
    def radiant_win(self):
        """
        Gets the radiant_win of this InlineResponse20014.
        Whether or not the Radiant won the match

        :return: The radiant_win of this InlineResponse20014.
        :rtype: bool
        """
        return self._radiant_win

    @radiant_win.setter
    def radiant_win(self, radiant_win):
        """
        Sets the radiant_win of this InlineResponse20014.
        Whether or not the Radiant won the match

        :param radiant_win: The radiant_win of this InlineResponse20014.
        :type: bool
        """

        self._radiant_win = radiant_win

    @property
    def radiant(self):
        """
        Gets the radiant of this InlineResponse20014.
        Whether the team/player/hero was on Radiant

        :return: The radiant of this InlineResponse20014.
        :rtype: bool
        """
        return self._radiant

    @radiant.setter
    def radiant(self, radiant):
        """
        Sets the radiant of this InlineResponse20014.
        Whether the team/player/hero was on Radiant

        :param radiant: The radiant of this InlineResponse20014.
        :type: bool
        """

        self._radiant = radiant

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
        if not isinstance(other, InlineResponse20014):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
