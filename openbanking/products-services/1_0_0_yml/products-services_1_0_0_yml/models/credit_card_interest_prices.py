# coding: utf-8

"""
    API's OpenData do Open Banking Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreditCardInterestPrices(object):
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
        'interval': 'Intervals',
        'rate': 'str'
    }

    attribute_map = {
        'interval': 'interval',
        'rate': 'rate'
    }

    def __init__(self, interval=None, rate=None):  # noqa: E501
        """CreditCardInterestPrices - a model defined in Swagger"""  # noqa: E501
        self._interval = None
        self._rate = None
        self.discriminator = None
        self.interval = interval
        self.rate = rate

    @property
    def interval(self):
        """Gets the interval of this CreditCardInterestPrices.  # noqa: E501


        :return: The interval of this CreditCardInterestPrices.  # noqa: E501
        :rtype: Intervals
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this CreditCardInterestPrices.


        :param interval: The interval of this CreditCardInterestPrices.  # noqa: E501
        :type: Intervals
        """
        if interval is None:
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501

        self._interval = interval

    @property
    def rate(self):
        """Gets the rate of this CreditCardInterestPrices.  # noqa: E501

        Percentual que corresponde a mediana (taxa efetiva) aplicada para  outras operações de crédito, no período informado.  # noqa: E501

        :return: The rate of this CreditCardInterestPrices.  # noqa: E501
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this CreditCardInterestPrices.

        Percentual que corresponde a mediana (taxa efetiva) aplicada para  outras operações de crédito, no período informado.  # noqa: E501

        :param rate: The rate of this CreditCardInterestPrices.  # noqa: E501
        :type: str
        """
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")  # noqa: E501

        self._rate = rate

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
        if issubclass(CreditCardInterestPrices, dict):
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
        if not isinstance(other, CreditCardInterestPrices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other