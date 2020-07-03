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


class InlineResponse2002(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, localized_name=None, img=None, icon=None, pro_win=None, pro_pick=None, hero_id=None, pro_ban=None, _1_pick=None, _1_win=None, _2_pick=None, _2_win=None, _3_pick=None, _3_win=None, _4_pick=None, _4_win=None, _5_pick=None, _5_win=None, _6_pick=None, _6_win=None, _7_pick=None, _7_win=None):
        """
        InlineResponse2002 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'localized_name': 'str',
            'img': 'str',
            'icon': 'str',
            'pro_win': 'int',
            'pro_pick': 'int',
            'hero_id': 'int',
            'pro_ban': 'int',
            '_1_pick': 'int',
            '_1_win': 'int',
            '_2_pick': 'int',
            '_2_win': 'int',
            '_3_pick': 'int',
            '_3_win': 'int',
            '_4_pick': 'int',
            '_4_win': 'int',
            '_5_pick': 'int',
            '_5_win': 'int',
            '_6_pick': 'int',
            '_6_win': 'int',
            '_7_pick': 'int',
            '_7_win': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'localized_name': 'localized_name',
            'img': 'img',
            'icon': 'icon',
            'pro_win': 'pro_win',
            'pro_pick': 'pro_pick',
            'hero_id': 'hero_id',
            'pro_ban': 'pro_ban',
            '_1_pick': '1_pick',
            '_1_win': '1_win',
            '_2_pick': '2_pick',
            '_2_win': '2_win',
            '_3_pick': '3_pick',
            '_3_win': '3_win',
            '_4_pick': '4_pick',
            '_4_win': '4_win',
            '_5_pick': '5_pick',
            '_5_win': '5_win',
            '_6_pick': '6_pick',
            '_6_win': '6_win',
            '_7_pick': '7_pick',
            '_7_win': '7_win'
        }

        self._id = id
        self._name = name
        self._localized_name = localized_name
        self._img = img
        self._icon = icon
        self._pro_win = pro_win
        self._pro_pick = pro_pick
        self._hero_id = hero_id
        self._pro_ban = pro_ban
        self.__1_pick = _1_pick
        self.__1_win = _1_win
        self.__2_pick = _2_pick
        self.__2_win = _2_win
        self.__3_pick = _3_pick
        self.__3_win = _3_win
        self.__4_pick = _4_pick
        self.__4_win = _4_win
        self.__5_pick = _5_pick
        self.__5_win = _5_win
        self.__6_pick = _6_pick
        self.__6_win = _6_win
        self.__7_pick = _7_pick
        self.__7_win = _7_win

    @property
    def id(self):
        """
        Gets the id of this InlineResponse2002.
        id

        :return: The id of this InlineResponse2002.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InlineResponse2002.
        id

        :param id: The id of this InlineResponse2002.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this InlineResponse2002.
        name

        :return: The name of this InlineResponse2002.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InlineResponse2002.
        name

        :param name: The name of this InlineResponse2002.
        :type: str
        """

        self._name = name

    @property
    def localized_name(self):
        """
        Gets the localized_name of this InlineResponse2002.
        localized_name

        :return: The localized_name of this InlineResponse2002.
        :rtype: str
        """
        return self._localized_name

    @localized_name.setter
    def localized_name(self, localized_name):
        """
        Sets the localized_name of this InlineResponse2002.
        localized_name

        :param localized_name: The localized_name of this InlineResponse2002.
        :type: str
        """

        self._localized_name = localized_name

    @property
    def img(self):
        """
        Gets the img of this InlineResponse2002.
        img

        :return: The img of this InlineResponse2002.
        :rtype: str
        """
        return self._img

    @img.setter
    def img(self, img):
        """
        Sets the img of this InlineResponse2002.
        img

        :param img: The img of this InlineResponse2002.
        :type: str
        """

        self._img = img

    @property
    def icon(self):
        """
        Gets the icon of this InlineResponse2002.
        icon

        :return: The icon of this InlineResponse2002.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """
        Sets the icon of this InlineResponse2002.
        icon

        :param icon: The icon of this InlineResponse2002.
        :type: str
        """

        self._icon = icon

    @property
    def pro_win(self):
        """
        Gets the pro_win of this InlineResponse2002.
        pro_win

        :return: The pro_win of this InlineResponse2002.
        :rtype: int
        """
        return self._pro_win

    @pro_win.setter
    def pro_win(self, pro_win):
        """
        Sets the pro_win of this InlineResponse2002.
        pro_win

        :param pro_win: The pro_win of this InlineResponse2002.
        :type: int
        """

        self._pro_win = pro_win

    @property
    def pro_pick(self):
        """
        Gets the pro_pick of this InlineResponse2002.
        pro_pick

        :return: The pro_pick of this InlineResponse2002.
        :rtype: int
        """
        return self._pro_pick

    @pro_pick.setter
    def pro_pick(self, pro_pick):
        """
        Sets the pro_pick of this InlineResponse2002.
        pro_pick

        :param pro_pick: The pro_pick of this InlineResponse2002.
        :type: int
        """

        self._pro_pick = pro_pick

    @property
    def hero_id(self):
        """
        Gets the hero_id of this InlineResponse2002.
        The ID value of the hero played

        :return: The hero_id of this InlineResponse2002.
        :rtype: int
        """
        return self._hero_id

    @hero_id.setter
    def hero_id(self, hero_id):
        """
        Sets the hero_id of this InlineResponse2002.
        The ID value of the hero played

        :param hero_id: The hero_id of this InlineResponse2002.
        :type: int
        """

        self._hero_id = hero_id

    @property
    def pro_ban(self):
        """
        Gets the pro_ban of this InlineResponse2002.
        pro_ban

        :return: The pro_ban of this InlineResponse2002.
        :rtype: int
        """
        return self._pro_ban

    @pro_ban.setter
    def pro_ban(self, pro_ban):
        """
        Sets the pro_ban of this InlineResponse2002.
        pro_ban

        :param pro_ban: The pro_ban of this InlineResponse2002.
        :type: int
        """

        self._pro_ban = pro_ban

    @property
    def _1_pick(self):
        """
        Gets the _1_pick of this InlineResponse2002.
        Herald picks

        :return: The _1_pick of this InlineResponse2002.
        :rtype: int
        """
        return self.__1_pick

    @_1_pick.setter
    def _1_pick(self, _1_pick):
        """
        Sets the _1_pick of this InlineResponse2002.
        Herald picks

        :param _1_pick: The _1_pick of this InlineResponse2002.
        :type: int
        """

        self.__1_pick = _1_pick

    @property
    def _1_win(self):
        """
        Gets the _1_win of this InlineResponse2002.
        Herald wins

        :return: The _1_win of this InlineResponse2002.
        :rtype: int
        """
        return self.__1_win

    @_1_win.setter
    def _1_win(self, _1_win):
        """
        Sets the _1_win of this InlineResponse2002.
        Herald wins

        :param _1_win: The _1_win of this InlineResponse2002.
        :type: int
        """

        self.__1_win = _1_win

    @property
    def _2_pick(self):
        """
        Gets the _2_pick of this InlineResponse2002.
        Guardian picks

        :return: The _2_pick of this InlineResponse2002.
        :rtype: int
        """
        return self.__2_pick

    @_2_pick.setter
    def _2_pick(self, _2_pick):
        """
        Sets the _2_pick of this InlineResponse2002.
        Guardian picks

        :param _2_pick: The _2_pick of this InlineResponse2002.
        :type: int
        """

        self.__2_pick = _2_pick

    @property
    def _2_win(self):
        """
        Gets the _2_win of this InlineResponse2002.
        Guardian wins

        :return: The _2_win of this InlineResponse2002.
        :rtype: int
        """
        return self.__2_win

    @_2_win.setter
    def _2_win(self, _2_win):
        """
        Sets the _2_win of this InlineResponse2002.
        Guardian wins

        :param _2_win: The _2_win of this InlineResponse2002.
        :type: int
        """

        self.__2_win = _2_win

    @property
    def _3_pick(self):
        """
        Gets the _3_pick of this InlineResponse2002.
        Crusader picks

        :return: The _3_pick of this InlineResponse2002.
        :rtype: int
        """
        return self.__3_pick

    @_3_pick.setter
    def _3_pick(self, _3_pick):
        """
        Sets the _3_pick of this InlineResponse2002.
        Crusader picks

        :param _3_pick: The _3_pick of this InlineResponse2002.
        :type: int
        """

        self.__3_pick = _3_pick

    @property
    def _3_win(self):
        """
        Gets the _3_win of this InlineResponse2002.
        Crusader wins

        :return: The _3_win of this InlineResponse2002.
        :rtype: int
        """
        return self.__3_win

    @_3_win.setter
    def _3_win(self, _3_win):
        """
        Sets the _3_win of this InlineResponse2002.
        Crusader wins

        :param _3_win: The _3_win of this InlineResponse2002.
        :type: int
        """

        self.__3_win = _3_win

    @property
    def _4_pick(self):
        """
        Gets the _4_pick of this InlineResponse2002.
        Archon picks

        :return: The _4_pick of this InlineResponse2002.
        :rtype: int
        """
        return self.__4_pick

    @_4_pick.setter
    def _4_pick(self, _4_pick):
        """
        Sets the _4_pick of this InlineResponse2002.
        Archon picks

        :param _4_pick: The _4_pick of this InlineResponse2002.
        :type: int
        """

        self.__4_pick = _4_pick

    @property
    def _4_win(self):
        """
        Gets the _4_win of this InlineResponse2002.
        Archon wins

        :return: The _4_win of this InlineResponse2002.
        :rtype: int
        """
        return self.__4_win

    @_4_win.setter
    def _4_win(self, _4_win):
        """
        Sets the _4_win of this InlineResponse2002.
        Archon wins

        :param _4_win: The _4_win of this InlineResponse2002.
        :type: int
        """

        self.__4_win = _4_win

    @property
    def _5_pick(self):
        """
        Gets the _5_pick of this InlineResponse2002.
        Legend picks

        :return: The _5_pick of this InlineResponse2002.
        :rtype: int
        """
        return self.__5_pick

    @_5_pick.setter
    def _5_pick(self, _5_pick):
        """
        Sets the _5_pick of this InlineResponse2002.
        Legend picks

        :param _5_pick: The _5_pick of this InlineResponse2002.
        :type: int
        """

        self.__5_pick = _5_pick

    @property
    def _5_win(self):
        """
        Gets the _5_win of this InlineResponse2002.
        Legend wins

        :return: The _5_win of this InlineResponse2002.
        :rtype: int
        """
        return self.__5_win

    @_5_win.setter
    def _5_win(self, _5_win):
        """
        Sets the _5_win of this InlineResponse2002.
        Legend wins

        :param _5_win: The _5_win of this InlineResponse2002.
        :type: int
        """

        self.__5_win = _5_win

    @property
    def _6_pick(self):
        """
        Gets the _6_pick of this InlineResponse2002.
        Ancient picks

        :return: The _6_pick of this InlineResponse2002.
        :rtype: int
        """
        return self.__6_pick

    @_6_pick.setter
    def _6_pick(self, _6_pick):
        """
        Sets the _6_pick of this InlineResponse2002.
        Ancient picks

        :param _6_pick: The _6_pick of this InlineResponse2002.
        :type: int
        """

        self.__6_pick = _6_pick

    @property
    def _6_win(self):
        """
        Gets the _6_win of this InlineResponse2002.
        Ancient wins

        :return: The _6_win of this InlineResponse2002.
        :rtype: int
        """
        return self.__6_win

    @_6_win.setter
    def _6_win(self, _6_win):
        """
        Sets the _6_win of this InlineResponse2002.
        Ancient wins

        :param _6_win: The _6_win of this InlineResponse2002.
        :type: int
        """

        self.__6_win = _6_win

    @property
    def _7_pick(self):
        """
        Gets the _7_pick of this InlineResponse2002.
        Divine picks

        :return: The _7_pick of this InlineResponse2002.
        :rtype: int
        """
        return self.__7_pick

    @_7_pick.setter
    def _7_pick(self, _7_pick):
        """
        Sets the _7_pick of this InlineResponse2002.
        Divine picks

        :param _7_pick: The _7_pick of this InlineResponse2002.
        :type: int
        """

        self.__7_pick = _7_pick

    @property
    def _7_win(self):
        """
        Gets the _7_win of this InlineResponse2002.
        Divine wins

        :return: The _7_win of this InlineResponse2002.
        :rtype: int
        """
        return self.__7_win

    @_7_win.setter
    def _7_win(self, _7_win):
        """
        Sets the _7_win of this InlineResponse2002.
        Divine wins

        :param _7_win: The _7_win of this InlineResponse2002.
        :type: int
        """

        self.__7_win = _7_win

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
