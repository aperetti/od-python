# coding: utf-8

"""
    OpenDota API

    # Introduction This API provides Dota 2 related data. Please keep request rate to approximately 3/s. 

    OpenAPI spec version: 15.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse20021(object):
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
        'hero_id': 'float',
        'result': 'InlineResponse20021Result'
    }

    attribute_map = {
        'hero_id': 'hero_id',
        'result': 'result'
    }

    def __init__(self, hero_id=None, result=None):
        """
        InlineResponse20021 - a model defined in Swagger
        """

        self._hero_id = None
        self._result = None

        if hero_id is not None:
          self.hero_id = hero_id
        if result is not None:
          self.result = result

    @property
    def hero_id(self):
        """
        Gets the hero_id of this InlineResponse20021.
        hero_id

        :return: The hero_id of this InlineResponse20021.
        :rtype: float
        """
        return self._hero_id

    @hero_id.setter
    def hero_id(self, hero_id):
        """
        Sets the hero_id of this InlineResponse20021.
        hero_id

        :param hero_id: The hero_id of this InlineResponse20021.
        :type: float
        """

        self._hero_id = hero_id

    @property
    def result(self):
        """
        Gets the result of this InlineResponse20021.

        :return: The result of this InlineResponse20021.
        :rtype: InlineResponse20021Result
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this InlineResponse20021.

        :param result: The result of this InlineResponse20021.
        :type: InlineResponse20021Result
        """

        self._result = result

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
        if not isinstance(other, InlineResponse20021):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
