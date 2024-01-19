# coding: utf-8

"""
    API's OpenData do Open Finance Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from products-services_3_0_0_yml.models.interest_rate_fee import InterestRateFee  # noqa: F401,E501

class FinancingInterestRate(InterestRateFee):
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
        'applications': 'list[ApplicationRate]',
        'minimum_rate': 'str',
        'maximum_rate': 'str'
    }
    if hasattr(InterestRateFee, "swagger_types"):
        swagger_types.update(InterestRateFee.swagger_types)

    attribute_map = {
        'applications': 'applications',
        'minimum_rate': 'minimumRate',
        'maximum_rate': 'maximumRate'
    }
    if hasattr(InterestRateFee, "attribute_map"):
        attribute_map.update(InterestRateFee.attribute_map)

    def __init__(self, applications=None, minimum_rate=None, maximum_rate=None, *args, **kwargs):  # noqa: E501
        """FinancingInterestRate - a model defined in Swagger"""  # noqa: E501
        self._applications = None
        self._minimum_rate = None
        self._maximum_rate = None
        self.discriminator = None
        self.applications = applications
        self.minimum_rate = minimum_rate
        self.maximum_rate = maximum_rate
        InterestRateFee.__init__(self, *args, **kwargs)

    @property
    def applications(self):
        """Gets the applications of this FinancingInterestRate.  # noqa: E501


        :return: The applications of this FinancingInterestRate.  # noqa: E501
        :rtype: list[ApplicationRate]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this FinancingInterestRate.


        :param applications: The applications of this FinancingInterestRate.  # noqa: E501
        :type: list[ApplicationRate]
        """
        if applications is None:
            raise ValueError("Invalid value for `applications`, must not be `None`")  # noqa: E501

        self._applications = applications

    @property
    def minimum_rate(self):
        """Gets the minimum_rate of this FinancingInterestRate.  # noqa: E501

        Percentual mínimo cobrado (taxa efetiva) no mês de referência, para o Financiamento contratado  A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)  # noqa: E501

        :return: The minimum_rate of this FinancingInterestRate.  # noqa: E501
        :rtype: str
        """
        return self._minimum_rate

    @minimum_rate.setter
    def minimum_rate(self, minimum_rate):
        """Sets the minimum_rate of this FinancingInterestRate.

        Percentual mínimo cobrado (taxa efetiva) no mês de referência, para o Financiamento contratado  A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)  # noqa: E501

        :param minimum_rate: The minimum_rate of this FinancingInterestRate.  # noqa: E501
        :type: str
        """
        if minimum_rate is None:
            raise ValueError("Invalid value for `minimum_rate`, must not be `None`")  # noqa: E501

        self._minimum_rate = minimum_rate

    @property
    def maximum_rate(self):
        """Gets the maximum_rate of this FinancingInterestRate.  # noqa: E501

        Percentual máximo cobrado (taxa efetiva) no mês de referência, para o Financiamento contratado  A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)  # noqa: E501

        :return: The maximum_rate of this FinancingInterestRate.  # noqa: E501
        :rtype: str
        """
        return self._maximum_rate

    @maximum_rate.setter
    def maximum_rate(self, maximum_rate):
        """Sets the maximum_rate of this FinancingInterestRate.

        Percentual máximo cobrado (taxa efetiva) no mês de referência, para o Financiamento contratado  A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)  # noqa: E501

        :param maximum_rate: The maximum_rate of this FinancingInterestRate.  # noqa: E501
        :type: str
        """
        if maximum_rate is None:
            raise ValueError("Invalid value for `maximum_rate`, must not be `None`")  # noqa: E501

        self._maximum_rate = maximum_rate

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
        if issubclass(FinancingInterestRate, dict):
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
        if not isinstance(other, FinancingInterestRate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
