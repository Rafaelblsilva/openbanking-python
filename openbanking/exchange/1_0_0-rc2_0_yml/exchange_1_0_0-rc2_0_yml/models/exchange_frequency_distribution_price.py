# coding: utf-8

"""
    API Exchange - Open Finance Brasil

    API de Câmbio do Open Finance Brasil – Fase 4. API que retorna informações de Câmbio.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ExchangeFrequencyDistributionPrice(object):
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
        'interval': 'EnumInterval',
        'value': 'str',
        'operation_rate': 'str'
    }

    attribute_map = {
        'interval': 'interval',
        'value': 'value',
        'operation_rate': 'operationRate'
    }

    def __init__(self, interval=None, value=None, operation_rate=None):  # noqa: E501
        """ExchangeFrequencyDistributionPrice - a model defined in Swagger"""  # noqa: E501
        self._interval = None
        self._value = None
        self._operation_rate = None
        self.discriminator = None
        self.interval = interval
        self.value = value
        self.operation_rate = operation_rate

    @property
    def interval(self):
        """Gets the interval of this ExchangeFrequencyDistributionPrice.  # noqa: E501


        :return: The interval of this ExchangeFrequencyDistributionPrice.  # noqa: E501
        :rtype: EnumInterval
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ExchangeFrequencyDistributionPrice.


        :param interval: The interval of this ExchangeFrequencyDistributionPrice.  # noqa: E501
        :type: EnumInterval
        """
        if interval is None:
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501

        self._interval = interval

    @property
    def value(self):
        """Gets the value of this ExchangeFrequencyDistributionPrice.  # noqa: E501

        Mediana.  # noqa: E501

        :return: The value of this ExchangeFrequencyDistributionPrice.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ExchangeFrequencyDistributionPrice.

        Mediana.  # noqa: E501

        :param value: The value of this ExchangeFrequencyDistributionPrice.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def operation_rate(self):
        """Gets the operation_rate of this ExchangeFrequencyDistributionPrice.  # noqa: E501

        Percentual de Operação.  # noqa: E501

        :return: The operation_rate of this ExchangeFrequencyDistributionPrice.  # noqa: E501
        :rtype: str
        """
        return self._operation_rate

    @operation_rate.setter
    def operation_rate(self, operation_rate):
        """Sets the operation_rate of this ExchangeFrequencyDistributionPrice.

        Percentual de Operação.  # noqa: E501

        :param operation_rate: The operation_rate of this ExchangeFrequencyDistributionPrice.  # noqa: E501
        :type: str
        """
        if operation_rate is None:
            raise ValueError("Invalid value for `operation_rate`, must not be `None`")  # noqa: E501

        self._operation_rate = operation_rate

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
        if issubclass(ExchangeFrequencyDistributionPrice, dict):
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
        if not isinstance(other, ExchangeFrequencyDistributionPrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
