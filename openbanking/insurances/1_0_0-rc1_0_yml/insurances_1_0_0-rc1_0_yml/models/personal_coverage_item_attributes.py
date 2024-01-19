# coding: utf-8

"""
    API Seguros - Open Finance Brasil

    As APIs descritas neste documento são referentes a API de Seguros da fase OpenInsurance do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PersonalCoverageItemAttributes(object):
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
        'indemnity_payment_methods': 'list[str]',
        'indemnity_payment_frequencies': 'list[EnumPersonalIndemnityPaymentFrequencyType]',
        'min_value': 'InsurancePensionMinValue',
        'max_value': 'InsurancePensionMaxValue',
        'indemnifiable_periods': 'list[EnumPersonalIndemnifiablePeriodType]',
        'maximum_qty_indemnifiable_installments': 'int',
        'grace_period': 'GracePeriod',
        'differentiated_grace_period': 'GracePeriod',
        'deductible_days': 'int',
        'differentiated_deductible_days': 'int',
        'deductible': 'PersonalCoverageItemAttributesDeductible',
        'differentiated_deductible': 'PersonalCoverageItemAttributesDifferentiatedDeductible',
        'excluded_risks': 'list[EnumExcludedRisks]',
        'excluded_risks_url': 'str',
        'allow_apart_purchase': 'bool'
    }

    attribute_map = {
        'indemnity_payment_methods': 'indemnityPaymentMethods',
        'indemnity_payment_frequencies': 'indemnityPaymentFrequencies',
        'min_value': 'minValue',
        'max_value': 'maxValue',
        'indemnifiable_periods': 'indemnifiablePeriods',
        'maximum_qty_indemnifiable_installments': 'maximumQtyIndemnifiableInstallments',
        'grace_period': 'gracePeriod',
        'differentiated_grace_period': 'differentiatedGracePeriod',
        'deductible_days': 'deductibleDays',
        'differentiated_deductible_days': 'differentiatedDeductibleDays',
        'deductible': 'deductible',
        'differentiated_deductible': 'differentiatedDeductible',
        'excluded_risks': 'excludedRisks',
        'excluded_risks_url': 'excludedRisksURL',
        'allow_apart_purchase': 'allowApartPurchase'
    }

    def __init__(self, indemnity_payment_methods=None, indemnity_payment_frequencies=None, min_value=None, max_value=None, indemnifiable_periods=None, maximum_qty_indemnifiable_installments=None, grace_period=None, differentiated_grace_period=None, deductible_days=None, differentiated_deductible_days=None, deductible=None, differentiated_deductible=None, excluded_risks=None, excluded_risks_url=None, allow_apart_purchase=None):  # noqa: E501
        """PersonalCoverageItemAttributes - a model defined in Swagger"""  # noqa: E501
        self._indemnity_payment_methods = None
        self._indemnity_payment_frequencies = None
        self._min_value = None
        self._max_value = None
        self._indemnifiable_periods = None
        self._maximum_qty_indemnifiable_installments = None
        self._grace_period = None
        self._differentiated_grace_period = None
        self._deductible_days = None
        self._differentiated_deductible_days = None
        self._deductible = None
        self._differentiated_deductible = None
        self._excluded_risks = None
        self._excluded_risks_url = None
        self._allow_apart_purchase = None
        self.discriminator = None
        if indemnity_payment_methods is not None:
            self.indemnity_payment_methods = indemnity_payment_methods
        if indemnity_payment_frequencies is not None:
            self.indemnity_payment_frequencies = indemnity_payment_frequencies
        self.min_value = min_value
        self.max_value = max_value
        if indemnifiable_periods is not None:
            self.indemnifiable_periods = indemnifiable_periods
        if maximum_qty_indemnifiable_installments is not None:
            self.maximum_qty_indemnifiable_installments = maximum_qty_indemnifiable_installments
        self.grace_period = grace_period
        if differentiated_grace_period is not None:
            self.differentiated_grace_period = differentiated_grace_period
        if deductible_days is not None:
            self.deductible_days = deductible_days
        if differentiated_deductible_days is not None:
            self.differentiated_deductible_days = differentiated_deductible_days
        if deductible is not None:
            self.deductible = deductible
        if differentiated_deductible is not None:
            self.differentiated_deductible = differentiated_deductible
        if excluded_risks is not None:
            self.excluded_risks = excluded_risks
        if excluded_risks_url is not None:
            self.excluded_risks_url = excluded_risks_url
        if allow_apart_purchase is not None:
            self.allow_apart_purchase = allow_apart_purchase

    @property
    def indemnity_payment_methods(self):
        """Gets the indemnity_payment_methods of this PersonalCoverageItemAttributes.  # noqa: E501

        Listagem da forma de pagamento da indenização para cada combinação de modalidade/cobertura do produto.  # noqa: E501

        :return: The indemnity_payment_methods of this PersonalCoverageItemAttributes.  # noqa: E501
        :rtype: list[str]
        """
        return self._indemnity_payment_methods

    @indemnity_payment_methods.setter
    def indemnity_payment_methods(self, indemnity_payment_methods):
        """Sets the indemnity_payment_methods of this PersonalCoverageItemAttributes.

        Listagem da forma de pagamento da indenização para cada combinação de modalidade/cobertura do produto.  # noqa: E501

        :param indemnity_payment_methods: The indemnity_payment_methods of this PersonalCoverageItemAttributes.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["PAGAMENTO_CAPITAL_SEGURADO_VALOR_MONETARIO", "REEMBOLSO_DESPESAS", "PRESTACAO_SERVICOS"]  # noqa: E501
        if not set(indemnity_payment_methods).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `indemnity_payment_methods` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(indemnity_payment_methods) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._indemnity_payment_methods = indemnity_payment_methods

    @property
    def indemnity_payment_frequencies(self):
        """Gets the indemnity_payment_frequencies of this PersonalCoverageItemAttributes.  # noqa: E501

        Listagem de tipos de frequência de pagamento de indenização para cada combinação de modalidade/cobertura do produto.  # noqa: E501

        :return: The indemnity_payment_frequencies of this PersonalCoverageItemAttributes.  # noqa: E501
        :rtype: list[EnumPersonalIndemnityPaymentFrequencyType]
        """
        return self._indemnity_payment_frequencies

    @indemnity_payment_frequencies.setter
    def indemnity_payment_frequencies(self, indemnity_payment_frequencies):
        """Sets the indemnity_payment_frequencies of this PersonalCoverageItemAttributes.

        Listagem de tipos de frequência de pagamento de indenização para cada combinação de modalidade/cobertura do produto.  # noqa: E501

        :param indemnity_payment_frequencies: The indemnity_payment_frequencies of this PersonalCoverageItemAttributes.  # noqa: E501
        :type: list[EnumPersonalIndemnityPaymentFrequencyType]
        """

        self._indemnity_payment_frequencies = indemnity_payment_frequencies

    @property
    def min_value(self):
        """Gets the min_value of this PersonalCoverageItemAttributes.  # noqa: E501


        :return: The min_value of this PersonalCoverageItemAttributes.  # noqa: E501
        :rtype: InsurancePensionMinValue
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this PersonalCoverageItemAttributes.


        :param min_value: The min_value of this PersonalCoverageItemAttributes.  # noqa: E501
        :type: InsurancePensionMinValue
        """
        if min_value is None:
            raise ValueError("Invalid value for `min_value`, must not be `None`")  # noqa: E501

        self._min_value = min_value

    @property
    def max_value(self):
        """Gets the max_value of this PersonalCoverageItemAttributes.  # noqa: E501


        :return: The max_value of this PersonalCoverageItemAttributes.  # noqa: E501
        :rtype: InsurancePensionMaxValue
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this PersonalCoverageItemAttributes.


        :param max_value: The max_value of this PersonalCoverageItemAttributes.  # noqa: E501
        :type: InsurancePensionMaxValue
        """
        if max_value is None:
            raise ValueError("Invalid value for `max_value`, must not be `None`")  # noqa: E501

        self._max_value = max_value

    @property
    def indemnifiable_periods(self):
        """Gets the indemnifiable_periods of this PersonalCoverageItemAttributes.  # noqa: E501


        :return: The indemnifiable_periods of this PersonalCoverageItemAttributes.  # noqa: E501
        :rtype: list[EnumPersonalIndemnifiablePeriodType]
        """
        return self._indemnifiable_periods

    @indemnifiable_periods.setter
    def indemnifiable_periods(self, indemnifiable_periods):
        """Sets the indemnifiable_periods of this PersonalCoverageItemAttributes.


        :param indemnifiable_periods: The indemnifiable_periods of this PersonalCoverageItemAttributes.  # noqa: E501
        :type: list[EnumPersonalIndemnifiablePeriodType]
        """

        self._indemnifiable_periods = indemnifiable_periods

    @property
    def maximum_qty_indemnifiable_installments(self):
        """Gets the maximum_qty_indemnifiable_installments of this PersonalCoverageItemAttributes.  # noqa: E501

        Caso o período indenizável seja relacionado a parcelas, listagem de número máximo de parcelas indenizáveis para cada combinação de modalidade/ cobertura do produto.  # noqa: E501

        :return: The maximum_qty_indemnifiable_installments of this PersonalCoverageItemAttributes.  # noqa: E501
        :rtype: int
        """
        return self._maximum_qty_indemnifiable_installments

    @maximum_qty_indemnifiable_installments.setter
    def maximum_qty_indemnifiable_installments(self, maximum_qty_indemnifiable_installments):
        """Sets the maximum_qty_indemnifiable_installments of this PersonalCoverageItemAttributes.

        Caso o período indenizável seja relacionado a parcelas, listagem de número máximo de parcelas indenizáveis para cada combinação de modalidade/ cobertura do produto.  # noqa: E501

        :param maximum_qty_indemnifiable_installments: The maximum_qty_indemnifiable_installments of this PersonalCoverageItemAttributes.  # noqa: E501
        :type: int
        """

        self._maximum_qty_indemnifiable_installments = maximum_qty_indemnifiable_installments

    @property
    def grace_period(self):
        """Gets the grace_period of this PersonalCoverageItemAttributes.  # noqa: E501


        :return: The grace_period of this PersonalCoverageItemAttributes.  # noqa: E501
        :rtype: GracePeriod
        """
        return self._grace_period

    @grace_period.setter
    def grace_period(self, grace_period):
        """Sets the grace_period of this PersonalCoverageItemAttributes.


        :param grace_period: The grace_period of this PersonalCoverageItemAttributes.  # noqa: E501
        :type: GracePeriod
        """
        if grace_period is None:
            raise ValueError("Invalid value for `grace_period`, must not be `None`")  # noqa: E501

        self._grace_period = grace_period

    @property
    def differentiated_grace_period(self):
        """Gets the differentiated_grace_period of this PersonalCoverageItemAttributes.  # noqa: E501


        :return: The differentiated_grace_period of this PersonalCoverageItemAttributes.  # noqa: E501
        :rtype: GracePeriod
        """
        return self._differentiated_grace_period

    @differentiated_grace_period.setter
    def differentiated_grace_period(self, differentiated_grace_period):
        """Sets the differentiated_grace_period of this PersonalCoverageItemAttributes.


        :param differentiated_grace_period: The differentiated_grace_period of this PersonalCoverageItemAttributes.  # noqa: E501
        :type: GracePeriod
        """

        self._differentiated_grace_period = differentiated_grace_period

    @property
    def deductible_days(self):
        """Gets the deductible_days of this PersonalCoverageItemAttributes.  # noqa: E501

        Listagem de franquia em dias para cada combinação de modalidade/cobertura do produto.  # noqa: E501

        :return: The deductible_days of this PersonalCoverageItemAttributes.  # noqa: E501
        :rtype: int
        """
        return self._deductible_days

    @deductible_days.setter
    def deductible_days(self, deductible_days):
        """Sets the deductible_days of this PersonalCoverageItemAttributes.

        Listagem de franquia em dias para cada combinação de modalidade/cobertura do produto.  # noqa: E501

        :param deductible_days: The deductible_days of this PersonalCoverageItemAttributes.  # noqa: E501
        :type: int
        """

        self._deductible_days = deductible_days

    @property
    def differentiated_deductible_days(self):
        """Gets the differentiated_deductible_days of this PersonalCoverageItemAttributes.  # noqa: E501

        Detalhamento da franquia em dias diferentes para cada cobertura que exista alguma especificidade. Caso a seguradora não tenha essa diferenciação, não retornará nada no campo.  # noqa: E501

        :return: The differentiated_deductible_days of this PersonalCoverageItemAttributes.  # noqa: E501
        :rtype: int
        """
        return self._differentiated_deductible_days

    @differentiated_deductible_days.setter
    def differentiated_deductible_days(self, differentiated_deductible_days):
        """Sets the differentiated_deductible_days of this PersonalCoverageItemAttributes.

        Detalhamento da franquia em dias diferentes para cada cobertura que exista alguma especificidade. Caso a seguradora não tenha essa diferenciação, não retornará nada no campo.  # noqa: E501

        :param differentiated_deductible_days: The differentiated_deductible_days of this PersonalCoverageItemAttributes.  # noqa: E501
        :type: int
        """

        self._differentiated_deductible_days = differentiated_deductible_days

    @property
    def deductible(self):
        """Gets the deductible of this PersonalCoverageItemAttributes.  # noqa: E501


        :return: The deductible of this PersonalCoverageItemAttributes.  # noqa: E501
        :rtype: PersonalCoverageItemAttributesDeductible
        """
        return self._deductible

    @deductible.setter
    def deductible(self, deductible):
        """Sets the deductible of this PersonalCoverageItemAttributes.


        :param deductible: The deductible of this PersonalCoverageItemAttributes.  # noqa: E501
        :type: PersonalCoverageItemAttributesDeductible
        """

        self._deductible = deductible

    @property
    def differentiated_deductible(self):
        """Gets the differentiated_deductible of this PersonalCoverageItemAttributes.  # noqa: E501


        :return: The differentiated_deductible of this PersonalCoverageItemAttributes.  # noqa: E501
        :rtype: PersonalCoverageItemAttributesDifferentiatedDeductible
        """
        return self._differentiated_deductible

    @differentiated_deductible.setter
    def differentiated_deductible(self, differentiated_deductible):
        """Sets the differentiated_deductible of this PersonalCoverageItemAttributes.


        :param differentiated_deductible: The differentiated_deductible of this PersonalCoverageItemAttributes.  # noqa: E501
        :type: PersonalCoverageItemAttributesDifferentiatedDeductible
        """

        self._differentiated_deductible = differentiated_deductible

    @property
    def excluded_risks(self):
        """Gets the excluded_risks of this PersonalCoverageItemAttributes.  # noqa: E501


        :return: The excluded_risks of this PersonalCoverageItemAttributes.  # noqa: E501
        :rtype: list[EnumExcludedRisks]
        """
        return self._excluded_risks

    @excluded_risks.setter
    def excluded_risks(self, excluded_risks):
        """Sets the excluded_risks of this PersonalCoverageItemAttributes.


        :param excluded_risks: The excluded_risks of this PersonalCoverageItemAttributes.  # noqa: E501
        :type: list[EnumExcludedRisks]
        """

        self._excluded_risks = excluded_risks

    @property
    def excluded_risks_url(self):
        """Gets the excluded_risks_url of this PersonalCoverageItemAttributes.  # noqa: E501

        Campo aberto (possibilidade de incluir URL)  # noqa: E501

        :return: The excluded_risks_url of this PersonalCoverageItemAttributes.  # noqa: E501
        :rtype: str
        """
        return self._excluded_risks_url

    @excluded_risks_url.setter
    def excluded_risks_url(self, excluded_risks_url):
        """Sets the excluded_risks_url of this PersonalCoverageItemAttributes.

        Campo aberto (possibilidade de incluir URL)  # noqa: E501

        :param excluded_risks_url: The excluded_risks_url of this PersonalCoverageItemAttributes.  # noqa: E501
        :type: str
        """

        self._excluded_risks_url = excluded_risks_url

    @property
    def allow_apart_purchase(self):
        """Gets the allow_apart_purchase of this PersonalCoverageItemAttributes.  # noqa: E501

        Indicar se a cobertura pode ser contratada isoladamente ou não:   1. true   2. false   # noqa: E501

        :return: The allow_apart_purchase of this PersonalCoverageItemAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._allow_apart_purchase

    @allow_apart_purchase.setter
    def allow_apart_purchase(self, allow_apart_purchase):
        """Sets the allow_apart_purchase of this PersonalCoverageItemAttributes.

        Indicar se a cobertura pode ser contratada isoladamente ou não:   1. true   2. false   # noqa: E501

        :param allow_apart_purchase: The allow_apart_purchase of this PersonalCoverageItemAttributes.  # noqa: E501
        :type: bool
        """

        self._allow_apart_purchase = allow_apart_purchase

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
        if issubclass(PersonalCoverageItemAttributes, dict):
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
        if not isinstance(other, PersonalCoverageItemAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
