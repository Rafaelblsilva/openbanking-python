# coding: utf-8

"""
    APIs Admin do Open Banking Brasil

    As API's administrativas são recursos que podem ser consumidos apenas pelo diretório para avaliação e controle da qualidade dos serviços fornecidos pelas instituições financeiras  # noqa: E501

    OpenAPI spec version: 1.0.0-rc5.1
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InvocationMetricsUnattended(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'current_day': 'int',
        'previous_days': 'list[int]'
    }

    attribute_map = {
        'current_day': 'currentDay',
        'previous_days': 'previousDays'
    }

    def __init__(self, current_day=None, previous_days=None):  # noqa: E501
        """InvocationMetricsUnattended - a model defined in Swagger"""  # noqa: E501
        self._current_day = None
        self._previous_days = None
        self.discriminator = None
        self.current_day = current_day
        self.previous_days = previous_days

    @property
    def current_day(self):
        """Gets the current_day of this InvocationMetricsUnattended.  # noqa: E501

        Número de chamadas no dia atual para o nível não acompanhado.  # noqa: E501

        :return: The current_day of this InvocationMetricsUnattended.  # noqa: E501
        :rtype: int
        """
        return self._current_day

    @current_day.setter
    def current_day(self, current_day):
        """Sets the current_day of this InvocationMetricsUnattended.

        Número de chamadas no dia atual para o nível não acompanhado.  # noqa: E501

        :param current_day: The current_day of this InvocationMetricsUnattended.  # noqa: E501
        :type: int
        """
        if current_day is None:
            raise ValueError("Invalid value for `current_day`, must not be `None`")  # noqa: E501

        self._current_day = current_day

    @property
    def previous_days(self):
        """Gets the previous_days of this InvocationMetricsUnattended.  # noqa: E501

        Número de chamadas nos dias anteriores para o nível não acompanhado. O primeiro item do array é referente a ontem, e assim por diante. Devem ser retornados no máximo sete dias caso estejam disponíveis.  # noqa: E501

        :return: The previous_days of this InvocationMetricsUnattended.  # noqa: E501
        :rtype: list[int]
        """
        return self._previous_days

    @previous_days.setter
    def previous_days(self, previous_days):
        """Sets the previous_days of this InvocationMetricsUnattended.

        Número de chamadas nos dias anteriores para o nível não acompanhado. O primeiro item do array é referente a ontem, e assim por diante. Devem ser retornados no máximo sete dias caso estejam disponíveis.  # noqa: E501

        :param previous_days: The previous_days of this InvocationMetricsUnattended.  # noqa: E501
        :type: list[int]
        """
        if previous_days is None:
            raise ValueError("Invalid value for `previous_days`, must not be `None`")  # noqa: E501

        self._previous_days = previous_days

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InvocationMetricsUnattended, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InvocationMetricsUnattended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
