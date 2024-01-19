# coding: utf-8

"""
    API Credit Fixed Incomes - Open Finance Brasil

    API de informações de operações de Renda Fixa Crédito do Open Finance Brasil – Fase 4. API que retorna informações de operações de investimento do tipo Renda Fixa Crédito (Debêntures, CRI/CRA) mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação do produto, rentabilidade, quantidade, prazos, saldos em posição do cliente e movimentações financeiras. Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints. A exposição se dará por cada operação de renda fixa contratada pelo cliente.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponseCreditFixedIncomesBalancesData(object):
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
        'reference_date_time': 'ReferenceDateTime',
        'updated_unit_price': 'UpdatedUnitPrice',
        'quantity': 'str',
        'gross_amount': 'GrossAmount',
        'net_amount': 'NetAmount',
        'income_tax': 'IncomeTax',
        'financial_transaction_tax': 'FinancialTransactionTax',
        'blocked_balance': 'BlockedBalance',
        'purchase_unit_price': 'PurchaseUnitPrice',
        'pre_fixed_rate': 'str',
        'post_fixed_indexer_percentage': 'PostFixedIndexerPercentage',
        'fine': 'Fine',
        'late_payment': 'LatePayment'
    }

    attribute_map = {
        'reference_date_time': 'referenceDateTime',
        'updated_unit_price': 'updatedUnitPrice',
        'quantity': 'quantity',
        'gross_amount': 'grossAmount',
        'net_amount': 'netAmount',
        'income_tax': 'incomeTax',
        'financial_transaction_tax': 'financialTransactionTax',
        'blocked_balance': 'blockedBalance',
        'purchase_unit_price': 'purchaseUnitPrice',
        'pre_fixed_rate': 'preFixedRate',
        'post_fixed_indexer_percentage': 'postFixedIndexerPercentage',
        'fine': 'fine',
        'late_payment': 'latePayment'
    }

    def __init__(self, reference_date_time=None, updated_unit_price=None, quantity=None, gross_amount=None, net_amount=None, income_tax=None, financial_transaction_tax=None, blocked_balance=None, purchase_unit_price=None, pre_fixed_rate=None, post_fixed_indexer_percentage=None, fine=None, late_payment=None):  # noqa: E501
        """ResponseCreditFixedIncomesBalancesData - a model defined in Swagger"""  # noqa: E501
        self._reference_date_time = None
        self._updated_unit_price = None
        self._quantity = None
        self._gross_amount = None
        self._net_amount = None
        self._income_tax = None
        self._financial_transaction_tax = None
        self._blocked_balance = None
        self._purchase_unit_price = None
        self._pre_fixed_rate = None
        self._post_fixed_indexer_percentage = None
        self._fine = None
        self._late_payment = None
        self.discriminator = None
        self.reference_date_time = reference_date_time
        self.updated_unit_price = updated_unit_price
        self.quantity = quantity
        self.gross_amount = gross_amount
        self.net_amount = net_amount
        self.income_tax = income_tax
        self.financial_transaction_tax = financial_transaction_tax
        self.blocked_balance = blocked_balance
        self.purchase_unit_price = purchase_unit_price
        if pre_fixed_rate is not None:
            self.pre_fixed_rate = pre_fixed_rate
        if post_fixed_indexer_percentage is not None:
            self.post_fixed_indexer_percentage = post_fixed_indexer_percentage
        if fine is not None:
            self.fine = fine
        if late_payment is not None:
            self.late_payment = late_payment

    @property
    def reference_date_time(self):
        """Gets the reference_date_time of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501


        :return: The reference_date_time of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :rtype: ReferenceDateTime
        """
        return self._reference_date_time

    @reference_date_time.setter
    def reference_date_time(self, reference_date_time):
        """Sets the reference_date_time of this ResponseCreditFixedIncomesBalancesData.


        :param reference_date_time: The reference_date_time of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :type: ReferenceDateTime
        """
        if reference_date_time is None:
            raise ValueError("Invalid value for `reference_date_time`, must not be `None`")  # noqa: E501

        self._reference_date_time = reference_date_time

    @property
    def updated_unit_price(self):
        """Gets the updated_unit_price of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501


        :return: The updated_unit_price of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :rtype: UpdatedUnitPrice
        """
        return self._updated_unit_price

    @updated_unit_price.setter
    def updated_unit_price(self, updated_unit_price):
        """Sets the updated_unit_price of this ResponseCreditFixedIncomesBalancesData.


        :param updated_unit_price: The updated_unit_price of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :type: UpdatedUnitPrice
        """
        if updated_unit_price is None:
            raise ValueError("Invalid value for `updated_unit_price`, must not be `None`")  # noqa: E501

        self._updated_unit_price = updated_unit_price

    @property
    def quantity(self):
        """Gets the quantity of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501

        quantidade de títulos detidos na data da posição do cliente  # noqa: E501

        :return: The quantity of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ResponseCreditFixedIncomesBalancesData.

        quantidade de títulos detidos na data da posição do cliente  # noqa: E501

        :param quantity: The quantity of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :type: str
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def gross_amount(self):
        """Gets the gross_amount of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501


        :return: The gross_amount of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :rtype: GrossAmount
        """
        return self._gross_amount

    @gross_amount.setter
    def gross_amount(self, gross_amount):
        """Sets the gross_amount of this ResponseCreditFixedIncomesBalancesData.


        :param gross_amount: The gross_amount of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :type: GrossAmount
        """
        if gross_amount is None:
            raise ValueError("Invalid value for `gross_amount`, must not be `None`")  # noqa: E501

        self._gross_amount = gross_amount

    @property
    def net_amount(self):
        """Gets the net_amount of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501


        :return: The net_amount of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :rtype: NetAmount
        """
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        """Sets the net_amount of this ResponseCreditFixedIncomesBalancesData.


        :param net_amount: The net_amount of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :type: NetAmount
        """
        if net_amount is None:
            raise ValueError("Invalid value for `net_amount`, must not be `None`")  # noqa: E501

        self._net_amount = net_amount

    @property
    def income_tax(self):
        """Gets the income_tax of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501


        :return: The income_tax of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :rtype: IncomeTax
        """
        return self._income_tax

    @income_tax.setter
    def income_tax(self, income_tax):
        """Sets the income_tax of this ResponseCreditFixedIncomesBalancesData.


        :param income_tax: The income_tax of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :type: IncomeTax
        """
        if income_tax is None:
            raise ValueError("Invalid value for `income_tax`, must not be `None`")  # noqa: E501

        self._income_tax = income_tax

    @property
    def financial_transaction_tax(self):
        """Gets the financial_transaction_tax of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501


        :return: The financial_transaction_tax of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :rtype: FinancialTransactionTax
        """
        return self._financial_transaction_tax

    @financial_transaction_tax.setter
    def financial_transaction_tax(self, financial_transaction_tax):
        """Sets the financial_transaction_tax of this ResponseCreditFixedIncomesBalancesData.


        :param financial_transaction_tax: The financial_transaction_tax of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :type: FinancialTransactionTax
        """
        if financial_transaction_tax is None:
            raise ValueError("Invalid value for `financial_transaction_tax`, must not be `None`")  # noqa: E501

        self._financial_transaction_tax = financial_transaction_tax

    @property
    def blocked_balance(self):
        """Gets the blocked_balance of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501


        :return: The blocked_balance of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :rtype: BlockedBalance
        """
        return self._blocked_balance

    @blocked_balance.setter
    def blocked_balance(self, blocked_balance):
        """Sets the blocked_balance of this ResponseCreditFixedIncomesBalancesData.


        :param blocked_balance: The blocked_balance of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :type: BlockedBalance
        """
        if blocked_balance is None:
            raise ValueError("Invalid value for `blocked_balance`, must not be `None`")  # noqa: E501

        self._blocked_balance = blocked_balance

    @property
    def purchase_unit_price(self):
        """Gets the purchase_unit_price of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501


        :return: The purchase_unit_price of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :rtype: PurchaseUnitPrice
        """
        return self._purchase_unit_price

    @purchase_unit_price.setter
    def purchase_unit_price(self, purchase_unit_price):
        """Sets the purchase_unit_price of this ResponseCreditFixedIncomesBalancesData.


        :param purchase_unit_price: The purchase_unit_price of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :type: PurchaseUnitPrice
        """
        if purchase_unit_price is None:
            raise ValueError("Invalid value for `purchase_unit_price`, must not be `None`")  # noqa: E501

        self._purchase_unit_price = purchase_unit_price

    @property
    def pre_fixed_rate(self):
        """Gets the pre_fixed_rate of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501

        Taxa de remuneração acordada com o cliente na contratação.  Em casos de produtos progressivos, considerar taxa vigente.  É esperado que o preenchimento deste campo pelas participantes seja enviado de acordo com o campo preFixedRate do endpoint /investment/{investmentId}.   # noqa: E501

        :return: The pre_fixed_rate of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :rtype: str
        """
        return self._pre_fixed_rate

    @pre_fixed_rate.setter
    def pre_fixed_rate(self, pre_fixed_rate):
        """Sets the pre_fixed_rate of this ResponseCreditFixedIncomesBalancesData.

        Taxa de remuneração acordada com o cliente na contratação.  Em casos de produtos progressivos, considerar taxa vigente.  É esperado que o preenchimento deste campo pelas participantes seja enviado de acordo com o campo preFixedRate do endpoint /investment/{investmentId}.   # noqa: E501

        :param pre_fixed_rate: The pre_fixed_rate of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :type: str
        """

        self._pre_fixed_rate = pre_fixed_rate

    @property
    def post_fixed_indexer_percentage(self):
        """Gets the post_fixed_indexer_percentage of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501


        :return: The post_fixed_indexer_percentage of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :rtype: PostFixedIndexerPercentage
        """
        return self._post_fixed_indexer_percentage

    @post_fixed_indexer_percentage.setter
    def post_fixed_indexer_percentage(self, post_fixed_indexer_percentage):
        """Sets the post_fixed_indexer_percentage of this ResponseCreditFixedIncomesBalancesData.


        :param post_fixed_indexer_percentage: The post_fixed_indexer_percentage of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :type: PostFixedIndexerPercentage
        """

        self._post_fixed_indexer_percentage = post_fixed_indexer_percentage

    @property
    def fine(self):
        """Gets the fine of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501


        :return: The fine of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :rtype: Fine
        """
        return self._fine

    @fine.setter
    def fine(self, fine):
        """Sets the fine of this ResponseCreditFixedIncomesBalancesData.


        :param fine: The fine of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :type: Fine
        """

        self._fine = fine

    @property
    def late_payment(self):
        """Gets the late_payment of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501


        :return: The late_payment of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :rtype: LatePayment
        """
        return self._late_payment

    @late_payment.setter
    def late_payment(self, late_payment):
        """Sets the late_payment of this ResponseCreditFixedIncomesBalancesData.


        :param late_payment: The late_payment of this ResponseCreditFixedIncomesBalancesData.  # noqa: E501
        :type: LatePayment
        """

        self._late_payment = late_payment

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
        if issubclass(ResponseCreditFixedIncomesBalancesData, dict):
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
        if not isinstance(other, ResponseCreditFixedIncomesBalancesData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
