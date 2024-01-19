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

class InvestmentsFundGeneralConditionsRedemption(object):
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
        'quotation_days': 'int',
        'quotation_term': 'EnumInvestmentsFundGeneralConditionsTermType',
        'payment_days': 'int',
        'payment_term': 'EnumInvestmentsFundGeneralConditionsTermType',
        'grace_days': 'int'
    }

    attribute_map = {
        'quotation_days': 'quotationDays',
        'quotation_term': 'quotationTerm',
        'payment_days': 'paymentDays',
        'payment_term': 'paymentTerm',
        'grace_days': 'graceDays'
    }

    def __init__(self, quotation_days=None, quotation_term=None, payment_days=None, payment_term=None, grace_days=None):  # noqa: E501
        """InvestmentsFundGeneralConditionsRedemption - a model defined in Swagger"""  # noqa: E501
        self._quotation_days = None
        self._quotation_term = None
        self._payment_days = None
        self._payment_term = None
        self._grace_days = None
        self.discriminator = None
        self.quotation_days = quotation_days
        self.quotation_term = quotation_term
        self.payment_days = payment_days
        self.payment_term = payment_term
        if grace_days is not None:
            self.grace_days = grace_days

    @property
    def quotation_days(self):
        """Gets the quotation_days of this InvestmentsFundGeneralConditionsRedemption.  # noqa: E501

        Prazo máximo em dias indicado no regulamento do fundo para a conversão das cotas em dinheiro.  # noqa: E501

        :return: The quotation_days of this InvestmentsFundGeneralConditionsRedemption.  # noqa: E501
        :rtype: int
        """
        return self._quotation_days

    @quotation_days.setter
    def quotation_days(self, quotation_days):
        """Sets the quotation_days of this InvestmentsFundGeneralConditionsRedemption.

        Prazo máximo em dias indicado no regulamento do fundo para a conversão das cotas em dinheiro.  # noqa: E501

        :param quotation_days: The quotation_days of this InvestmentsFundGeneralConditionsRedemption.  # noqa: E501
        :type: int
        """
        if quotation_days is None:
            raise ValueError("Invalid value for `quotation_days`, must not be `None`")  # noqa: E501

        self._quotation_days = quotation_days

    @property
    def quotation_term(self):
        """Gets the quotation_term of this InvestmentsFundGeneralConditionsRedemption.  # noqa: E501


        :return: The quotation_term of this InvestmentsFundGeneralConditionsRedemption.  # noqa: E501
        :rtype: EnumInvestmentsFundGeneralConditionsTermType
        """
        return self._quotation_term

    @quotation_term.setter
    def quotation_term(self, quotation_term):
        """Sets the quotation_term of this InvestmentsFundGeneralConditionsRedemption.


        :param quotation_term: The quotation_term of this InvestmentsFundGeneralConditionsRedemption.  # noqa: E501
        :type: EnumInvestmentsFundGeneralConditionsTermType
        """
        if quotation_term is None:
            raise ValueError("Invalid value for `quotation_term`, must not be `None`")  # noqa: E501

        self._quotation_term = quotation_term

    @property
    def payment_days(self):
        """Gets the payment_days of this InvestmentsFundGeneralConditionsRedemption.  # noqa: E501

        Prazo máximo em dias do efetivo pagamento, pelo fundo, do valor líquido devido ao cotista que efetuou pedido de resgate.  # noqa: E501

        :return: The payment_days of this InvestmentsFundGeneralConditionsRedemption.  # noqa: E501
        :rtype: int
        """
        return self._payment_days

    @payment_days.setter
    def payment_days(self, payment_days):
        """Sets the payment_days of this InvestmentsFundGeneralConditionsRedemption.

        Prazo máximo em dias do efetivo pagamento, pelo fundo, do valor líquido devido ao cotista que efetuou pedido de resgate.  # noqa: E501

        :param payment_days: The payment_days of this InvestmentsFundGeneralConditionsRedemption.  # noqa: E501
        :type: int
        """
        if payment_days is None:
            raise ValueError("Invalid value for `payment_days`, must not be `None`")  # noqa: E501

        self._payment_days = payment_days

    @property
    def payment_term(self):
        """Gets the payment_term of this InvestmentsFundGeneralConditionsRedemption.  # noqa: E501


        :return: The payment_term of this InvestmentsFundGeneralConditionsRedemption.  # noqa: E501
        :rtype: EnumInvestmentsFundGeneralConditionsTermType
        """
        return self._payment_term

    @payment_term.setter
    def payment_term(self, payment_term):
        """Sets the payment_term of this InvestmentsFundGeneralConditionsRedemption.


        :param payment_term: The payment_term of this InvestmentsFundGeneralConditionsRedemption.  # noqa: E501
        :type: EnumInvestmentsFundGeneralConditionsTermType
        """
        if payment_term is None:
            raise ValueError("Invalid value for `payment_term`, must not be `None`")  # noqa: E501

        self._payment_term = payment_term

    @property
    def grace_days(self):
        """Gets the grace_days of this InvestmentsFundGeneralConditionsRedemption.  # noqa: E501

        Estabelece um período em quantidade de dias corridos em que o investidor não pode resgatar os recursos aplicados no fundo. Caso ocorra resgate antes do período, o investidor perderá a rentabilidade do período. Caso não exista, não informe o campo.  # noqa: E501

        :return: The grace_days of this InvestmentsFundGeneralConditionsRedemption.  # noqa: E501
        :rtype: int
        """
        return self._grace_days

    @grace_days.setter
    def grace_days(self, grace_days):
        """Sets the grace_days of this InvestmentsFundGeneralConditionsRedemption.

        Estabelece um período em quantidade de dias corridos em que o investidor não pode resgatar os recursos aplicados no fundo. Caso ocorra resgate antes do período, o investidor perderá a rentabilidade do período. Caso não exista, não informe o campo.  # noqa: E501

        :param grace_days: The grace_days of this InvestmentsFundGeneralConditionsRedemption.  # noqa: E501
        :type: int
        """

        self._grace_days = grace_days

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
        if issubclass(InvestmentsFundGeneralConditionsRedemption, dict):
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
        if not isinstance(other, InvestmentsFundGeneralConditionsRedemption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
