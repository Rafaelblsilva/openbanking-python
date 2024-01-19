# coding: utf-8

"""
    API Credit-cards-accounts - Open Banking Brasil

    API de contas de pagamento pós-pagas do Open Banking Brasil – Fase 2. API que retorna informações de contas de pagamento pós-paga mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, produto, bandeira, limites de crédito, informações sobre transações de pagamento efetuadas e faturas.  Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Credit-cards-accounts  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/accounts`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### `/accounts/{creditCardAccountId}`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### `/accounts/{creditCardAccountId}/bills`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_READ** ### `/accounts/{creditCardAccountId}/{billId}/transactions`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_TRANSACTIONS_READ** ### `/accounts/{creditCardAccountId}/limits`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_LIMITS_READ** ### `/accounts/{creditCardAccountId}/transactions`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ**   # noqa: E501

    OpenAPI spec version: 1.0.4
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreditCardAccountsBillsFinanceCharge(object):
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
        'type': 'EnumCreditCardAccountsFinanceChargeType',
        'additional_info': 'str',
        'amount': 'float',
        'currency': 'str'
    }

    attribute_map = {
        'type': 'type',
        'additional_info': 'additionalInfo',
        'amount': 'amount',
        'currency': 'currency'
    }

    def __init__(self, type=None, additional_info=None, amount=None, currency=None):  # noqa: E501
        """CreditCardAccountsBillsFinanceCharge - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._additional_info = None
        self._amount = None
        self._currency = None
        self.discriminator = None
        self.type = type
        if additional_info is not None:
            self.additional_info = additional_info
        self.amount = amount
        self.currency = currency

    @property
    def type(self):
        """Gets the type of this CreditCardAccountsBillsFinanceCharge.  # noqa: E501


        :return: The type of this CreditCardAccountsBillsFinanceCharge.  # noqa: E501
        :rtype: EnumCreditCardAccountsFinanceChargeType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreditCardAccountsBillsFinanceCharge.


        :param type: The type of this CreditCardAccountsBillsFinanceCharge.  # noqa: E501
        :type: EnumCreditCardAccountsFinanceChargeType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def additional_info(self):
        """Gets the additional_info of this CreditCardAccountsBillsFinanceCharge.  # noqa: E501

        Campo livre, de preenchimento obrigatório se selecionado tipo de encargo 'OUTROS'  # noqa: E501

        :return: The additional_info of this CreditCardAccountsBillsFinanceCharge.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this CreditCardAccountsBillsFinanceCharge.

        Campo livre, de preenchimento obrigatório se selecionado tipo de encargo 'OUTROS'  # noqa: E501

        :param additional_info: The additional_info of this CreditCardAccountsBillsFinanceCharge.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def amount(self):
        """Gets the amount of this CreditCardAccountsBillsFinanceCharge.  # noqa: E501

        Valor cobrado pelo encargo. Expresso em valor monetário com 4 casas decimais  # noqa: E501

        :return: The amount of this CreditCardAccountsBillsFinanceCharge.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreditCardAccountsBillsFinanceCharge.

        Valor cobrado pelo encargo. Expresso em valor monetário com 4 casas decimais  # noqa: E501

        :param amount: The amount of this CreditCardAccountsBillsFinanceCharge.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this CreditCardAccountsBillsFinanceCharge.  # noqa: E501

        Moeda referente ao valor cobrado pelo encargo, segundo modelo ISO-4217. p.ex. 'BRL'  Todos os saldos informados estão representados com a moeda vigente do Brasil.   # noqa: E501

        :return: The currency of this CreditCardAccountsBillsFinanceCharge.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CreditCardAccountsBillsFinanceCharge.

        Moeda referente ao valor cobrado pelo encargo, segundo modelo ISO-4217. p.ex. 'BRL'  Todos os saldos informados estão representados com a moeda vigente do Brasil.   # noqa: E501

        :param currency: The currency of this CreditCardAccountsBillsFinanceCharge.  # noqa: E501
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
        if issubclass(CreditCardAccountsBillsFinanceCharge, dict):
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
        if not isinstance(other, CreditCardAccountsBillsFinanceCharge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
