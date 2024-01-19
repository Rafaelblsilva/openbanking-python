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

class PersonalAccountsIncomeRatesPrepaidPaymentAccount(object):
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
        'applications': 'list[object]',
        'mininum_rate': 'str',
        'maximum_rate': 'str'
    }

    attribute_map = {
        'applications': 'applications',
        'mininum_rate': 'mininumRate',
        'maximum_rate': 'maximumRate'
    }

    def __init__(self, applications=None, mininum_rate=None, maximum_rate=None):  # noqa: E501
        """PersonalAccountsIncomeRatesPrepaidPaymentAccount - a model defined in Swagger"""  # noqa: E501
        self._applications = None
        self._mininum_rate = None
        self._maximum_rate = None
        self.discriminator = None
        self.applications = applications
        if mininum_rate is not None:
            self.mininum_rate = mininum_rate
        self.maximum_rate = maximum_rate

    @property
    def applications(self):
        """Gets the applications of this PersonalAccountsIncomeRatesPrepaidPaymentAccount.  # noqa: E501


        :return: The applications of this PersonalAccountsIncomeRatesPrepaidPaymentAccount.  # noqa: E501
        :rtype: list[object]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this PersonalAccountsIncomeRatesPrepaidPaymentAccount.


        :param applications: The applications of this PersonalAccountsIncomeRatesPrepaidPaymentAccount.  # noqa: E501
        :type: list[object]
        """
        if applications is None:
            raise ValueError("Invalid value for `applications`, must not be `None`")  # noqa: E501

        self._applications = applications

    @property
    def mininum_rate(self):
        """Gets the mininum_rate of this PersonalAccountsIncomeRatesPrepaidPaymentAccount.  # noqa: E501

        Percentual mínimo referente à taxa de remuneração efetivamente aplicada no mês de referência para CONTA_PAGAMENTO_PRE_PAGA. A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, emso que venham preenchidas com zeros  # noqa: E501

        :return: The mininum_rate of this PersonalAccountsIncomeRatesPrepaidPaymentAccount.  # noqa: E501
        :rtype: str
        """
        return self._mininum_rate

    @mininum_rate.setter
    def mininum_rate(self, mininum_rate):
        """Sets the mininum_rate of this PersonalAccountsIncomeRatesPrepaidPaymentAccount.

        Percentual mínimo referente à taxa de remuneração efetivamente aplicada no mês de referência para CONTA_PAGAMENTO_PRE_PAGA. A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, emso que venham preenchidas com zeros  # noqa: E501

        :param mininum_rate: The mininum_rate of this PersonalAccountsIncomeRatesPrepaidPaymentAccount.  # noqa: E501
        :type: str
        """

        self._mininum_rate = mininum_rate

    @property
    def maximum_rate(self):
        """Gets the maximum_rate of this PersonalAccountsIncomeRatesPrepaidPaymentAccount.  # noqa: E501

        Percentual máximo referente à taxa de remuneração efetivamente aplicada no mês de referência para VCONTA_PAGAMENTO_PRE_PAGA. A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, emso que venham preenchidas com zeros  # noqa: E501

        :return: The maximum_rate of this PersonalAccountsIncomeRatesPrepaidPaymentAccount.  # noqa: E501
        :rtype: str
        """
        return self._maximum_rate

    @maximum_rate.setter
    def maximum_rate(self, maximum_rate):
        """Sets the maximum_rate of this PersonalAccountsIncomeRatesPrepaidPaymentAccount.

        Percentual máximo referente à taxa de remuneração efetivamente aplicada no mês de referência para VCONTA_PAGAMENTO_PRE_PAGA. A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, emso que venham preenchidas com zeros  # noqa: E501

        :param maximum_rate: The maximum_rate of this PersonalAccountsIncomeRatesPrepaidPaymentAccount.  # noqa: E501
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
        if issubclass(PersonalAccountsIncomeRatesPrepaidPaymentAccount, dict):
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
        if not isinstance(other, PersonalAccountsIncomeRatesPrepaidPaymentAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
