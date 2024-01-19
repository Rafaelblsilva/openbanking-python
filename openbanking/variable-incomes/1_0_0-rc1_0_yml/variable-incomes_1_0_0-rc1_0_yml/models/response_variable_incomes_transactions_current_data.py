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

class ResponseVariableIncomesTransactionsCurrentData(object):
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
        'type': 'EnumVariableIncomesTransactionsCurrentType',
        'transaction_type': 'EnumVariableIncomesTransactionsCurrentTransactionType',
        'type_additional_info': 'str',
        'transaction_date': 'date',
        'price_factor': 'str',
        'transaction_unit_price': 'ResponseVariableIncomesTransactionsDataTransactionUnitPrice',
        'transaction_quantity': 'str',
        'transaction_value': 'ResponseVariableIncomesTransactionsDataTransactionValue',
        'transaction_id': 'str',
        'broker_note_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'transaction_type': 'transactionType',
        'type_additional_info': 'typeAdditionalInfo',
        'transaction_date': 'transactionDate',
        'price_factor': 'priceFactor',
        'transaction_unit_price': 'transactionUnitPrice',
        'transaction_quantity': 'transactionQuantity',
        'transaction_value': 'transactionValue',
        'transaction_id': 'transactionId',
        'broker_note_id': 'brokerNoteId'
    }

    def __init__(self, type=None, transaction_type=None, type_additional_info=None, transaction_date=None, price_factor=None, transaction_unit_price=None, transaction_quantity=None, transaction_value=None, transaction_id=None, broker_note_id=None):  # noqa: E501
        """ResponseVariableIncomesTransactionsCurrentData - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._transaction_type = None
        self._type_additional_info = None
        self._transaction_date = None
        self._price_factor = None
        self._transaction_unit_price = None
        self._transaction_quantity = None
        self._transaction_value = None
        self._transaction_id = None
        self._broker_note_id = None
        self.discriminator = None
        self.type = type
        self.transaction_type = transaction_type
        if type_additional_info is not None:
            self.type_additional_info = type_additional_info
        self.transaction_date = transaction_date
        if price_factor is not None:
            self.price_factor = price_factor
        if transaction_unit_price is not None:
            self.transaction_unit_price = transaction_unit_price
        if transaction_quantity is not None:
            self.transaction_quantity = transaction_quantity
        self.transaction_value = transaction_value
        self.transaction_id = transaction_id
        if broker_note_id is not None:
            self.broker_note_id = broker_note_id

    @property
    def type(self):
        """Gets the type of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501


        :return: The type of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :rtype: EnumVariableIncomesTransactionsCurrentType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResponseVariableIncomesTransactionsCurrentData.


        :param type: The type of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :type: EnumVariableIncomesTransactionsCurrentType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def transaction_type(self):
        """Gets the transaction_type of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501


        :return: The transaction_type of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :rtype: EnumVariableIncomesTransactionsCurrentTransactionType
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this ResponseVariableIncomesTransactionsCurrentData.


        :param transaction_type: The transaction_type of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :type: EnumVariableIncomesTransactionsCurrentTransactionType
        """
        if transaction_type is None:
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501

        self._transaction_type = transaction_type

    @property
    def type_additional_info(self):
        """Gets the type_additional_info of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501

        Informação adicional do tipo de movimentação, para preenchimento no caso de movimentações não delimitadas no domínio.  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo 'transactionType' for preenchido com o valor 'OUTROS'.   # noqa: E501

        :return: The type_additional_info of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :rtype: str
        """
        return self._type_additional_info

    @type_additional_info.setter
    def type_additional_info(self, type_additional_info):
        """Sets the type_additional_info of this ResponseVariableIncomesTransactionsCurrentData.

        Informação adicional do tipo de movimentação, para preenchimento no caso de movimentações não delimitadas no domínio.  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo 'transactionType' for preenchido com o valor 'OUTROS'.   # noqa: E501

        :param type_additional_info: The type_additional_info of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :type: str
        """

        self._type_additional_info = type_additional_info

    @property
    def transaction_date(self):
        """Gets the transaction_date of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501

        Data da movimentação.  [Restrição] Data do pregão: compartilhar movimentos até a data da posição.   # noqa: E501

        :return: The transaction_date of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :rtype: date
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        """Sets the transaction_date of this ResponseVariableIncomesTransactionsCurrentData.

        Data da movimentação.  [Restrição] Data do pregão: compartilhar movimentos até a data da posição.   # noqa: E501

        :param transaction_date: The transaction_date of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :type: date
        """
        if transaction_date is None:
            raise ValueError("Invalid value for `transaction_date`, must not be `None`")  # noqa: E501

        self._transaction_date = transaction_date

    @property
    def price_factor(self):
        """Gets the price_factor of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501

        Fator que indica o número de ações utilizadas para a formação do preço. Valor informado deve ser maior que zero.   # noqa: E501

        :return: The price_factor of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :rtype: str
        """
        return self._price_factor

    @price_factor.setter
    def price_factor(self, price_factor):
        """Sets the price_factor of this ResponseVariableIncomesTransactionsCurrentData.

        Fator que indica o número de ações utilizadas para a formação do preço. Valor informado deve ser maior que zero.   # noqa: E501

        :param price_factor: The price_factor of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :type: str
        """

        self._price_factor = price_factor

    @property
    def transaction_unit_price(self):
        """Gets the transaction_unit_price of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501


        :return: The transaction_unit_price of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :rtype: ResponseVariableIncomesTransactionsDataTransactionUnitPrice
        """
        return self._transaction_unit_price

    @transaction_unit_price.setter
    def transaction_unit_price(self, transaction_unit_price):
        """Sets the transaction_unit_price of this ResponseVariableIncomesTransactionsCurrentData.


        :param transaction_unit_price: The transaction_unit_price of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :type: ResponseVariableIncomesTransactionsDataTransactionUnitPrice
        """

        self._transaction_unit_price = transaction_unit_price

    @property
    def transaction_quantity(self):
        """Gets the transaction_quantity of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501

        Quantidade de ativos movimentados.  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo 'transactionType' for preenchido com os valores 'COMPRA', 'VENDA' ou 'ALUGUEIS'.   # noqa: E501

        :return: The transaction_quantity of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_quantity

    @transaction_quantity.setter
    def transaction_quantity(self, transaction_quantity):
        """Sets the transaction_quantity of this ResponseVariableIncomesTransactionsCurrentData.

        Quantidade de ativos movimentados.  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo 'transactionType' for preenchido com os valores 'COMPRA', 'VENDA' ou 'ALUGUEIS'.   # noqa: E501

        :param transaction_quantity: The transaction_quantity of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :type: str
        """

        self._transaction_quantity = transaction_quantity

    @property
    def transaction_value(self):
        """Gets the transaction_value of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501


        :return: The transaction_value of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :rtype: ResponseVariableIncomesTransactionsDataTransactionValue
        """
        return self._transaction_value

    @transaction_value.setter
    def transaction_value(self, transaction_value):
        """Sets the transaction_value of this ResponseVariableIncomesTransactionsCurrentData.


        :param transaction_value: The transaction_value of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :type: ResponseVariableIncomesTransactionsDataTransactionValue
        """
        if transaction_value is None:
            raise ValueError("Invalid value for `transaction_value`, must not be `None`")  # noqa: E501

        self._transaction_value = transaction_value

    @property
    def transaction_id(self):
        """Gets the transaction_id of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501

        Código ou identificador único prestado pela instituição que mantém a representação individual do movimento.  # noqa: E501

        :return: The transaction_id of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this ResponseVariableIncomesTransactionsCurrentData.

        Código ou identificador único prestado pela instituição que mantém a representação individual do movimento.  # noqa: E501

        :param transaction_id: The transaction_id of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :type: str
        """
        if transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501

        self._transaction_id = transaction_id

    @property
    def broker_note_id(self):
        """Gets the broker_note_id of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501

        Identificador da nota de negociação.  [Restrição] Informação de envio obrigatório caso o motivo da movimentação seja compra ou venda.   # noqa: E501

        :return: The broker_note_id of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :rtype: str
        """
        return self._broker_note_id

    @broker_note_id.setter
    def broker_note_id(self, broker_note_id):
        """Sets the broker_note_id of this ResponseVariableIncomesTransactionsCurrentData.

        Identificador da nota de negociação.  [Restrição] Informação de envio obrigatório caso o motivo da movimentação seja compra ou venda.   # noqa: E501

        :param broker_note_id: The broker_note_id of this ResponseVariableIncomesTransactionsCurrentData.  # noqa: E501
        :type: str
        """

        self._broker_note_id = broker_note_id

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
        if issubclass(ResponseVariableIncomesTransactionsCurrentData, dict):
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
        if not isinstance(other, ResponseVariableIncomesTransactionsCurrentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
