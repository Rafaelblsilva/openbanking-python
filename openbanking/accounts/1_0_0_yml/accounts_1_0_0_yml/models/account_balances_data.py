# coding: utf-8

"""
    API Accounts - Open Banking Brasil

    API de contas de depósito à vista, contas de poupança e contas pré-pagas do Open Banking Brasil – Fase 2. API que retorna informações de contas de depósito à vista, contas de poupança e contas de pagamento pré-pagas mantidas nas instituições transmissoras por seus clientes, incluindo dados de identificação da conta, saldos, limites e transações.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Accounts  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/accounts`   - permissions:     - GET: **ACCOUNTS_READ** ### `/accounts/{accountId}`   - permissions:     - GET: **ACCOUNTS_READ** ### `/accounts/{accountId}/balances`   - permissions:     - GET: **ACCOUNTS_BALANCES_READ** ### `/accounts/{accountId}/transactions`   - permissions:     - GET: **ACCOUNTS_TRANSACTIONS_READ** ### `/accounts/{accountId}/overdraft-limits`   - permissions:     - GET: **ACCOUNTS_OVERDRAFT_LIMITS_READ**   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AccountBalancesData(object):
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
        'available_amount': 'float',
        'available_amount_currency': 'str',
        'blocked_amount': 'float',
        'blocked_amount_currency': 'str',
        'automatically_invested_amount': 'float',
        'automatically_invested_amount_currency': 'str'
    }

    attribute_map = {
        'available_amount': 'availableAmount',
        'available_amount_currency': 'availableAmountCurrency',
        'blocked_amount': 'blockedAmount',
        'blocked_amount_currency': 'blockedAmountCurrency',
        'automatically_invested_amount': 'automaticallyInvestedAmount',
        'automatically_invested_amount_currency': 'automaticallyInvestedAmountCurrency'
    }

    def __init__(self, available_amount=None, available_amount_currency=None, blocked_amount=None, blocked_amount_currency=None, automatically_invested_amount=None, automatically_invested_amount_currency=None):  # noqa: E501
        """AccountBalancesData - a model defined in Swagger"""  # noqa: E501
        self._available_amount = None
        self._available_amount_currency = None
        self._blocked_amount = None
        self._blocked_amount_currency = None
        self._automatically_invested_amount = None
        self._automatically_invested_amount_currency = None
        self.discriminator = None
        self.available_amount = available_amount
        self.available_amount_currency = available_amount_currency
        self.blocked_amount = blocked_amount
        self.blocked_amount_currency = blocked_amount_currency
        self.automatically_invested_amount = automatically_invested_amount
        self.automatically_invested_amount_currency = automatically_invested_amount_currency

    @property
    def available_amount(self):
        """Gets the available_amount of this AccountBalancesData.  # noqa: E501

        Saldo disponível para utilização imediata. No caso de conta de depósito a vista, sem considerar cheque especial e investimentos atrelados a conta. Admite saldo negativo. Expresso em valor monetário com 4 casas decimais.  # noqa: E501

        :return: The available_amount of this AccountBalancesData.  # noqa: E501
        :rtype: float
        """
        return self._available_amount

    @available_amount.setter
    def available_amount(self, available_amount):
        """Sets the available_amount of this AccountBalancesData.

        Saldo disponível para utilização imediata. No caso de conta de depósito a vista, sem considerar cheque especial e investimentos atrelados a conta. Admite saldo negativo. Expresso em valor monetário com 4 casas decimais.  # noqa: E501

        :param available_amount: The available_amount of this AccountBalancesData.  # noqa: E501
        :type: float
        """
        if available_amount is None:
            raise ValueError("Invalid value for `available_amount`, must not be `None`")  # noqa: E501

        self._available_amount = available_amount

    @property
    def available_amount_currency(self):
        """Gets the available_amount_currency of this AccountBalancesData.  # noqa: E501

        Moeda referente ao valor do saldo disponível, segundo modelo ISO-4217. p.ex. 'BRL'. Pode ser preenchido com “NA” caso a instituição não possua a informação.  # noqa: E501

        :return: The available_amount_currency of this AccountBalancesData.  # noqa: E501
        :rtype: str
        """
        return self._available_amount_currency

    @available_amount_currency.setter
    def available_amount_currency(self, available_amount_currency):
        """Sets the available_amount_currency of this AccountBalancesData.

        Moeda referente ao valor do saldo disponível, segundo modelo ISO-4217. p.ex. 'BRL'. Pode ser preenchido com “NA” caso a instituição não possua a informação.  # noqa: E501

        :param available_amount_currency: The available_amount_currency of this AccountBalancesData.  # noqa: E501
        :type: str
        """
        if available_amount_currency is None:
            raise ValueError("Invalid value for `available_amount_currency`, must not be `None`")  # noqa: E501

        self._available_amount_currency = available_amount_currency

    @property
    def blocked_amount(self):
        """Gets the blocked_amount of this AccountBalancesData.  # noqa: E501

        Saldo bloqueado, não disponível para utilização imediata, por motivo de bloqueio apresentado para o cliente nos canais eletrônicos Expresso em valor monetário com 4 casas decimais.  # noqa: E501

        :return: The blocked_amount of this AccountBalancesData.  # noqa: E501
        :rtype: float
        """
        return self._blocked_amount

    @blocked_amount.setter
    def blocked_amount(self, blocked_amount):
        """Sets the blocked_amount of this AccountBalancesData.

        Saldo bloqueado, não disponível para utilização imediata, por motivo de bloqueio apresentado para o cliente nos canais eletrônicos Expresso em valor monetário com 4 casas decimais.  # noqa: E501

        :param blocked_amount: The blocked_amount of this AccountBalancesData.  # noqa: E501
        :type: float
        """
        if blocked_amount is None:
            raise ValueError("Invalid value for `blocked_amount`, must not be `None`")  # noqa: E501

        self._blocked_amount = blocked_amount

    @property
    def blocked_amount_currency(self):
        """Gets the blocked_amount_currency of this AccountBalancesData.  # noqa: E501

        Moeda referente ao valor do saldo bloqueado, segundo modelo ISO-4217. p.ex. 'BRL'. Pode ser preenchido com “NA” caso a instituição não possua a informação.  # noqa: E501

        :return: The blocked_amount_currency of this AccountBalancesData.  # noqa: E501
        :rtype: str
        """
        return self._blocked_amount_currency

    @blocked_amount_currency.setter
    def blocked_amount_currency(self, blocked_amount_currency):
        """Sets the blocked_amount_currency of this AccountBalancesData.

        Moeda referente ao valor do saldo bloqueado, segundo modelo ISO-4217. p.ex. 'BRL'. Pode ser preenchido com “NA” caso a instituição não possua a informação.  # noqa: E501

        :param blocked_amount_currency: The blocked_amount_currency of this AccountBalancesData.  # noqa: E501
        :type: str
        """
        if blocked_amount_currency is None:
            raise ValueError("Invalid value for `blocked_amount_currency`, must not be `None`")  # noqa: E501

        self._blocked_amount_currency = blocked_amount_currency

    @property
    def automatically_invested_amount(self):
        """Gets the automatically_invested_amount of this AccountBalancesData.  # noqa: E501

        Saldo disponível com aplicação automática - corresponde a soma do saldo disponível acrescido do valor obtido a partir da aplicação automática Expresso em valor monetário com 4 casas decimais.  # noqa: E501

        :return: The automatically_invested_amount of this AccountBalancesData.  # noqa: E501
        :rtype: float
        """
        return self._automatically_invested_amount

    @automatically_invested_amount.setter
    def automatically_invested_amount(self, automatically_invested_amount):
        """Sets the automatically_invested_amount of this AccountBalancesData.

        Saldo disponível com aplicação automática - corresponde a soma do saldo disponível acrescido do valor obtido a partir da aplicação automática Expresso em valor monetário com 4 casas decimais.  # noqa: E501

        :param automatically_invested_amount: The automatically_invested_amount of this AccountBalancesData.  # noqa: E501
        :type: float
        """
        if automatically_invested_amount is None:
            raise ValueError("Invalid value for `automatically_invested_amount`, must not be `None`")  # noqa: E501

        self._automatically_invested_amount = automatically_invested_amount

    @property
    def automatically_invested_amount_currency(self):
        """Gets the automatically_invested_amount_currency of this AccountBalancesData.  # noqa: E501

        Moeda referente ao valor do saldo disponível com aplicação automática, segundo modelo ISO-4217. p.ex. 'BRL'. Pode ser preenchido com “NA” caso a instituição não possua a informação.  # noqa: E501

        :return: The automatically_invested_amount_currency of this AccountBalancesData.  # noqa: E501
        :rtype: str
        """
        return self._automatically_invested_amount_currency

    @automatically_invested_amount_currency.setter
    def automatically_invested_amount_currency(self, automatically_invested_amount_currency):
        """Sets the automatically_invested_amount_currency of this AccountBalancesData.

        Moeda referente ao valor do saldo disponível com aplicação automática, segundo modelo ISO-4217. p.ex. 'BRL'. Pode ser preenchido com “NA” caso a instituição não possua a informação.  # noqa: E501

        :param automatically_invested_amount_currency: The automatically_invested_amount_currency of this AccountBalancesData.  # noqa: E501
        :type: str
        """
        if automatically_invested_amount_currency is None:
            raise ValueError("Invalid value for `automatically_invested_amount_currency`, must not be `None`")  # noqa: E501

        self._automatically_invested_amount_currency = automatically_invested_amount_currency

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
        if issubclass(AccountBalancesData, dict):
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
        if not isinstance(other, AccountBalancesData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
