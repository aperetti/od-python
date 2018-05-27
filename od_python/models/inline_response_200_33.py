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


class InlineResponse20033(object):
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
        'table_name': 'str',
        'column_name': 'str',
        'data_type': 'str'
    }

    attribute_map = {
        'table_name': 'table_name',
        'column_name': 'column_name',
        'data_type': 'data_type'
    }

    def __init__(self, table_name=None, column_name=None, data_type=None):
        """
        InlineResponse20033 - a model defined in Swagger
        """

        self._table_name = None
        self._column_name = None
        self._data_type = None

        if table_name is not None:
          self.table_name = table_name
        if column_name is not None:
          self.column_name = column_name
        if data_type is not None:
          self.data_type = data_type

    @property
    def table_name(self):
        """
        Gets the table_name of this InlineResponse20033.
        table_name

        :return: The table_name of this InlineResponse20033.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """
        Sets the table_name of this InlineResponse20033.
        table_name

        :param table_name: The table_name of this InlineResponse20033.
        :type: str
        """

        self._table_name = table_name

    @property
    def column_name(self):
        """
        Gets the column_name of this InlineResponse20033.
        column_name

        :return: The column_name of this InlineResponse20033.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """
        Sets the column_name of this InlineResponse20033.
        column_name

        :param column_name: The column_name of this InlineResponse20033.
        :type: str
        """

        self._column_name = column_name

    @property
    def data_type(self):
        """
        Gets the data_type of this InlineResponse20033.
        data_type

        :return: The data_type of this InlineResponse20033.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this InlineResponse20033.
        data_type

        :param data_type: The data_type of this InlineResponse20033.
        :type: str
        """

        self._data_type = data_type

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
        if not isinstance(other, InlineResponse20033):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
