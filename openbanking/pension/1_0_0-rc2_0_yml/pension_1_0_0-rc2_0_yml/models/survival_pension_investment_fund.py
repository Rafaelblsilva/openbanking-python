# coding: utf-8

"""
    API Pension - Open Finance Brasil

    API de Previdência do Open Finance Brasil – Fase 4. API que retorna informações de Previdência.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SurvivalPensionInvestmentFund(object):
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
        'cnpj_number': 'CnpjNumber',
        'name': 'str',
        'maximum_administration_fee': 'str',
        'type_performance_fee': 'str',
        'maximum_performance_fee': 'str',
        'eligibility_rule': 'bool',
        'minimum_contribution_amount': 'str',
        'minimum_mathematical_provision_amount': 'str',
        'currency': 'CurrencyCode'
    }

    attribute_map = {
        'cnpj_number': 'cnpjNumber',
        'name': 'name',
        'maximum_administration_fee': 'maximumAdministrationFee',
        'type_performance_fee': 'typePerformanceFee',
        'maximum_performance_fee': 'maximumPerformanceFee',
        'eligibility_rule': 'eligibilityRule',
        'minimum_contribution_amount': 'minimumContributionAmount',
        'minimum_mathematical_provision_amount': 'minimumMathematicalProvisionAmount',
        'currency': 'currency'
    }

    def __init__(self, cnpj_number=None, name=None, maximum_administration_fee=None, type_performance_fee=None, maximum_performance_fee=None, eligibility_rule=None, minimum_contribution_amount=None, minimum_mathematical_provision_amount=None, currency=None):  # noqa: E501
        """SurvivalPensionInvestmentFund - a model defined in Swagger"""  # noqa: E501
        self._cnpj_number = None
        self._name = None
        self._maximum_administration_fee = None
        self._type_performance_fee = None
        self._maximum_performance_fee = None
        self._eligibility_rule = None
        self._minimum_contribution_amount = None
        self._minimum_mathematical_provision_amount = None
        self._currency = None
        self.discriminator = None
        self.cnpj_number = cnpj_number
        self.name = name
        self.maximum_administration_fee = maximum_administration_fee
        self.type_performance_fee = type_performance_fee
        if maximum_performance_fee is not None:
            self.maximum_performance_fee = maximum_performance_fee
        if eligibility_rule is not None:
            self.eligibility_rule = eligibility_rule
        if minimum_contribution_amount is not None:
            self.minimum_contribution_amount = minimum_contribution_amount
        if minimum_mathematical_provision_amount is not None:
            self.minimum_mathematical_provision_amount = minimum_mathematical_provision_amount
        if currency is not None:
            self.currency = currency

    @property
    def cnpj_number(self):
        """Gets the cnpj_number of this SurvivalPensionInvestmentFund.  # noqa: E501


        :return: The cnpj_number of this SurvivalPensionInvestmentFund.  # noqa: E501
        :rtype: CnpjNumber
        """
        return self._cnpj_number

    @cnpj_number.setter
    def cnpj_number(self, cnpj_number):
        """Sets the cnpj_number of this SurvivalPensionInvestmentFund.


        :param cnpj_number: The cnpj_number of this SurvivalPensionInvestmentFund.  # noqa: E501
        :type: CnpjNumber
        """
        if cnpj_number is None:
            raise ValueError("Invalid value for `cnpj_number`, must not be `None`")  # noqa: E501

        self._cnpj_number = cnpj_number

    @property
    def name(self):
        """Gets the name of this SurvivalPensionInvestmentFund.  # noqa: E501

        Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando: - Nome Fantasia   # noqa: E501

        :return: The name of this SurvivalPensionInvestmentFund.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SurvivalPensionInvestmentFund.

        Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando: - Nome Fantasia   # noqa: E501

        :param name: The name of this SurvivalPensionInvestmentFund.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def maximum_administration_fee(self):
        """Gets the maximum_administration_fee of this SurvivalPensionInvestmentFund.  # noqa: E501

        Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:   - Taxa Máxima de Administração - em %   # noqa: E501

        :return: The maximum_administration_fee of this SurvivalPensionInvestmentFund.  # noqa: E501
        :rtype: str
        """
        return self._maximum_administration_fee

    @maximum_administration_fee.setter
    def maximum_administration_fee(self, maximum_administration_fee):
        """Sets the maximum_administration_fee of this SurvivalPensionInvestmentFund.

        Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:   - Taxa Máxima de Administração - em %   # noqa: E501

        :param maximum_administration_fee: The maximum_administration_fee of this SurvivalPensionInvestmentFund.  # noqa: E501
        :type: str
        """
        if maximum_administration_fee is None:
            raise ValueError("Invalid value for `maximum_administration_fee`, must not be `None`")  # noqa: E501

        self._maximum_administration_fee = maximum_administration_fee

    @property
    def type_performance_fee(self):
        """Gets the type_performance_fee of this SurvivalPensionInvestmentFund.  # noqa: E501

        Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:    - Tipo de taxa de performance   # noqa: E501

        :return: The type_performance_fee of this SurvivalPensionInvestmentFund.  # noqa: E501
        :rtype: str
        """
        return self._type_performance_fee

    @type_performance_fee.setter
    def type_performance_fee(self, type_performance_fee):
        """Sets the type_performance_fee of this SurvivalPensionInvestmentFund.

        Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:    - Tipo de taxa de performance   # noqa: E501

        :param type_performance_fee: The type_performance_fee of this SurvivalPensionInvestmentFund.  # noqa: E501
        :type: str
        """
        if type_performance_fee is None:
            raise ValueError("Invalid value for `type_performance_fee`, must not be `None`")  # noqa: E501
        allowed_values = ["DIRETAMENTE", "INDIRETAMENTE", "NAO_APLICA"]  # noqa: E501
        if type_performance_fee not in allowed_values:
            raise ValueError(
                "Invalid value for `type_performance_fee` ({0}), must be one of {1}"  # noqa: E501
                .format(type_performance_fee, allowed_values)
            )

        self._type_performance_fee = type_performance_fee

    @property
    def maximum_performance_fee(self):
        """Gets the maximum_performance_fee of this SurvivalPensionInvestmentFund.  # noqa: E501

        Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:    - Taxa Máxima de Performance - em %   # noqa: E501

        :return: The maximum_performance_fee of this SurvivalPensionInvestmentFund.  # noqa: E501
        :rtype: str
        """
        return self._maximum_performance_fee

    @maximum_performance_fee.setter
    def maximum_performance_fee(self, maximum_performance_fee):
        """Sets the maximum_performance_fee of this SurvivalPensionInvestmentFund.

        Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:    - Taxa Máxima de Performance - em %   # noqa: E501

        :param maximum_performance_fee: The maximum_performance_fee of this SurvivalPensionInvestmentFund.  # noqa: E501
        :type: str
        """

        self._maximum_performance_fee = maximum_performance_fee

    @property
    def eligibility_rule(self):
        """Gets the eligibility_rule of this SurvivalPensionInvestmentFund.  # noqa: E501

        Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:   - Regra de Elegibilidade   # noqa: E501

        :return: The eligibility_rule of this SurvivalPensionInvestmentFund.  # noqa: E501
        :rtype: bool
        """
        return self._eligibility_rule

    @eligibility_rule.setter
    def eligibility_rule(self, eligibility_rule):
        """Sets the eligibility_rule of this SurvivalPensionInvestmentFund.

        Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:   - Regra de Elegibilidade   # noqa: E501

        :param eligibility_rule: The eligibility_rule of this SurvivalPensionInvestmentFund.  # noqa: E501
        :type: bool
        """

        self._eligibility_rule = eligibility_rule

    @property
    def minimum_contribution_amount(self):
        """Gets the minimum_contribution_amount of this SurvivalPensionInvestmentFund.  # noqa: E501

        Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:    - Valor Mínimo de Contribuição   # noqa: E501

        :return: The minimum_contribution_amount of this SurvivalPensionInvestmentFund.  # noqa: E501
        :rtype: str
        """
        return self._minimum_contribution_amount

    @minimum_contribution_amount.setter
    def minimum_contribution_amount(self, minimum_contribution_amount):
        """Sets the minimum_contribution_amount of this SurvivalPensionInvestmentFund.

        Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:    - Valor Mínimo de Contribuição   # noqa: E501

        :param minimum_contribution_amount: The minimum_contribution_amount of this SurvivalPensionInvestmentFund.  # noqa: E501
        :type: str
        """

        self._minimum_contribution_amount = minimum_contribution_amount

    @property
    def minimum_mathematical_provision_amount(self):
        """Gets the minimum_mathematical_provision_amount of this SurvivalPensionInvestmentFund.  # noqa: E501

        Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:    - Valor Mínimo do Saldo Provisão matemática   # noqa: E501

        :return: The minimum_mathematical_provision_amount of this SurvivalPensionInvestmentFund.  # noqa: E501
        :rtype: str
        """
        return self._minimum_mathematical_provision_amount

    @minimum_mathematical_provision_amount.setter
    def minimum_mathematical_provision_amount(self, minimum_mathematical_provision_amount):
        """Sets the minimum_mathematical_provision_amount of this SurvivalPensionInvestmentFund.

        Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:    - Valor Mínimo do Saldo Provisão matemática   # noqa: E501

        :param minimum_mathematical_provision_amount: The minimum_mathematical_provision_amount of this SurvivalPensionInvestmentFund.  # noqa: E501
        :type: str
        """

        self._minimum_mathematical_provision_amount = minimum_mathematical_provision_amount

    @property
    def currency(self):
        """Gets the currency of this SurvivalPensionInvestmentFund.  # noqa: E501


        :return: The currency of this SurvivalPensionInvestmentFund.  # noqa: E501
        :rtype: CurrencyCode
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SurvivalPensionInvestmentFund.


        :param currency: The currency of this SurvivalPensionInvestmentFund.  # noqa: E501
        :type: CurrencyCode
        """

        self._currency = currency

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
        if issubclass(SurvivalPensionInvestmentFund, dict):
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
        if not isinstance(other, SurvivalPensionInvestmentFund):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other