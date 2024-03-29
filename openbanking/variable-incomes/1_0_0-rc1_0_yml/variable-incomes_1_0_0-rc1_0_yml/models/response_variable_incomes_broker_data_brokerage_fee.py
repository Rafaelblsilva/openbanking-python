# coding: utf-8

"""
    API Variable Incomes - Open Finance Brasil

    API de informações de operações de Renda Variável Open Finance Brasil – Fase 4.  API que retorna informações de operações de investimento do tipo Renda Variável mantidas nas instituições transmissoras por seus clientes, incluindo dados como informações do produto, quantidade, saldos em posição do cliente, movimentações financeiras e detalhes da nota de negociação.  Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints. A granularidade de exposição de operações de renda variável se dá por cada ativo (ticker) da carteira do cliente. Segue abaixo tabela com o escopo de produtos a ser considerado para compartilhamento:  ```    |----------------------|-------------------------------|----------------------|-----------------------------------|    | CLASSE DE ATIVOS     | PRODUTO                       | SUBPRODUTO           | DENOMINAÇÃO                       |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de Investimentos       |     -                | FIAGRO                            |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Ações                         | Subscrição           | Bonus / Direito / Recibo          |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de Investimentos       | Fundo imobiliario    | FII                               |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Ações                         | À vista              | ON / PN / UNIT                    |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF                  | ETF de Renda Variável             |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF                  | ETF Internacional                 |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF Renda Fixa       | ETF Renda Fixa                    |    |----------------------|-------------------------------|----------------------|-----------------------------------|    ```   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponseVariableIncomesBrokerDataBrokerageFee(object):
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
        'amount': 'str',
        'currency': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'currency': 'currency'
    }

    def __init__(self, amount=None, currency=None):  # noqa: E501
        """ResponseVariableIncomesBrokerDataBrokerageFee - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._currency = None
        self.discriminator = None
        self.amount = amount
        self.currency = currency

    @property
    def amount(self):
        """Gets the amount of this ResponseVariableIncomesBrokerDataBrokerageFee.  # noqa: E501

        Valor relacionado ao objeto.  # noqa: E501

        :return: The amount of this ResponseVariableIncomesBrokerDataBrokerageFee.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ResponseVariableIncomesBrokerDataBrokerageFee.

        Valor relacionado ao objeto.  # noqa: E501

        :param amount: The amount of this ResponseVariableIncomesBrokerDataBrokerageFee.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this ResponseVariableIncomesBrokerDataBrokerageFee.  # noqa: E501

        Moeda referente ao valor monetário, seguindo o modelo ISO-4217.  # noqa: E501

        :return: The currency of this ResponseVariableIncomesBrokerDataBrokerageFee.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ResponseVariableIncomesBrokerDataBrokerageFee.

        Moeda referente ao valor monetário, seguindo o modelo ISO-4217.  # noqa: E501

        :param currency: The currency of this ResponseVariableIncomesBrokerDataBrokerageFee.  # noqa: E501
        :type: str
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
        if issubclass(ResponseVariableIncomesBrokerDataBrokerageFee, dict):
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
        if not isinstance(other, ResponseVariableIncomesBrokerDataBrokerageFee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
