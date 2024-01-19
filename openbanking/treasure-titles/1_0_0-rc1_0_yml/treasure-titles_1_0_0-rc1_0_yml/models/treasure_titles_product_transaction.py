# coding: utf-8

"""
    API Treasure Titles - Open Finance Brasil

    API de informações de operações de Títulos do Tesouro Direto Open Finance Brasil – Fase 4. API que retorna informações de operações de investimento do tipo Títulos do Tesouro Direto mantidas nas instituições transmissoras por seus clientes, incluindo dados como informações do produto, quantidade, saldos em posição do cliente e movimentações financeiras. Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints. Devem ser considerados como escopo de exposição todos os títulos ofertados pelo Tesouro Direto. A exposição se dará por cada operação de títulos do Tesouro Direto contratada pelo cliente.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TreasureTitlesProductTransaction(object):
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
        'type': 'TreasureTitlesType',
        'transaction_type': 'TreasureTitlesTransactionType',
        'transaction_type_additional_info': 'str',
        'transaction_date': 'TreasureTitlesTransactionDate',
        'transaction_unit_price': 'TreasureTitlesTransactionUnitPrice',
        'transaction_quantity': 'TreasureTitlesTransactionQuantity',
        'transaction_gross_value': 'TreasureTitlesTransactionGrossValue',
        'income_tax': 'TreasureTitlesProductTransactionIncomeTax',
        'financial_transaction_tax': 'TreasureTitlesProductTransactionFinancialTransactionTax',
        'transaction_net_value': 'TreasureTitlesTransactionNetValue',
        'remuneration_transaction_rate': 'TreasureTitlesRemunerationTransactionRate',
        'transaction_id': 'TreasureTitlesTransactionId'
    }

    attribute_map = {
        'type': 'type',
        'transaction_type': 'transactionType',
        'transaction_type_additional_info': 'transactionTypeAdditionalInfo',
        'transaction_date': 'transactionDate',
        'transaction_unit_price': 'transactionUnitPrice',
        'transaction_quantity': 'transactionQuantity',
        'transaction_gross_value': 'transactionGrossValue',
        'income_tax': 'incomeTax',
        'financial_transaction_tax': 'financialTransactionTax',
        'transaction_net_value': 'transactionNetValue',
        'remuneration_transaction_rate': 'remunerationTransactionRate',
        'transaction_id': 'transactionId'
    }

    def __init__(self, type=None, transaction_type=None, transaction_type_additional_info=None, transaction_date=None, transaction_unit_price=None, transaction_quantity=None, transaction_gross_value=None, income_tax=None, financial_transaction_tax=None, transaction_net_value=None, remuneration_transaction_rate=None, transaction_id=None):  # noqa: E501
        """TreasureTitlesProductTransaction - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._transaction_type = None
        self._transaction_type_additional_info = None
        self._transaction_date = None
        self._transaction_unit_price = None
        self._transaction_quantity = None
        self._transaction_gross_value = None
        self._income_tax = None
        self._financial_transaction_tax = None
        self._transaction_net_value = None
        self._remuneration_transaction_rate = None
        self._transaction_id = None
        self.discriminator = None
        self.type = type
        self.transaction_type = transaction_type
        if transaction_type_additional_info is not None:
            self.transaction_type_additional_info = transaction_type_additional_info
        self.transaction_date = transaction_date
        self.transaction_unit_price = transaction_unit_price
        self.transaction_quantity = transaction_quantity
        self.transaction_gross_value = transaction_gross_value
        if income_tax is not None:
            self.income_tax = income_tax
        if financial_transaction_tax is not None:
            self.financial_transaction_tax = financial_transaction_tax
        self.transaction_net_value = transaction_net_value
        if remuneration_transaction_rate is not None:
            self.remuneration_transaction_rate = remuneration_transaction_rate
        self.transaction_id = transaction_id

    @property
    def type(self):
        """Gets the type of this TreasureTitlesProductTransaction.  # noqa: E501


        :return: The type of this TreasureTitlesProductTransaction.  # noqa: E501
        :rtype: TreasureTitlesType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TreasureTitlesProductTransaction.


        :param type: The type of this TreasureTitlesProductTransaction.  # noqa: E501
        :type: TreasureTitlesType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def transaction_type(self):
        """Gets the transaction_type of this TreasureTitlesProductTransaction.  # noqa: E501


        :return: The transaction_type of this TreasureTitlesProductTransaction.  # noqa: E501
        :rtype: TreasureTitlesTransactionType
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this TreasureTitlesProductTransaction.


        :param transaction_type: The transaction_type of this TreasureTitlesProductTransaction.  # noqa: E501
        :type: TreasureTitlesTransactionType
        """
        if transaction_type is None:
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501

        self._transaction_type = transaction_type

    @property
    def transaction_type_additional_info(self):
        """Gets the transaction_type_additional_info of this TreasureTitlesProductTransaction.  # noqa: E501

        Informação adicional do tipo de movimentação, para preenchimento no caso de movimentações não de limitadas no domínio.  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo 'transactionType' for preenchido com o valor 'OUTROS'.   # noqa: E501

        :return: The transaction_type_additional_info of this TreasureTitlesProductTransaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type_additional_info

    @transaction_type_additional_info.setter
    def transaction_type_additional_info(self, transaction_type_additional_info):
        """Sets the transaction_type_additional_info of this TreasureTitlesProductTransaction.

        Informação adicional do tipo de movimentação, para preenchimento no caso de movimentações não de limitadas no domínio.  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo 'transactionType' for preenchido com o valor 'OUTROS'.   # noqa: E501

        :param transaction_type_additional_info: The transaction_type_additional_info of this TreasureTitlesProductTransaction.  # noqa: E501
        :type: str
        """

        self._transaction_type_additional_info = transaction_type_additional_info

    @property
    def transaction_date(self):
        """Gets the transaction_date of this TreasureTitlesProductTransaction.  # noqa: E501


        :return: The transaction_date of this TreasureTitlesProductTransaction.  # noqa: E501
        :rtype: TreasureTitlesTransactionDate
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        """Sets the transaction_date of this TreasureTitlesProductTransaction.


        :param transaction_date: The transaction_date of this TreasureTitlesProductTransaction.  # noqa: E501
        :type: TreasureTitlesTransactionDate
        """
        if transaction_date is None:
            raise ValueError("Invalid value for `transaction_date`, must not be `None`")  # noqa: E501

        self._transaction_date = transaction_date

    @property
    def transaction_unit_price(self):
        """Gets the transaction_unit_price of this TreasureTitlesProductTransaction.  # noqa: E501


        :return: The transaction_unit_price of this TreasureTitlesProductTransaction.  # noqa: E501
        :rtype: TreasureTitlesTransactionUnitPrice
        """
        return self._transaction_unit_price

    @transaction_unit_price.setter
    def transaction_unit_price(self, transaction_unit_price):
        """Sets the transaction_unit_price of this TreasureTitlesProductTransaction.


        :param transaction_unit_price: The transaction_unit_price of this TreasureTitlesProductTransaction.  # noqa: E501
        :type: TreasureTitlesTransactionUnitPrice
        """
        if transaction_unit_price is None:
            raise ValueError("Invalid value for `transaction_unit_price`, must not be `None`")  # noqa: E501

        self._transaction_unit_price = transaction_unit_price

    @property
    def transaction_quantity(self):
        """Gets the transaction_quantity of this TreasureTitlesProductTransaction.  # noqa: E501


        :return: The transaction_quantity of this TreasureTitlesProductTransaction.  # noqa: E501
        :rtype: TreasureTitlesTransactionQuantity
        """
        return self._transaction_quantity

    @transaction_quantity.setter
    def transaction_quantity(self, transaction_quantity):
        """Sets the transaction_quantity of this TreasureTitlesProductTransaction.


        :param transaction_quantity: The transaction_quantity of this TreasureTitlesProductTransaction.  # noqa: E501
        :type: TreasureTitlesTransactionQuantity
        """
        if transaction_quantity is None:
            raise ValueError("Invalid value for `transaction_quantity`, must not be `None`")  # noqa: E501

        self._transaction_quantity = transaction_quantity

    @property
    def transaction_gross_value(self):
        """Gets the transaction_gross_value of this TreasureTitlesProductTransaction.  # noqa: E501


        :return: The transaction_gross_value of this TreasureTitlesProductTransaction.  # noqa: E501
        :rtype: TreasureTitlesTransactionGrossValue
        """
        return self._transaction_gross_value

    @transaction_gross_value.setter
    def transaction_gross_value(self, transaction_gross_value):
        """Sets the transaction_gross_value of this TreasureTitlesProductTransaction.


        :param transaction_gross_value: The transaction_gross_value of this TreasureTitlesProductTransaction.  # noqa: E501
        :type: TreasureTitlesTransactionGrossValue
        """
        if transaction_gross_value is None:
            raise ValueError("Invalid value for `transaction_gross_value`, must not be `None`")  # noqa: E501

        self._transaction_gross_value = transaction_gross_value

    @property
    def income_tax(self):
        """Gets the income_tax of this TreasureTitlesProductTransaction.  # noqa: E501


        :return: The income_tax of this TreasureTitlesProductTransaction.  # noqa: E501
        :rtype: TreasureTitlesProductTransactionIncomeTax
        """
        return self._income_tax

    @income_tax.setter
    def income_tax(self, income_tax):
        """Sets the income_tax of this TreasureTitlesProductTransaction.


        :param income_tax: The income_tax of this TreasureTitlesProductTransaction.  # noqa: E501
        :type: TreasureTitlesProductTransactionIncomeTax
        """

        self._income_tax = income_tax

    @property
    def financial_transaction_tax(self):
        """Gets the financial_transaction_tax of this TreasureTitlesProductTransaction.  # noqa: E501


        :return: The financial_transaction_tax of this TreasureTitlesProductTransaction.  # noqa: E501
        :rtype: TreasureTitlesProductTransactionFinancialTransactionTax
        """
        return self._financial_transaction_tax

    @financial_transaction_tax.setter
    def financial_transaction_tax(self, financial_transaction_tax):
        """Sets the financial_transaction_tax of this TreasureTitlesProductTransaction.


        :param financial_transaction_tax: The financial_transaction_tax of this TreasureTitlesProductTransaction.  # noqa: E501
        :type: TreasureTitlesProductTransactionFinancialTransactionTax
        """

        self._financial_transaction_tax = financial_transaction_tax

    @property
    def transaction_net_value(self):
        """Gets the transaction_net_value of this TreasureTitlesProductTransaction.  # noqa: E501


        :return: The transaction_net_value of this TreasureTitlesProductTransaction.  # noqa: E501
        :rtype: TreasureTitlesTransactionNetValue
        """
        return self._transaction_net_value

    @transaction_net_value.setter
    def transaction_net_value(self, transaction_net_value):
        """Sets the transaction_net_value of this TreasureTitlesProductTransaction.


        :param transaction_net_value: The transaction_net_value of this TreasureTitlesProductTransaction.  # noqa: E501
        :type: TreasureTitlesTransactionNetValue
        """
        if transaction_net_value is None:
            raise ValueError("Invalid value for `transaction_net_value`, must not be `None`")  # noqa: E501

        self._transaction_net_value = transaction_net_value

    @property
    def remuneration_transaction_rate(self):
        """Gets the remuneration_transaction_rate of this TreasureTitlesProductTransaction.  # noqa: E501


        :return: The remuneration_transaction_rate of this TreasureTitlesProductTransaction.  # noqa: E501
        :rtype: TreasureTitlesRemunerationTransactionRate
        """
        return self._remuneration_transaction_rate

    @remuneration_transaction_rate.setter
    def remuneration_transaction_rate(self, remuneration_transaction_rate):
        """Sets the remuneration_transaction_rate of this TreasureTitlesProductTransaction.


        :param remuneration_transaction_rate: The remuneration_transaction_rate of this TreasureTitlesProductTransaction.  # noqa: E501
        :type: TreasureTitlesRemunerationTransactionRate
        """

        self._remuneration_transaction_rate = remuneration_transaction_rate

    @property
    def transaction_id(self):
        """Gets the transaction_id of this TreasureTitlesProductTransaction.  # noqa: E501


        :return: The transaction_id of this TreasureTitlesProductTransaction.  # noqa: E501
        :rtype: TreasureTitlesTransactionId
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this TreasureTitlesProductTransaction.


        :param transaction_id: The transaction_id of this TreasureTitlesProductTransaction.  # noqa: E501
        :type: TreasureTitlesTransactionId
        """
        if transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501

        self._transaction_id = transaction_id

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
        if issubclass(TreasureTitlesProductTransaction, dict):
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
        if not isinstance(other, TreasureTitlesProductTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
