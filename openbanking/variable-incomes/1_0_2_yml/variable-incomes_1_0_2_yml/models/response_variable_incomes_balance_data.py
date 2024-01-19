# coding: utf-8

"""
    API Variable Incomes - Open Finance Brasil

    API de informações de operações de Renda Variável Open Finance Brasil – Fase 4.  API que retorna informações de operações de investimento do tipo Renda Variável mantidas nas instituições transmissoras por seus clientes, incluindo dados como informações do produto, quantidade, saldos em posição do cliente, movimentações financeiras e detalhes da nota de negociação.  Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints.  A granularidade de exposição de operações de renda variável se dá por cada ativo (ticker) da carteira do cliente.  Compartilhamento considera lote padrão e fracionário, entretanto, no Open Finance Brasil, as informações são consolidadas via ticker do lote padrão.  A defasagem em relação ao canal eletrônico da instituição deve ser o fechamento (pregão) do dia anterior (d-1).   Em relação ao aluguel de ações: neste momento não faz parte do escopo de compartilhamento a carteira/posição de aluguel do cliente (ativos alugados e movimentações relacionadas a esses ativos).  Apenas deve ser compartilhado as transações de pagamento ou recebimento de juros oriundos dos contratos de ações alugadas (ou doadas) pelos clientes.  Para o identificador do investimento (investmentId) deve ser adotado o seguinte comportamento:  - Após 12 meses sem movimentações e com quantidade de ativos zerada, o resourceId correspondente ao investmentId em questão deve passar ao status UNAVAILABLE (considerando consentimento válido);  - Nas situações em que o cliente compre novamente o ativo após um período de 12 meses sem movimentação e com quantidade de ativos zerada, o mesmo identificador (investmentId) deve ser utilizado. Especificamente para tais produtos, o status do recurso na resources deve passar de UNAVAILABLE para AVAILABLE.  Segue abaixo tabela com o escopo de produtos a ser considerado para compartilhamento:  ```    |----------------------|-------------------------------|----------------------|-----------------------------------|    | CLASSE DE ATIVOS     | PRODUTO                       | SUBPRODUTO           | DENOMINAÇÃO                       |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de Investimentos       |     -                | FIAGRO                            |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Ações                         | Subscrição           | Bonus / Direito / Recibo          |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de Investimentos       | Fundo imobiliario    | FII                               |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Ações                         | À vista              | ON / PN / UNIT                    |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF                  | ETF de Renda Variável             |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF                  | ETF Internacional                 |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF Renda Fixa       | ETF Renda Fixa                    |    |----------------------|-------------------------------|----------------------|-----------------------------------|    ```   # noqa: E501

    OpenAPI spec version: 1.0.2
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponseVariableIncomesBalanceData(object):
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
        'reference_date': 'date',
        'price_factor': 'str',
        'gross_amount': 'VariableIncomesBalancesGrossAmount',
        'blocked_balance': 'VariableIncomesBalancesBlockedBalance',
        'quantity': 'str',
        'closing_price': 'VariableIncomesBalancesClosingPrice'
    }

    attribute_map = {
        'reference_date': 'referenceDate',
        'price_factor': 'priceFactor',
        'gross_amount': 'grossAmount',
        'blocked_balance': 'blockedBalance',
        'quantity': 'quantity',
        'closing_price': 'closingPrice'
    }

    def __init__(self, reference_date=None, price_factor=None, gross_amount=None, blocked_balance=None, quantity=None, closing_price=None):  # noqa: E501
        """ResponseVariableIncomesBalanceData - a model defined in Swagger"""  # noqa: E501
        self._reference_date = None
        self._price_factor = None
        self._gross_amount = None
        self._blocked_balance = None
        self._quantity = None
        self._closing_price = None
        self.discriminator = None
        self.reference_date = reference_date
        self.price_factor = price_factor
        self.gross_amount = gross_amount
        self.blocked_balance = blocked_balance
        self.quantity = quantity
        self.closing_price = closing_price

    @property
    def reference_date(self):
        """Gets the reference_date of this ResponseVariableIncomesBalanceData.  # noqa: E501

        Posição fechada para o ativo da data do dia anterior.  # noqa: E501

        :return: The reference_date of this ResponseVariableIncomesBalanceData.  # noqa: E501
        :rtype: date
        """
        return self._reference_date

    @reference_date.setter
    def reference_date(self, reference_date):
        """Sets the reference_date of this ResponseVariableIncomesBalanceData.

        Posição fechada para o ativo da data do dia anterior.  # noqa: E501

        :param reference_date: The reference_date of this ResponseVariableIncomesBalanceData.  # noqa: E501
        :type: date
        """
        if reference_date is None:
            raise ValueError("Invalid value for `reference_date`, must not be `None`")  # noqa: E501

        self._reference_date = reference_date

    @property
    def price_factor(self):
        """Gets the price_factor of this ResponseVariableIncomesBalanceData.  # noqa: E501

        Fator que indica o número de ações utilizadas para a formação do preço. Valor informado deve ser maior que zero.   # noqa: E501

        :return: The price_factor of this ResponseVariableIncomesBalanceData.  # noqa: E501
        :rtype: str
        """
        return self._price_factor

    @price_factor.setter
    def price_factor(self, price_factor):
        """Sets the price_factor of this ResponseVariableIncomesBalanceData.

        Fator que indica o número de ações utilizadas para a formação do preço. Valor informado deve ser maior que zero.   # noqa: E501

        :param price_factor: The price_factor of this ResponseVariableIncomesBalanceData.  # noqa: E501
        :type: str
        """
        if price_factor is None:
            raise ValueError("Invalid value for `price_factor`, must not be `None`")  # noqa: E501

        self._price_factor = price_factor

    @property
    def gross_amount(self):
        """Gets the gross_amount of this ResponseVariableIncomesBalanceData.  # noqa: E501


        :return: The gross_amount of this ResponseVariableIncomesBalanceData.  # noqa: E501
        :rtype: VariableIncomesBalancesGrossAmount
        """
        return self._gross_amount

    @gross_amount.setter
    def gross_amount(self, gross_amount):
        """Sets the gross_amount of this ResponseVariableIncomesBalanceData.


        :param gross_amount: The gross_amount of this ResponseVariableIncomesBalanceData.  # noqa: E501
        :type: VariableIncomesBalancesGrossAmount
        """
        if gross_amount is None:
            raise ValueError("Invalid value for `gross_amount`, must not be `None`")  # noqa: E501

        self._gross_amount = gross_amount

    @property
    def blocked_balance(self):
        """Gets the blocked_balance of this ResponseVariableIncomesBalanceData.  # noqa: E501


        :return: The blocked_balance of this ResponseVariableIncomesBalanceData.  # noqa: E501
        :rtype: VariableIncomesBalancesBlockedBalance
        """
        return self._blocked_balance

    @blocked_balance.setter
    def blocked_balance(self, blocked_balance):
        """Sets the blocked_balance of this ResponseVariableIncomesBalanceData.


        :param blocked_balance: The blocked_balance of this ResponseVariableIncomesBalanceData.  # noqa: E501
        :type: VariableIncomesBalancesBlockedBalance
        """
        if blocked_balance is None:
            raise ValueError("Invalid value for `blocked_balance`, must not be `None`")  # noqa: E501

        self._blocked_balance = blocked_balance

    @property
    def quantity(self):
        """Gets the quantity of this ResponseVariableIncomesBalanceData.  # noqa: E501

        Quatidade total do ativo na data de referência.  # noqa: E501

        :return: The quantity of this ResponseVariableIncomesBalanceData.  # noqa: E501
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ResponseVariableIncomesBalanceData.

        Quatidade total do ativo na data de referência.  # noqa: E501

        :param quantity: The quantity of this ResponseVariableIncomesBalanceData.  # noqa: E501
        :type: str
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def closing_price(self):
        """Gets the closing_price of this ResponseVariableIncomesBalanceData.  # noqa: E501


        :return: The closing_price of this ResponseVariableIncomesBalanceData.  # noqa: E501
        :rtype: VariableIncomesBalancesClosingPrice
        """
        return self._closing_price

    @closing_price.setter
    def closing_price(self, closing_price):
        """Sets the closing_price of this ResponseVariableIncomesBalanceData.


        :param closing_price: The closing_price of this ResponseVariableIncomesBalanceData.  # noqa: E501
        :type: VariableIncomesBalancesClosingPrice
        """
        if closing_price is None:
            raise ValueError("Invalid value for `closing_price`, must not be `None`")  # noqa: E501

        self._closing_price = closing_price

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
        if issubclass(ResponseVariableIncomesBalanceData, dict):
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
        if not isinstance(other, ResponseVariableIncomesBalanceData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
