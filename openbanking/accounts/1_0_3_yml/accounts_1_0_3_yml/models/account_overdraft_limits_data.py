# coding: utf-8

"""
    API Accounts - Open Banking Brasil

    API de contas de depósito à vista, contas de poupança e contas pré-pagas do Open Banking Brasil – Fase 2. API que retorna informações de contas de depósito à vista, contas de poupança e contas de pagamento pré-pagas mantidas nas instituições transmissoras por seus clientes, incluindo dados de identificação da conta, saldos, limites e transações.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Accounts  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/accounts`   - permissions:     - GET: **ACCOUNTS_READ** ### `/accounts/{accountId}`   - permissions:     - GET: **ACCOUNTS_READ** ### `/accounts/{accountId}/balances`   - permissions:     - GET: **ACCOUNTS_BALANCES_READ** ### `/accounts/{accountId}/transactions`   - permissions:     - GET: **ACCOUNTS_TRANSACTIONS_READ** ### `/accounts/{accountId}/overdraft-limits`   - permissions:     - GET: **ACCOUNTS_OVERDRAFT_LIMITS_READ**   # noqa: E501

    OpenAPI spec version: 1.0.3
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AccountOverdraftLimitsData(object):
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
        'overdraft_contracted_limit': 'float',
        'overdraft_contracted_limit_currency': 'str',
        'overdraft_used_limit': 'float',
        'overdraft_used_limit_currency': 'str',
        'unarranged_overdraft_amount': 'float',
        'unarranged_overdraft_amount_currency': 'str'
    }

    attribute_map = {
        'overdraft_contracted_limit': 'overdraftContractedLimit',
        'overdraft_contracted_limit_currency': 'overdraftContractedLimitCurrency',
        'overdraft_used_limit': 'overdraftUsedLimit',
        'overdraft_used_limit_currency': 'overdraftUsedLimitCurrency',
        'unarranged_overdraft_amount': 'unarrangedOverdraftAmount',
        'unarranged_overdraft_amount_currency': 'unarrangedOverdraftAmountCurrency'
    }

    def __init__(self, overdraft_contracted_limit=None, overdraft_contracted_limit_currency=None, overdraft_used_limit=None, overdraft_used_limit_currency=None, unarranged_overdraft_amount=None, unarranged_overdraft_amount_currency=None):  # noqa: E501
        """AccountOverdraftLimitsData - a model defined in Swagger"""  # noqa: E501
        self._overdraft_contracted_limit = None
        self._overdraft_contracted_limit_currency = None
        self._overdraft_used_limit = None
        self._overdraft_used_limit_currency = None
        self._unarranged_overdraft_amount = None
        self._unarranged_overdraft_amount_currency = None
        self.discriminator = None
        self.overdraft_contracted_limit = overdraft_contracted_limit
        self.overdraft_contracted_limit_currency = overdraft_contracted_limit_currency
        self.overdraft_used_limit = overdraft_used_limit
        self.overdraft_used_limit_currency = overdraft_used_limit_currency
        self.unarranged_overdraft_amount = unarranged_overdraft_amount
        self.unarranged_overdraft_amount_currency = unarranged_overdraft_amount_currency

    @property
    def overdraft_contracted_limit(self):
        """Gets the overdraft_contracted_limit of this AccountOverdraftLimitsData.  # noqa: E501

        Valor do limite contratado do cheque especial.  # noqa: E501

        :return: The overdraft_contracted_limit of this AccountOverdraftLimitsData.  # noqa: E501
        :rtype: float
        """
        return self._overdraft_contracted_limit

    @overdraft_contracted_limit.setter
    def overdraft_contracted_limit(self, overdraft_contracted_limit):
        """Sets the overdraft_contracted_limit of this AccountOverdraftLimitsData.

        Valor do limite contratado do cheque especial.  # noqa: E501

        :param overdraft_contracted_limit: The overdraft_contracted_limit of this AccountOverdraftLimitsData.  # noqa: E501
        :type: float
        """
        if overdraft_contracted_limit is None:
            raise ValueError("Invalid value for `overdraft_contracted_limit`, must not be `None`")  # noqa: E501

        self._overdraft_contracted_limit = overdraft_contracted_limit

    @property
    def overdraft_contracted_limit_currency(self):
        """Gets the overdraft_contracted_limit_currency of this AccountOverdraftLimitsData.  # noqa: E501

        Moeda referente ao valor do limite contratado do cheque especial, segundo modelo ISO-4217. p.ex. 'BRL'. Pode ser preenchido com “NA” caso a instituição não possua a informação.  # noqa: E501

        :return: The overdraft_contracted_limit_currency of this AccountOverdraftLimitsData.  # noqa: E501
        :rtype: str
        """
        return self._overdraft_contracted_limit_currency

    @overdraft_contracted_limit_currency.setter
    def overdraft_contracted_limit_currency(self, overdraft_contracted_limit_currency):
        """Sets the overdraft_contracted_limit_currency of this AccountOverdraftLimitsData.

        Moeda referente ao valor do limite contratado do cheque especial, segundo modelo ISO-4217. p.ex. 'BRL'. Pode ser preenchido com “NA” caso a instituição não possua a informação.  # noqa: E501

        :param overdraft_contracted_limit_currency: The overdraft_contracted_limit_currency of this AccountOverdraftLimitsData.  # noqa: E501
        :type: str
        """
        if overdraft_contracted_limit_currency is None:
            raise ValueError("Invalid value for `overdraft_contracted_limit_currency`, must not be `None`")  # noqa: E501

        self._overdraft_contracted_limit_currency = overdraft_contracted_limit_currency

    @property
    def overdraft_used_limit(self):
        """Gets the overdraft_used_limit of this AccountOverdraftLimitsData.  # noqa: E501

        Valor utilizado total do limite do cheque especial e o adiantamento a depositante.  # noqa: E501

        :return: The overdraft_used_limit of this AccountOverdraftLimitsData.  # noqa: E501
        :rtype: float
        """
        return self._overdraft_used_limit

    @overdraft_used_limit.setter
    def overdraft_used_limit(self, overdraft_used_limit):
        """Sets the overdraft_used_limit of this AccountOverdraftLimitsData.

        Valor utilizado total do limite do cheque especial e o adiantamento a depositante.  # noqa: E501

        :param overdraft_used_limit: The overdraft_used_limit of this AccountOverdraftLimitsData.  # noqa: E501
        :type: float
        """
        if overdraft_used_limit is None:
            raise ValueError("Invalid value for `overdraft_used_limit`, must not be `None`")  # noqa: E501

        self._overdraft_used_limit = overdraft_used_limit

    @property
    def overdraft_used_limit_currency(self):
        """Gets the overdraft_used_limit_currency of this AccountOverdraftLimitsData.  # noqa: E501

        Moeda referente ao valor utilizado total do limite do cheque especial e o adiantamento a depositante, segundo modelo ISO-4217. p.ex. 'BRL'. Pode ser preenchido com “NA” caso a instituição não possua a informação.  # noqa: E501

        :return: The overdraft_used_limit_currency of this AccountOverdraftLimitsData.  # noqa: E501
        :rtype: str
        """
        return self._overdraft_used_limit_currency

    @overdraft_used_limit_currency.setter
    def overdraft_used_limit_currency(self, overdraft_used_limit_currency):
        """Sets the overdraft_used_limit_currency of this AccountOverdraftLimitsData.

        Moeda referente ao valor utilizado total do limite do cheque especial e o adiantamento a depositante, segundo modelo ISO-4217. p.ex. 'BRL'. Pode ser preenchido com “NA” caso a instituição não possua a informação.  # noqa: E501

        :param overdraft_used_limit_currency: The overdraft_used_limit_currency of this AccountOverdraftLimitsData.  # noqa: E501
        :type: str
        """
        if overdraft_used_limit_currency is None:
            raise ValueError("Invalid value for `overdraft_used_limit_currency`, must not be `None`")  # noqa: E501

        self._overdraft_used_limit_currency = overdraft_used_limit_currency

    @property
    def unarranged_overdraft_amount(self):
        """Gets the unarranged_overdraft_amount of this AccountOverdraftLimitsData.  # noqa: E501

        Valor de operação contratada em caráter emergencial para cobertura de saldo devedor em conta de depósitos à vista e de excesso sobre o limite pactuado de cheque especial.  # noqa: E501

        :return: The unarranged_overdraft_amount of this AccountOverdraftLimitsData.  # noqa: E501
        :rtype: float
        """
        return self._unarranged_overdraft_amount

    @unarranged_overdraft_amount.setter
    def unarranged_overdraft_amount(self, unarranged_overdraft_amount):
        """Sets the unarranged_overdraft_amount of this AccountOverdraftLimitsData.

        Valor de operação contratada em caráter emergencial para cobertura de saldo devedor em conta de depósitos à vista e de excesso sobre o limite pactuado de cheque especial.  # noqa: E501

        :param unarranged_overdraft_amount: The unarranged_overdraft_amount of this AccountOverdraftLimitsData.  # noqa: E501
        :type: float
        """
        if unarranged_overdraft_amount is None:
            raise ValueError("Invalid value for `unarranged_overdraft_amount`, must not be `None`")  # noqa: E501

        self._unarranged_overdraft_amount = unarranged_overdraft_amount

    @property
    def unarranged_overdraft_amount_currency(self):
        """Gets the unarranged_overdraft_amount_currency of this AccountOverdraftLimitsData.  # noqa: E501

        Moeda referente ao valor de operação contratada em caráter emergencial para cobertura de saldo devedor em conta de depósitos à vista e de excesso sobre o limite pactuado de cheque especial, segundo modelo ISO-4217. p.ex. 'BRL'. Pode ser preenchido com “NA” caso a instituição não possua a informação.  # noqa: E501

        :return: The unarranged_overdraft_amount_currency of this AccountOverdraftLimitsData.  # noqa: E501
        :rtype: str
        """
        return self._unarranged_overdraft_amount_currency

    @unarranged_overdraft_amount_currency.setter
    def unarranged_overdraft_amount_currency(self, unarranged_overdraft_amount_currency):
        """Sets the unarranged_overdraft_amount_currency of this AccountOverdraftLimitsData.

        Moeda referente ao valor de operação contratada em caráter emergencial para cobertura de saldo devedor em conta de depósitos à vista e de excesso sobre o limite pactuado de cheque especial, segundo modelo ISO-4217. p.ex. 'BRL'. Pode ser preenchido com “NA” caso a instituição não possua a informação.  # noqa: E501

        :param unarranged_overdraft_amount_currency: The unarranged_overdraft_amount_currency of this AccountOverdraftLimitsData.  # noqa: E501
        :type: str
        """
        if unarranged_overdraft_amount_currency is None:
            raise ValueError("Invalid value for `unarranged_overdraft_amount_currency`, must not be `None`")  # noqa: E501

        self._unarranged_overdraft_amount_currency = unarranged_overdraft_amount_currency

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
        if issubclass(AccountOverdraftLimitsData, dict):
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
        if not isinstance(other, AccountOverdraftLimitsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
