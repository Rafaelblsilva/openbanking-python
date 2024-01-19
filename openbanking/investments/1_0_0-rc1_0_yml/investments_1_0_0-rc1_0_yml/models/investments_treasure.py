# coding: utf-8

"""
    API Investments - Open Finance Brasil

    Estas APIs visam o compartilhamento de dados sobre Investimentos e suas características entre as Instituições Financeiras participantes do Open Finance Brasil   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InvestmentsTreasure(object):
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
        'participant': 'Participant',
        'investment_type': 'EnumInvestmentsTreasureInvestmentType',
        'custody_fee': 'NoIdentificationFrequencyDistribution',
        'loading_rate': 'NoIdentificationFrequencyDistribution'
    }

    attribute_map = {
        'participant': 'participant',
        'investment_type': 'investmentType',
        'custody_fee': 'custodyFee',
        'loading_rate': 'loadingRate'
    }

    def __init__(self, participant=None, investment_type=None, custody_fee=None, loading_rate=None):  # noqa: E501
        """InvestmentsTreasure - a model defined in Swagger"""  # noqa: E501
        self._participant = None
        self._investment_type = None
        self._custody_fee = None
        self._loading_rate = None
        self.discriminator = None
        self.participant = participant
        self.investment_type = investment_type
        self.custody_fee = custody_fee
        self.loading_rate = loading_rate

    @property
    def participant(self):
        """Gets the participant of this InvestmentsTreasure.  # noqa: E501


        :return: The participant of this InvestmentsTreasure.  # noqa: E501
        :rtype: Participant
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this InvestmentsTreasure.


        :param participant: The participant of this InvestmentsTreasure.  # noqa: E501
        :type: Participant
        """
        if participant is None:
            raise ValueError("Invalid value for `participant`, must not be `None`")  # noqa: E501

        self._participant = participant

    @property
    def investment_type(self):
        """Gets the investment_type of this InvestmentsTreasure.  # noqa: E501


        :return: The investment_type of this InvestmentsTreasure.  # noqa: E501
        :rtype: EnumInvestmentsTreasureInvestmentType
        """
        return self._investment_type

    @investment_type.setter
    def investment_type(self, investment_type):
        """Sets the investment_type of this InvestmentsTreasure.


        :param investment_type: The investment_type of this InvestmentsTreasure.  # noqa: E501
        :type: EnumInvestmentsTreasureInvestmentType
        """
        if investment_type is None:
            raise ValueError("Invalid value for `investment_type`, must not be `None`")  # noqa: E501

        self._investment_type = investment_type

    @property
    def custody_fee(self):
        """Gets the custody_fee of this InvestmentsTreasure.  # noqa: E501


        :return: The custody_fee of this InvestmentsTreasure.  # noqa: E501
        :rtype: NoIdentificationFrequencyDistribution
        """
        return self._custody_fee

    @custody_fee.setter
    def custody_fee(self, custody_fee):
        """Sets the custody_fee of this InvestmentsTreasure.


        :param custody_fee: The custody_fee of this InvestmentsTreasure.  # noqa: E501
        :type: NoIdentificationFrequencyDistribution
        """
        if custody_fee is None:
            raise ValueError("Invalid value for `custody_fee`, must not be `None`")  # noqa: E501

        self._custody_fee = custody_fee

    @property
    def loading_rate(self):
        """Gets the loading_rate of this InvestmentsTreasure.  # noqa: E501


        :return: The loading_rate of this InvestmentsTreasure.  # noqa: E501
        :rtype: NoIdentificationFrequencyDistribution
        """
        return self._loading_rate

    @loading_rate.setter
    def loading_rate(self, loading_rate):
        """Sets the loading_rate of this InvestmentsTreasure.


        :param loading_rate: The loading_rate of this InvestmentsTreasure.  # noqa: E501
        :type: NoIdentificationFrequencyDistribution
        """
        if loading_rate is None:
            raise ValueError("Invalid value for `loading_rate`, must not be `None`")  # noqa: E501

        self._loading_rate = loading_rate

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
        if issubclass(InvestmentsTreasure, dict):
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
        if not isinstance(other, InvestmentsTreasure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
