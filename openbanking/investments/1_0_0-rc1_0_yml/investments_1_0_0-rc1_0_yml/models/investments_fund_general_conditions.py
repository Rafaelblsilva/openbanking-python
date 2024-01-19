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

class InvestmentsFundGeneralConditions(object):
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
        'minimum_amount': 'InvestmentFundMinimumAmount',
        'redemption': 'InvestmentsFundGeneralConditionsRedemption',
        'application': 'InvestmentsFundGeneralConditionsApplication',
        'fund_quota_type': 'EnumInvestmentsFundGeneralConditionsFundQuotaType'
    }

    attribute_map = {
        'minimum_amount': 'minimumAmount',
        'redemption': 'redemption',
        'application': 'application',
        'fund_quota_type': 'fundQuotaType'
    }

    def __init__(self, minimum_amount=None, redemption=None, application=None, fund_quota_type=None):  # noqa: E501
        """InvestmentsFundGeneralConditions - a model defined in Swagger"""  # noqa: E501
        self._minimum_amount = None
        self._redemption = None
        self._application = None
        self._fund_quota_type = None
        self.discriminator = None
        self.minimum_amount = minimum_amount
        self.redemption = redemption
        self.application = application
        self.fund_quota_type = fund_quota_type

    @property
    def minimum_amount(self):
        """Gets the minimum_amount of this InvestmentsFundGeneralConditions.  # noqa: E501


        :return: The minimum_amount of this InvestmentsFundGeneralConditions.  # noqa: E501
        :rtype: InvestmentFundMinimumAmount
        """
        return self._minimum_amount

    @minimum_amount.setter
    def minimum_amount(self, minimum_amount):
        """Sets the minimum_amount of this InvestmentsFundGeneralConditions.


        :param minimum_amount: The minimum_amount of this InvestmentsFundGeneralConditions.  # noqa: E501
        :type: InvestmentFundMinimumAmount
        """
        if minimum_amount is None:
            raise ValueError("Invalid value for `minimum_amount`, must not be `None`")  # noqa: E501

        self._minimum_amount = minimum_amount

    @property
    def redemption(self):
        """Gets the redemption of this InvestmentsFundGeneralConditions.  # noqa: E501


        :return: The redemption of this InvestmentsFundGeneralConditions.  # noqa: E501
        :rtype: InvestmentsFundGeneralConditionsRedemption
        """
        return self._redemption

    @redemption.setter
    def redemption(self, redemption):
        """Sets the redemption of this InvestmentsFundGeneralConditions.


        :param redemption: The redemption of this InvestmentsFundGeneralConditions.  # noqa: E501
        :type: InvestmentsFundGeneralConditionsRedemption
        """
        if redemption is None:
            raise ValueError("Invalid value for `redemption`, must not be `None`")  # noqa: E501

        self._redemption = redemption

    @property
    def application(self):
        """Gets the application of this InvestmentsFundGeneralConditions.  # noqa: E501


        :return: The application of this InvestmentsFundGeneralConditions.  # noqa: E501
        :rtype: InvestmentsFundGeneralConditionsApplication
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this InvestmentsFundGeneralConditions.


        :param application: The application of this InvestmentsFundGeneralConditions.  # noqa: E501
        :type: InvestmentsFundGeneralConditionsApplication
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501

        self._application = application

    @property
    def fund_quota_type(self):
        """Gets the fund_quota_type of this InvestmentsFundGeneralConditions.  # noqa: E501


        :return: The fund_quota_type of this InvestmentsFundGeneralConditions.  # noqa: E501
        :rtype: EnumInvestmentsFundGeneralConditionsFundQuotaType
        """
        return self._fund_quota_type

    @fund_quota_type.setter
    def fund_quota_type(self, fund_quota_type):
        """Sets the fund_quota_type of this InvestmentsFundGeneralConditions.


        :param fund_quota_type: The fund_quota_type of this InvestmentsFundGeneralConditions.  # noqa: E501
        :type: EnumInvestmentsFundGeneralConditionsFundQuotaType
        """
        if fund_quota_type is None:
            raise ValueError("Invalid value for `fund_quota_type`, must not be `None`")  # noqa: E501

        self._fund_quota_type = fund_quota_type

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
        if issubclass(InvestmentsFundGeneralConditions, dict):
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
        if not isinstance(other, InvestmentsFundGeneralConditions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
