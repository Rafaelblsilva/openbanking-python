# coding: utf-8

"""
    API Funds - Open Finance Brasil

    API de informações de operações de Fundos de Investimento Open Finance Brasil – Fase 4.  API que retorna informações de operações de investimento do tipo Fundos de Investimento mantidas nas instituições transmissoras por seus clientes, incluindo dados como informações do produto, quantidade, saldos em posição do cliente e movimentações financeiras.  Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints.  Devem ser considerados como escopo de exposição todos os fundos de investimento classificados como: Renda Fixa, Ações, Multimercado e Cambial.  Para identificação do produto e posição do cliente, a exposição será de forma consolidada por Fundo de Investimento.  Para movimentações, a exposição se dará pela Ordem do Cliente, por exemplo, uma Ordem de Resgate é compartilhada como uma única movimentação, mesmo que esteja associada a diferentes Certificados (Cautelas).  As instituições podem apresentar cenários distintos no que diz respeito ao sincronismo entre posição `/balances` e movimentação `/transactions` e `/transactions-current` da API:  - Algumas instituições refletem movimentações ainda não convertidas na posição do cliente em seus canais eletrônicos. Isso implica que pode ocorrer compartilhamento de posição atualizada, cujas movimentações relacionadas serão expostas no ecossistema apenas após a conversão das mesmas;  - Outras instituições refletem na posição apenas movimentações convertidas nos seus canais eletrônicos. Isso implica que o compartilhamento da posição em relação às movimentações é feito de forma sincronizada no ecossistema.  Para o identificador do investimento (investmentId) deve ser adotado o seguinte comportamento:  - Após 12 meses sem movimentações e com quantidade de ativos zerada, o resourceId correspondente ao investmentId em questão deve passar ao status UNAVAILABLE (considerando consentimento válido);  - Nas situações em que o cliente compre novamente o ativo após um período de 12 meses sem movimentação e com quantidade de ativos zerada, o mesmo identificador (investmentId) deve ser utilizado. Especificamente para tais produtos, o status do recurso na resources deve passar de UNAVAILABLE para AVAILABLE.   # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponseFundsTransactionsData(object):
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
        'transaction_id': 'str',
        'type': 'EnumFundsTransactionsType',
        'transaction_type': 'EnumFundsTransactionsTransactionType',
        'transaction_type_additional_info': 'str',
        'transaction_conversion_date': 'date',
        'transaction_quota_price': 'ResponseFundsTransactionsDataTransactionQuotaPrice',
        'transaction_quota_quantity': 'str',
        'transaction_value': 'ResponseFundsTransactionsDataTransactionValue',
        'transaction_gross_value': 'ResponseFundsTransactionsDataTransactionGrossValue',
        'income_tax': 'ResponseFundsTransactionsDataIncomeTax',
        'financial_transaction_tax': 'ResponseFundsTransactionsDataFinancialTransactionTax',
        'transaction_exit_fee': 'ResponseFundsTransactionsDataTransactionExitFee',
        'transaction_net_value': 'ResponseFundsTransactionsDataTransactionNetValue'
    }

    attribute_map = {
        'transaction_id': 'transactionId',
        'type': 'type',
        'transaction_type': 'transactionType',
        'transaction_type_additional_info': 'transactionTypeAdditionalInfo',
        'transaction_conversion_date': 'transactionConversionDate',
        'transaction_quota_price': 'transactionQuotaPrice',
        'transaction_quota_quantity': 'transactionQuotaQuantity',
        'transaction_value': 'transactionValue',
        'transaction_gross_value': 'transactionGrossValue',
        'income_tax': 'incomeTax',
        'financial_transaction_tax': 'financialTransactionTax',
        'transaction_exit_fee': 'transactionExitFee',
        'transaction_net_value': 'transactionNetValue'
    }

    def __init__(self, transaction_id=None, type=None, transaction_type=None, transaction_type_additional_info=None, transaction_conversion_date=None, transaction_quota_price=None, transaction_quota_quantity=None, transaction_value=None, transaction_gross_value=None, income_tax=None, financial_transaction_tax=None, transaction_exit_fee=None, transaction_net_value=None):  # noqa: E501
        """ResponseFundsTransactionsData - a model defined in Swagger"""  # noqa: E501
        self._transaction_id = None
        self._type = None
        self._transaction_type = None
        self._transaction_type_additional_info = None
        self._transaction_conversion_date = None
        self._transaction_quota_price = None
        self._transaction_quota_quantity = None
        self._transaction_value = None
        self._transaction_gross_value = None
        self._income_tax = None
        self._financial_transaction_tax = None
        self._transaction_exit_fee = None
        self._transaction_net_value = None
        self.discriminator = None
        self.transaction_id = transaction_id
        self.type = type
        self.transaction_type = transaction_type
        if transaction_type_additional_info is not None:
            self.transaction_type_additional_info = transaction_type_additional_info
        self.transaction_conversion_date = transaction_conversion_date
        self.transaction_quota_price = transaction_quota_price
        self.transaction_quota_quantity = transaction_quota_quantity
        self.transaction_value = transaction_value
        self.transaction_gross_value = transaction_gross_value
        if income_tax is not None:
            self.income_tax = income_tax
        if financial_transaction_tax is not None:
            self.financial_transaction_tax = financial_transaction_tax
        if transaction_exit_fee is not None:
            self.transaction_exit_fee = transaction_exit_fee
        if transaction_net_value is not None:
            self.transaction_net_value = transaction_net_value

    @property
    def transaction_id(self):
        """Gets the transaction_id of this ResponseFundsTransactionsData.  # noqa: E501

        Código ou identificador único prestado pela instituição que mantém a representação individual do movimento na posição do fundo.  # noqa: E501

        :return: The transaction_id of this ResponseFundsTransactionsData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this ResponseFundsTransactionsData.

        Código ou identificador único prestado pela instituição que mantém a representação individual do movimento na posição do fundo.  # noqa: E501

        :param transaction_id: The transaction_id of this ResponseFundsTransactionsData.  # noqa: E501
        :type: str
        """
        if transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501

        self._transaction_id = transaction_id

    @property
    def type(self):
        """Gets the type of this ResponseFundsTransactionsData.  # noqa: E501


        :return: The type of this ResponseFundsTransactionsData.  # noqa: E501
        :rtype: EnumFundsTransactionsType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResponseFundsTransactionsData.


        :param type: The type of this ResponseFundsTransactionsData.  # noqa: E501
        :type: EnumFundsTransactionsType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def transaction_type(self):
        """Gets the transaction_type of this ResponseFundsTransactionsData.  # noqa: E501


        :return: The transaction_type of this ResponseFundsTransactionsData.  # noqa: E501
        :rtype: EnumFundsTransactionsTransactionType
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this ResponseFundsTransactionsData.


        :param transaction_type: The transaction_type of this ResponseFundsTransactionsData.  # noqa: E501
        :type: EnumFundsTransactionsTransactionType
        """
        if transaction_type is None:
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501

        self._transaction_type = transaction_type

    @property
    def transaction_type_additional_info(self):
        """Gets the transaction_type_additional_info of this ResponseFundsTransactionsData.  # noqa: E501

        Informação adicional do tipo do motivo, para preenchimento no caso de movimentações não delimitadas no domínio.  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo 'transactionType' for preenchido com o valor 'OUTROS'.   # noqa: E501

        :return: The transaction_type_additional_info of this ResponseFundsTransactionsData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type_additional_info

    @transaction_type_additional_info.setter
    def transaction_type_additional_info(self, transaction_type_additional_info):
        """Sets the transaction_type_additional_info of this ResponseFundsTransactionsData.

        Informação adicional do tipo do motivo, para preenchimento no caso de movimentações não delimitadas no domínio.  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo 'transactionType' for preenchido com o valor 'OUTROS'.   # noqa: E501

        :param transaction_type_additional_info: The transaction_type_additional_info of this ResponseFundsTransactionsData.  # noqa: E501
        :type: str
        """

        self._transaction_type_additional_info = transaction_type_additional_info

    @property
    def transaction_conversion_date(self):
        """Gets the transaction_conversion_date of this ResponseFundsTransactionsData.  # noqa: E501

        Data da conversão da transação de movimentação do fundo de investimento.  # noqa: E501

        :return: The transaction_conversion_date of this ResponseFundsTransactionsData.  # noqa: E501
        :rtype: date
        """
        return self._transaction_conversion_date

    @transaction_conversion_date.setter
    def transaction_conversion_date(self, transaction_conversion_date):
        """Sets the transaction_conversion_date of this ResponseFundsTransactionsData.

        Data da conversão da transação de movimentação do fundo de investimento.  # noqa: E501

        :param transaction_conversion_date: The transaction_conversion_date of this ResponseFundsTransactionsData.  # noqa: E501
        :type: date
        """
        if transaction_conversion_date is None:
            raise ValueError("Invalid value for `transaction_conversion_date`, must not be `None`")  # noqa: E501

        self._transaction_conversion_date = transaction_conversion_date

    @property
    def transaction_quota_price(self):
        """Gets the transaction_quota_price of this ResponseFundsTransactionsData.  # noqa: E501


        :return: The transaction_quota_price of this ResponseFundsTransactionsData.  # noqa: E501
        :rtype: ResponseFundsTransactionsDataTransactionQuotaPrice
        """
        return self._transaction_quota_price

    @transaction_quota_price.setter
    def transaction_quota_price(self, transaction_quota_price):
        """Sets the transaction_quota_price of this ResponseFundsTransactionsData.


        :param transaction_quota_price: The transaction_quota_price of this ResponseFundsTransactionsData.  # noqa: E501
        :type: ResponseFundsTransactionsDataTransactionQuotaPrice
        """
        if transaction_quota_price is None:
            raise ValueError("Invalid value for `transaction_quota_price`, must not be `None`")  # noqa: E501

        self._transaction_quota_price = transaction_quota_price

    @property
    def transaction_quota_quantity(self):
        """Gets the transaction_quota_quantity of this ResponseFundsTransactionsData.  # noqa: E501

        Número de cotas convertidas na data da movimentação.   # noqa: E501

        :return: The transaction_quota_quantity of this ResponseFundsTransactionsData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_quota_quantity

    @transaction_quota_quantity.setter
    def transaction_quota_quantity(self, transaction_quota_quantity):
        """Sets the transaction_quota_quantity of this ResponseFundsTransactionsData.

        Número de cotas convertidas na data da movimentação.   # noqa: E501

        :param transaction_quota_quantity: The transaction_quota_quantity of this ResponseFundsTransactionsData.  # noqa: E501
        :type: str
        """
        if transaction_quota_quantity is None:
            raise ValueError("Invalid value for `transaction_quota_quantity`, must not be `None`")  # noqa: E501

        self._transaction_quota_quantity = transaction_quota_quantity

    @property
    def transaction_value(self):
        """Gets the transaction_value of this ResponseFundsTransactionsData.  # noqa: E501


        :return: The transaction_value of this ResponseFundsTransactionsData.  # noqa: E501
        :rtype: ResponseFundsTransactionsDataTransactionValue
        """
        return self._transaction_value

    @transaction_value.setter
    def transaction_value(self, transaction_value):
        """Sets the transaction_value of this ResponseFundsTransactionsData.


        :param transaction_value: The transaction_value of this ResponseFundsTransactionsData.  # noqa: E501
        :type: ResponseFundsTransactionsDataTransactionValue
        """
        if transaction_value is None:
            raise ValueError("Invalid value for `transaction_value`, must not be `None`")  # noqa: E501

        self._transaction_value = transaction_value

    @property
    def transaction_gross_value(self):
        """Gets the transaction_gross_value of this ResponseFundsTransactionsData.  # noqa: E501


        :return: The transaction_gross_value of this ResponseFundsTransactionsData.  # noqa: E501
        :rtype: ResponseFundsTransactionsDataTransactionGrossValue
        """
        return self._transaction_gross_value

    @transaction_gross_value.setter
    def transaction_gross_value(self, transaction_gross_value):
        """Sets the transaction_gross_value of this ResponseFundsTransactionsData.


        :param transaction_gross_value: The transaction_gross_value of this ResponseFundsTransactionsData.  # noqa: E501
        :type: ResponseFundsTransactionsDataTransactionGrossValue
        """
        if transaction_gross_value is None:
            raise ValueError("Invalid value for `transaction_gross_value`, must not be `None`")  # noqa: E501

        self._transaction_gross_value = transaction_gross_value

    @property
    def income_tax(self):
        """Gets the income_tax of this ResponseFundsTransactionsData.  # noqa: E501


        :return: The income_tax of this ResponseFundsTransactionsData.  # noqa: E501
        :rtype: ResponseFundsTransactionsDataIncomeTax
        """
        return self._income_tax

    @income_tax.setter
    def income_tax(self, income_tax):
        """Sets the income_tax of this ResponseFundsTransactionsData.


        :param income_tax: The income_tax of this ResponseFundsTransactionsData.  # noqa: E501
        :type: ResponseFundsTransactionsDataIncomeTax
        """

        self._income_tax = income_tax

    @property
    def financial_transaction_tax(self):
        """Gets the financial_transaction_tax of this ResponseFundsTransactionsData.  # noqa: E501


        :return: The financial_transaction_tax of this ResponseFundsTransactionsData.  # noqa: E501
        :rtype: ResponseFundsTransactionsDataFinancialTransactionTax
        """
        return self._financial_transaction_tax

    @financial_transaction_tax.setter
    def financial_transaction_tax(self, financial_transaction_tax):
        """Sets the financial_transaction_tax of this ResponseFundsTransactionsData.


        :param financial_transaction_tax: The financial_transaction_tax of this ResponseFundsTransactionsData.  # noqa: E501
        :type: ResponseFundsTransactionsDataFinancialTransactionTax
        """

        self._financial_transaction_tax = financial_transaction_tax

    @property
    def transaction_exit_fee(self):
        """Gets the transaction_exit_fee of this ResponseFundsTransactionsData.  # noqa: E501


        :return: The transaction_exit_fee of this ResponseFundsTransactionsData.  # noqa: E501
        :rtype: ResponseFundsTransactionsDataTransactionExitFee
        """
        return self._transaction_exit_fee

    @transaction_exit_fee.setter
    def transaction_exit_fee(self, transaction_exit_fee):
        """Sets the transaction_exit_fee of this ResponseFundsTransactionsData.


        :param transaction_exit_fee: The transaction_exit_fee of this ResponseFundsTransactionsData.  # noqa: E501
        :type: ResponseFundsTransactionsDataTransactionExitFee
        """

        self._transaction_exit_fee = transaction_exit_fee

    @property
    def transaction_net_value(self):
        """Gets the transaction_net_value of this ResponseFundsTransactionsData.  # noqa: E501


        :return: The transaction_net_value of this ResponseFundsTransactionsData.  # noqa: E501
        :rtype: ResponseFundsTransactionsDataTransactionNetValue
        """
        return self._transaction_net_value

    @transaction_net_value.setter
    def transaction_net_value(self, transaction_net_value):
        """Sets the transaction_net_value of this ResponseFundsTransactionsData.


        :param transaction_net_value: The transaction_net_value of this ResponseFundsTransactionsData.  # noqa: E501
        :type: ResponseFundsTransactionsDataTransactionNetValue
        """

        self._transaction_net_value = transaction_net_value

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
        if issubclass(ResponseFundsTransactionsData, dict):
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
        if not isinstance(other, ResponseFundsTransactionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
