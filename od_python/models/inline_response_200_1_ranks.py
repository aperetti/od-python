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


class InlineResponse2001Ranks(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, commmand=None, row_count=None, rows=None, fields=None, row_as_array=None, sum=None):
        """
        InlineResponse2001Ranks - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'commmand': 'str',
            'row_count': 'int',
            'rows': 'list[InlineResponse2001RanksRows]',
            'fields': 'list[InlineResponse2001RanksFields]',
            'row_as_array': 'bool',
            'sum': 'InlineResponse2001RanksSum'
        }

        self.attribute_map = {
            'commmand': 'commmand',
            'row_count': 'rowCount',
            'rows': 'rows',
            'fields': 'fields',
            'row_as_array': 'rowAsArray',
            'sum': 'sum'
        }

        self._commmand = commmand
        self._row_count = row_count
        self._rows = rows
        self._fields = fields
        self._row_as_array = row_as_array
        self._sum = sum

    @property
    def commmand(self):
        """
        Gets the commmand of this InlineResponse2001Ranks.
        command

        :return: The commmand of this InlineResponse2001Ranks.
        :rtype: str
        """
        return self._commmand

    @commmand.setter
    def commmand(self, commmand):
        """
        Sets the commmand of this InlineResponse2001Ranks.
        command

        :param commmand: The commmand of this InlineResponse2001Ranks.
        :type: str
        """

        self._commmand = commmand

    @property
    def row_count(self):
        """
        Gets the row_count of this InlineResponse2001Ranks.
        rowCount

        :return: The row_count of this InlineResponse2001Ranks.
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        """
        Sets the row_count of this InlineResponse2001Ranks.
        rowCount

        :param row_count: The row_count of this InlineResponse2001Ranks.
        :type: int
        """

        self._row_count = row_count

    @property
    def rows(self):
        """
        Gets the rows of this InlineResponse2001Ranks.
        rows

        :return: The rows of this InlineResponse2001Ranks.
        :rtype: list[InlineResponse2001RanksRows]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """
        Sets the rows of this InlineResponse2001Ranks.
        rows

        :param rows: The rows of this InlineResponse2001Ranks.
        :type: list[InlineResponse2001RanksRows]
        """

        self._rows = rows

    @property
    def fields(self):
        """
        Gets the fields of this InlineResponse2001Ranks.
        fields

        :return: The fields of this InlineResponse2001Ranks.
        :rtype: list[InlineResponse2001RanksFields]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this InlineResponse2001Ranks.
        fields

        :param fields: The fields of this InlineResponse2001Ranks.
        :type: list[InlineResponse2001RanksFields]
        """

        self._fields = fields

    @property
    def row_as_array(self):
        """
        Gets the row_as_array of this InlineResponse2001Ranks.
        rowAsArray

        :return: The row_as_array of this InlineResponse2001Ranks.
        :rtype: bool
        """
        return self._row_as_array

    @row_as_array.setter
    def row_as_array(self, row_as_array):
        """
        Sets the row_as_array of this InlineResponse2001Ranks.
        rowAsArray

        :param row_as_array: The row_as_array of this InlineResponse2001Ranks.
        :type: bool
        """

        self._row_as_array = row_as_array

    @property
    def sum(self):
        """
        Gets the sum of this InlineResponse2001Ranks.


        :return: The sum of this InlineResponse2001Ranks.
        :rtype: InlineResponse2001RanksSum
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """
        Sets the sum of this InlineResponse2001Ranks.


        :param sum: The sum of this InlineResponse2001Ranks.
        :type: InlineResponse2001RanksSum
        """

        self._sum = sum

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
