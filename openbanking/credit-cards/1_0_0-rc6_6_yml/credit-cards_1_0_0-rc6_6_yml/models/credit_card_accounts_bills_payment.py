# coding: utf-8

"""
    API Credit-cards-accounts - Open Banking Brasil

    API de contas de pagamento pós-pagas do Open Banking Brasil – Fase 2. API que retorna informações de contas de pagamento pós-paga mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, produto, bandeira, limites de crédito, informações sobre transações de pagamento efetuadas e faturas.  Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.   # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.    ## Permissions necessárias para a API Credit-cards-accounts  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/accounts`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### `/accounts/{creditCardAccountId}`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### `/accounts/{creditCardAccountId}/bills`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_READ** ### `/accounts/{creditCardAccountId}/{billId}/transactions`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_TRANSACTIONS_READ** ### `/accounts/{creditCardAccountId}/limits`           - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_LIMITS_READ** ### `/accounts/{creditCardAccountId}/transactions`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ**   # noqa: E501

    OpenAPI spec version: 1.0.0-rc6.6
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreditCardAccountsBillsPayment(object):
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
        'value_type': 'EnumCreditCardAccountsBillingValueType',
        'payment_date': 'date',
        'payment_mode': 'EnumCreditCardAccountsPaymentMode',
        'amount': 'float',
        'currency': 'str'
    }

    attribute_map = {
        'value_type': 'valueType',
        'payment_date': 'paymentDate',
        'payment_mode': 'paymentMode',
        'amount': 'amount',
        'currency': 'currency'
    }

    def __init__(self, value_type=None, payment_date=None, payment_mode=None, amount=None, currency=None):  # noqa: E501
        """CreditCardAccountsBillsPayment - a model defined in Swagger"""  # noqa: E501
        self._value_type = None
        self._payment_date = None
        self._payment_mode = None
        self._amount = None
        self._currency = None
        self.discriminator = None
        self.value_type = value_type
        self.payment_date = payment_date
        self.payment_mode = payment_mode
        self.amount = amount
        self.currency = currency

    @property
    def value_type(self):
        """Gets the value_type of this CreditCardAccountsBillsPayment.  # noqa: E501


        :return: The value_type of this CreditCardAccountsBillsPayment.  # noqa: E501
        :rtype: EnumCreditCardAccountsBillingValueType
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this CreditCardAccountsBillsPayment.


        :param value_type: The value_type of this CreditCardAccountsBillsPayment.  # noqa: E501
        :type: EnumCreditCardAccountsBillingValueType
        """
        if value_type is None:
            raise ValueError("Invalid value for `value_type`, must not be `None`")  # noqa: E501

        self._value_type = value_type

    @property
    def payment_date(self):
        """Gets the payment_date of this CreditCardAccountsBillsPayment.  # noqa: E501

        Data efetiva de quando o Pagamento da fatura foi realizado  # noqa: E501

        :return: The payment_date of this CreditCardAccountsBillsPayment.  # noqa: E501
        :rtype: date
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this CreditCardAccountsBillsPayment.

        Data efetiva de quando o Pagamento da fatura foi realizado  # noqa: E501

        :param payment_date: The payment_date of this CreditCardAccountsBillsPayment.  # noqa: E501
        :type: date
        """
        if payment_date is None:
            raise ValueError("Invalid value for `payment_date`, must not be `None`")  # noqa: E501

        self._payment_date = payment_date

    @property
    def payment_mode(self):
        """Gets the payment_mode of this CreditCardAccountsBillsPayment.  # noqa: E501


        :return: The payment_mode of this CreditCardAccountsBillsPayment.  # noqa: E501
        :rtype: EnumCreditCardAccountsPaymentMode
        """
        return self._payment_mode

    @payment_mode.setter
    def payment_mode(self, payment_mode):
        """Sets the payment_mode of this CreditCardAccountsBillsPayment.


        :param payment_mode: The payment_mode of this CreditCardAccountsBillsPayment.  # noqa: E501
        :type: EnumCreditCardAccountsPaymentMode
        """
        if payment_mode is None:
            raise ValueError("Invalid value for `payment_mode`, must not be `None`")  # noqa: E501

        self._payment_mode = payment_mode

    @property
    def amount(self):
        """Gets the amount of this CreditCardAccountsBillsPayment.  # noqa: E501

        Valor pagamento segundo o valueType.  Expresso em valor monetário com 4 casas decimais  # noqa: E501

        :return: The amount of this CreditCardAccountsBillsPayment.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreditCardAccountsBillsPayment.

        Valor pagamento segundo o valueType.  Expresso em valor monetário com 4 casas decimais  # noqa: E501

        :param amount: The amount of this CreditCardAccountsBillsPayment.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this CreditCardAccountsBillsPayment.  # noqa: E501

        Moeda referente ao valor de pagamento da fatura, segundo modelo ISO-4217. p.ex. 'BRL' Todos os valores informados estão representados com a moeda vigente do Brasil   # noqa: E501

        :return: The currency of this CreditCardAccountsBillsPayment.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CreditCardAccountsBillsPayment.

        Moeda referente ao valor de pagamento da fatura, segundo modelo ISO-4217. p.ex. 'BRL' Todos os valores informados estão representados com a moeda vigente do Brasil   # noqa: E501

        :param currency: The currency of this CreditCardAccountsBillsPayment.  # noqa: E501
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
        if issubclass(CreditCardAccountsBillsPayment, dict):
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
        if not isinstance(other, CreditCardAccountsBillsPayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
