# coding: utf-8

"""
    API Investments - Open Finance Brasil

    Estas APIs visam o compartilhamento de dados sobre Investimentos e suas características entre as Instituições Financeiras participantes do Open Finance Brasil   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InvestmentsNoIdentificationFrequencyDistribution(object):
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
        'prices': 'list[DistributionFrequencyPrice]',
        'minimum': 'str',
        'maximum': 'str'
    }

    attribute_map = {
        'prices': 'prices',
        'minimum': 'minimum',
        'maximum': 'maximum'
    }

    def __init__(self, prices=None, minimum=None, maximum=None):  # noqa: E501
        """InvestmentsNoIdentificationFrequencyDistribution - a model defined in Swagger"""  # noqa: E501
        self._prices = None
        self._minimum = None
        self._maximum = None
        self.discriminator = None
        self.prices = prices
        self.minimum = minimum
        self.maximum = maximum

    @property
    def prices(self):
        """Gets the prices of this InvestmentsNoIdentificationFrequencyDistribution.  # noqa: E501

        Distribuição dos preços.  # noqa: E501

        :return: The prices of this InvestmentsNoIdentificationFrequencyDistribution.  # noqa: E501
        :rtype: list[DistributionFrequencyPrice]
        """
        return self._prices

    @prices.setter
    def prices(self, prices):
        """Sets the prices of this InvestmentsNoIdentificationFrequencyDistribution.

        Distribuição dos preços.  # noqa: E501

        :param prices: The prices of this InvestmentsNoIdentificationFrequencyDistribution.  # noqa: E501
        :type: list[DistributionFrequencyPrice]
        """
        if prices is None:
            raise ValueError("Invalid value for `prices`, must not be `None`")  # noqa: E501

        self._prices = prices

    @property
    def minimum(self):
        """Gets the minimum of this InvestmentsNoIdentificationFrequencyDistribution.  # noqa: E501

        Valor mínimo.  # noqa: E501

        :return: The minimum of this InvestmentsNoIdentificationFrequencyDistribution.  # noqa: E501
        :rtype: str
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this InvestmentsNoIdentificationFrequencyDistribution.

        Valor mínimo.  # noqa: E501

        :param minimum: The minimum of this InvestmentsNoIdentificationFrequencyDistribution.  # noqa: E501
        :type: str
        """
        if minimum is None:
            raise ValueError("Invalid value for `minimum`, must not be `None`")  # noqa: E501

        self._minimum = minimum

    @property
    def maximum(self):
        """Gets the maximum of this InvestmentsNoIdentificationFrequencyDistribution.  # noqa: E501

        Valor máximo.  # noqa: E501

        :return: The maximum of this InvestmentsNoIdentificationFrequencyDistribution.  # noqa: E501
        :rtype: str
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this InvestmentsNoIdentificationFrequencyDistribution.

        Valor máximo.  # noqa: E501

        :param maximum: The maximum of this InvestmentsNoIdentificationFrequencyDistribution.  # noqa: E501
        :type: str
        """
        if maximum is None:
            raise ValueError("Invalid value for `maximum`, must not be `None`")  # noqa: E501

        self._maximum = maximum

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
        if issubclass(InvestmentsNoIdentificationFrequencyDistribution, dict):
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
        if not isinstance(other, InvestmentsNoIdentificationFrequencyDistribution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
