# coding: utf-8

"""
    API Pension - Open Finance Brasil

    API de Previdência do Open Finance Brasil – Fase 4. API que retorna informações de Previdência.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SurvivalPensionGrantPeriodBenefit(object):
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
        'income_modalities': 'list[str]',
        'biometric_table': 'list[str]',
        'interest_rate': 'str',
        'update_index': 'UpdateIndex',
        'reversal_financial_results': 'str',
        'investment_funds': 'list[SurvivalPensionInvestmentFund]'
    }

    attribute_map = {
        'income_modalities': 'incomeModalities',
        'biometric_table': 'biometricTable',
        'interest_rate': 'interestRate',
        'update_index': 'updateIndex',
        'reversal_financial_results': 'reversalFinancialResults',
        'investment_funds': 'investmentFunds'
    }

    def __init__(self, income_modalities=None, biometric_table=None, interest_rate=None, update_index=None, reversal_financial_results=None, investment_funds=None):  # noqa: E501
        """SurvivalPensionGrantPeriodBenefit - a model defined in Swagger"""  # noqa: E501
        self._income_modalities = None
        self._biometric_table = None
        self._interest_rate = None
        self._update_index = None
        self._reversal_financial_results = None
        self._investment_funds = None
        self.discriminator = None
        self.income_modalities = income_modalities
        if biometric_table is not None:
            self.biometric_table = biometric_table
        if interest_rate is not None:
            self.interest_rate = interest_rate
        if update_index is not None:
            self.update_index = update_index
        if reversal_financial_results is not None:
            self.reversal_financial_results = reversal_financial_results
        if investment_funds is not None:
            self.investment_funds = investment_funds

    @property
    def income_modalities(self):
        """Gets the income_modalities of this SurvivalPensionGrantPeriodBenefit.  # noqa: E501


        :return: The income_modalities of this SurvivalPensionGrantPeriodBenefit.  # noqa: E501
        :rtype: list[str]
        """
        return self._income_modalities

    @income_modalities.setter
    def income_modalities(self, income_modalities):
        """Sets the income_modalities of this SurvivalPensionGrantPeriodBenefit.


        :param income_modalities: The income_modalities of this SurvivalPensionGrantPeriodBenefit.  # noqa: E501
        :type: list[str]
        """
        if income_modalities is None:
            raise ValueError("Invalid value for `income_modalities`, must not be `None`")  # noqa: E501
        allowed_values = ["PAGAMENTO_UNICO", "RENDA_PRAZO_CERTO", "RENDA_TEMPORARIA", "RENDA_TEMPORARIA_REVERSIVEL", "RENDA_TEMPORARIA_MINMO_GARANTIDO", "RENDA_TEMPORARIA_REVERSIVEL_MININO_GARANTIDO", "RENDA_VITALICIA", "RENDA_VITALICIA_REVERSIVEL_BENEFICIARIO_INDICADO", "RENDA_VITALICIA_CONJUGE_CONTINUIDADE_MENORES", "RENDA_VITALICIA_MINIMO_GARANTIDO", "RENDA_VITALICIA_PRAZO_MINIMO_GRANTIDO"]  # noqa: E501
        if not set(income_modalities).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `income_modalities` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(income_modalities) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._income_modalities = income_modalities

    @property
    def biometric_table(self):
        """Gets the biometric_table of this SurvivalPensionGrantPeriodBenefit.  # noqa: E501


        :return: The biometric_table of this SurvivalPensionGrantPeriodBenefit.  # noqa: E501
        :rtype: list[str]
        """
        return self._biometric_table

    @biometric_table.setter
    def biometric_table(self, biometric_table):
        """Sets the biometric_table of this SurvivalPensionGrantPeriodBenefit.


        :param biometric_table: The biometric_table of this SurvivalPensionGrantPeriodBenefit.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["AT_2000_MALE", "AT_2000_FEMALE", "AT_2000_MALE_FEMALE", "AT_2000_MALE_SUAVIZADA_10", "AT_2000_FEMALE_SUAVIZADA_10", "AT_2000_MALE_FEMALE_SUAVIZADA_10", "AT_2000_MALE_SUAVIZADA_15", "AT_2000_FEMALE_SUAVIZADA_15", "AT_2000_MALE_FEMALE_SUAVIZADA_15", "AT_83_MALE", "AT_83_FEMALE", "AT_83_MALE_FEMALE", "BR_EMSSB_MALE", "BR_EMSSB_FEMALE", "BR_EMSSB_MALE_FEMALE"]  # noqa: E501
        if not set(biometric_table).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `biometric_table` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(biometric_table) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._biometric_table = biometric_table

    @property
    def interest_rate(self):
        """Gets the interest_rate of this SurvivalPensionGrantPeriodBenefit.  # noqa: E501

        Taxa de juros garantida utilizada para conversão em renda. Em %  # noqa: E501

        :return: The interest_rate of this SurvivalPensionGrantPeriodBenefit.  # noqa: E501
        :rtype: str
        """
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        """Sets the interest_rate of this SurvivalPensionGrantPeriodBenefit.

        Taxa de juros garantida utilizada para conversão em renda. Em %  # noqa: E501

        :param interest_rate: The interest_rate of this SurvivalPensionGrantPeriodBenefit.  # noqa: E501
        :type: str
        """

        self._interest_rate = interest_rate

    @property
    def update_index(self):
        """Gets the update_index of this SurvivalPensionGrantPeriodBenefit.  # noqa: E501


        :return: The update_index of this SurvivalPensionGrantPeriodBenefit.  # noqa: E501
        :rtype: UpdateIndex
        """
        return self._update_index

    @update_index.setter
    def update_index(self, update_index):
        """Sets the update_index of this SurvivalPensionGrantPeriodBenefit.


        :param update_index: The update_index of this SurvivalPensionGrantPeriodBenefit.  # noqa: E501
        :type: UpdateIndex
        """

        self._update_index = update_index

    @property
    def reversal_financial_results(self):
        """Gets the reversal_financial_results of this SurvivalPensionGrantPeriodBenefit.  # noqa: E501

        Percentual de reversão de excedente financeiro na concessão. Em %.  # noqa: E501

        :return: The reversal_financial_results of this SurvivalPensionGrantPeriodBenefit.  # noqa: E501
        :rtype: str
        """
        return self._reversal_financial_results

    @reversal_financial_results.setter
    def reversal_financial_results(self, reversal_financial_results):
        """Sets the reversal_financial_results of this SurvivalPensionGrantPeriodBenefit.

        Percentual de reversão de excedente financeiro na concessão. Em %.  # noqa: E501

        :param reversal_financial_results: The reversal_financial_results of this SurvivalPensionGrantPeriodBenefit.  # noqa: E501
        :type: str
        """

        self._reversal_financial_results = reversal_financial_results

    @property
    def investment_funds(self):
        """Gets the investment_funds of this SurvivalPensionGrantPeriodBenefit.  # noqa: E501


        :return: The investment_funds of this SurvivalPensionGrantPeriodBenefit.  # noqa: E501
        :rtype: list[SurvivalPensionInvestmentFund]
        """
        return self._investment_funds

    @investment_funds.setter
    def investment_funds(self, investment_funds):
        """Sets the investment_funds of this SurvivalPensionGrantPeriodBenefit.


        :param investment_funds: The investment_funds of this SurvivalPensionGrantPeriodBenefit.  # noqa: E501
        :type: list[SurvivalPensionInvestmentFund]
        """

        self._investment_funds = investment_funds

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
        if issubclass(SurvivalPensionGrantPeriodBenefit, dict):
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
        if not isinstance(other, SurvivalPensionGrantPeriodBenefit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
