# coding: utf-8

"""
    API's OpenData do Open Banking Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreditCardInterest(object):
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
        'fee_rate': 'InterestRate',
        'instalment_rate': 'InterestRate',
        'interest_rates': 'list[CreditCardInterestRate]'
    }

    attribute_map = {
        'fee_rate': 'feeRate',
        'instalment_rate': 'instalmentRate',
        'interest_rates': 'interestRates'
    }

    def __init__(self, fee_rate=None, instalment_rate=None, interest_rates=None):  # noqa: E501
        """CreditCardInterest - a model defined in Swagger"""  # noqa: E501
        self._fee_rate = None
        self._instalment_rate = None
        self._interest_rates = None
        self.discriminator = None
        self.fee_rate = fee_rate
        self.instalment_rate = instalment_rate
        self.interest_rates = interest_rates

    @property
    def fee_rate(self):
        """Gets the fee_rate of this CreditCardInterest.  # noqa: E501


        :return: The fee_rate of this CreditCardInterest.  # noqa: E501
        :rtype: InterestRate
        """
        return self._fee_rate

    @fee_rate.setter
    def fee_rate(self, fee_rate):
        """Sets the fee_rate of this CreditCardInterest.


        :param fee_rate: The fee_rate of this CreditCardInterest.  # noqa: E501
        :type: InterestRate
        """
        if fee_rate is None:
            raise ValueError("Invalid value for `fee_rate`, must not be `None`")  # noqa: E501

        self._fee_rate = fee_rate

    @property
    def instalment_rate(self):
        """Gets the instalment_rate of this CreditCardInterest.  # noqa: E501


        :return: The instalment_rate of this CreditCardInterest.  # noqa: E501
        :rtype: InterestRate
        """
        return self._instalment_rate

    @instalment_rate.setter
    def instalment_rate(self, instalment_rate):
        """Sets the instalment_rate of this CreditCardInterest.


        :param instalment_rate: The instalment_rate of this CreditCardInterest.  # noqa: E501
        :type: InterestRate
        """
        if instalment_rate is None:
            raise ValueError("Invalid value for `instalment_rate`, must not be `None`")  # noqa: E501

        self._instalment_rate = instalment_rate

    @property
    def interest_rates(self):
        """Gets the interest_rates of this CreditCardInterest.  # noqa: E501

        Lista de outras operações de crédito  # noqa: E501

        :return: The interest_rates of this CreditCardInterest.  # noqa: E501
        :rtype: list[CreditCardInterestRate]
        """
        return self._interest_rates

    @interest_rates.setter
    def interest_rates(self, interest_rates):
        """Sets the interest_rates of this CreditCardInterest.

        Lista de outras operações de crédito  # noqa: E501

        :param interest_rates: The interest_rates of this CreditCardInterest.  # noqa: E501
        :type: list[CreditCardInterestRate]
        """
        if interest_rates is None:
            raise ValueError("Invalid value for `interest_rates`, must not be `None`")  # noqa: E501

        self._interest_rates = interest_rates

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
        if issubclass(CreditCardInterest, dict):
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
        if not isinstance(other, CreditCardInterest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
