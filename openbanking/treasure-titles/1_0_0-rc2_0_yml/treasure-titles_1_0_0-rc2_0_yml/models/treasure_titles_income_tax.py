# coding: utf-8

"""
    API Treasure Titles - Open Finance Brasil

    API de informações de operações de Títulos do Tesouro Direto Open Finance Brasil – Fase 4. API que retorna informações de operações de investimento do tipo Títulos do Tesouro Direto mantidas nas instituições transmissoras por seus clientes, incluindo dados como informações do produto, quantidade, saldos em posição do cliente e movimentações financeiras. Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints. Devem ser considerados como escopo de exposição todos os títulos ofertados pelo Tesouro Direto. A exposição se dará por cada operação de títulos do Tesouro Direto contratada pelo cliente.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TreasureTitlesIncomeTax(object):
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
        'amount': 'TreasureTitlesIncomeTaxAmount',
        'currency': 'TreasureTitlesCurrency'
    }

    attribute_map = {
        'amount': 'amount',
        'currency': 'currency'
    }

    def __init__(self, amount=None, currency=None):  # noqa: E501
        """TreasureTitlesIncomeTax - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._currency = None
        self.discriminator = None
        self.amount = amount
        self.currency = currency

    @property
    def amount(self):
        """Gets the amount of this TreasureTitlesIncomeTax.  # noqa: E501


        :return: The amount of this TreasureTitlesIncomeTax.  # noqa: E501
        :rtype: TreasureTitlesIncomeTaxAmount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TreasureTitlesIncomeTax.


        :param amount: The amount of this TreasureTitlesIncomeTax.  # noqa: E501
        :type: TreasureTitlesIncomeTaxAmount
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this TreasureTitlesIncomeTax.  # noqa: E501


        :return: The currency of this TreasureTitlesIncomeTax.  # noqa: E501
        :rtype: TreasureTitlesCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this TreasureTitlesIncomeTax.


        :param currency: The currency of this TreasureTitlesIncomeTax.  # noqa: E501
        :type: TreasureTitlesCurrency
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

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
        if issubclass(TreasureTitlesIncomeTax, dict):
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
        if not isinstance(other, TreasureTitlesIncomeTax):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
