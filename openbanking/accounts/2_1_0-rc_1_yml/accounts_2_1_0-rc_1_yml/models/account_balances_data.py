# coding: utf-8

"""
    API Accounts - Open Finance Brasil

    API de contas de depósito à vista, contas de poupança e contas pré-pagas do Open Finance Brasil – Fase 2. API que retorna informações de contas de depósito à vista, contas de poupança e contas de pagamento pré-pagas mantidas nas instituições transmissoras por seus clientes, incluindo dados de identificação da conta, saldos, limites e transações.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Accounts  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/accounts`   - permissions:     - GET: **ACCOUNTS_READ** ### `/accounts/{accountId}`   - permissions:     - GET: **ACCOUNTS_READ** ### `/accounts/{accountId}/balances`   - permissions:     - GET: **ACCOUNTS_BALANCES_READ** ### `/accounts/{accountId}/transactions`   - permissions:     - GET: **ACCOUNTS_TRANSACTIONS_READ** ### `/accounts/{accountId}/transactions-current`   - permissions:     - GET: **ACCOUNTS_TRANSACTIONS_READ** ### `/accounts/{accountId}/overdraft-limits`   - permissions:     - GET: **ACCOUNTS_OVERDRAFT_LIMITS_READ**  ## Tabela: Data de imutabilidade por tipo de transação ``` |---------------------------------------|-------------------------|-----------------------| | Tipo de Transação                     | Data da Obrigatoriedade | Data da Imutabilidade | |---------------------------------------|-------------------------|-----------------------| | TED                                   | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | PIX                                   | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | TRANSFERENCIA MESMA INSTITUIÇÃO (TEF) | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | TARIFA SERVIÇOS AVULSOS               | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | FOLHA DE PAGAMENTO                    | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | DOC                                   | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | BOLETO                                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | CONVÊNIO ARRECADAÇÃO                  | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | PACOTE TARIFA SERVIÇOS                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | DEPÓSITO                              | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | SAQUE                                 | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | CARTÃO                                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | ENCARGOS JUROS CHEQUE ESPECIAL        | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | RENDIMENTO APLICAÇÃO FINANCEIRA       | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | PORTABILIDADE SALÁRIO                 | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | RESGATE APLICAÇÃO FINANCEIRA          | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | OPERAÇÃO DE CRÉDITO                   | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | OUTROS                                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| ```   # noqa: E501

    OpenAPI spec version: 2.1.0-rc.1
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
        'available_amount': 'AccountBalancesDataAvailableAmount',
        'blocked_amount': 'AccountBalancesDataBlockedAmount',
        'automatically_invested_amount': 'AccountBalancesDataAutomaticallyInvestedAmount',
        'update_date_time': 'datetime'
    }

    attribute_map = {
        'available_amount': 'availableAmount',
        'blocked_amount': 'blockedAmount',
        'automatically_invested_amount': 'automaticallyInvestedAmount',
        'update_date_time': 'updateDateTime'
    }

    def __init__(self, available_amount=None, blocked_amount=None, automatically_invested_amount=None, update_date_time=None):  # noqa: E501
        """AccountBalancesData - a model defined in Swagger"""  # noqa: E501
        self._available_amount = None
        self._blocked_amount = None
        self._automatically_invested_amount = None
        self._update_date_time = None
        self.discriminator = None
        self.available_amount = available_amount
        self.blocked_amount = blocked_amount
        self.automatically_invested_amount = automatically_invested_amount
        self.update_date_time = update_date_time

    @property
    def available_amount(self):
        """Gets the available_amount of this AccountBalancesData.  # noqa: E501


        :return: The available_amount of this AccountBalancesData.  # noqa: E501
        :rtype: AccountBalancesDataAvailableAmount
        """
        return self._available_amount

    @available_amount.setter
    def available_amount(self, available_amount):
        """Sets the available_amount of this AccountBalancesData.


        :param available_amount: The available_amount of this AccountBalancesData.  # noqa: E501
        :type: AccountBalancesDataAvailableAmount
        """
        if available_amount is None:
            raise ValueError("Invalid value for `available_amount`, must not be `None`")  # noqa: E501

        self._available_amount = available_amount

    @property
    def blocked_amount(self):
        """Gets the blocked_amount of this AccountBalancesData.  # noqa: E501


        :return: The blocked_amount of this AccountBalancesData.  # noqa: E501
        :rtype: AccountBalancesDataBlockedAmount
        """
        return self._blocked_amount

    @blocked_amount.setter
    def blocked_amount(self, blocked_amount):
        """Sets the blocked_amount of this AccountBalancesData.


        :param blocked_amount: The blocked_amount of this AccountBalancesData.  # noqa: E501
        :type: AccountBalancesDataBlockedAmount
        """
        if blocked_amount is None:
            raise ValueError("Invalid value for `blocked_amount`, must not be `None`")  # noqa: E501

        self._blocked_amount = blocked_amount

    @property
    def automatically_invested_amount(self):
        """Gets the automatically_invested_amount of this AccountBalancesData.  # noqa: E501


        :return: The automatically_invested_amount of this AccountBalancesData.  # noqa: E501
        :rtype: AccountBalancesDataAutomaticallyInvestedAmount
        """
        return self._automatically_invested_amount

    @automatically_invested_amount.setter
    def automatically_invested_amount(self, automatically_invested_amount):
        """Sets the automatically_invested_amount of this AccountBalancesData.


        :param automatically_invested_amount: The automatically_invested_amount of this AccountBalancesData.  # noqa: E501
        :type: AccountBalancesDataAutomaticallyInvestedAmount
        """
        if automatically_invested_amount is None:
            raise ValueError("Invalid value for `automatically_invested_amount`, must not be `None`")  # noqa: E501

        self._automatically_invested_amount = automatically_invested_amount

    @property
    def update_date_time(self):
        """Gets the update_date_time of this AccountBalancesData.  # noqa: E501

        Data e hora da última atualização do saldo. É esperado que a instituição informe a última vez que capturou o saldo para compartilhamento no Open Finance. Dessa forma, é possível que: - Caso a instituição capture dados de forma síncrona essa informação seja de poucos momentos; - Caso a instituição capture dados de forma assíncrona essa informação seja de horas ou dias no passado; - Quando não existente uma data vinculada especificamente ao bloco, se assume a data e hora de atualização do cadastro como um todo.  De toda forma, é preciso continuar respeitando o prazo máximo de tempestividade da API de Contas.   # noqa: E501

        :return: The update_date_time of this AccountBalancesData.  # noqa: E501
        :rtype: datetime
        """
        return self._update_date_time

    @update_date_time.setter
    def update_date_time(self, update_date_time):
        """Sets the update_date_time of this AccountBalancesData.

        Data e hora da última atualização do saldo. É esperado que a instituição informe a última vez que capturou o saldo para compartilhamento no Open Finance. Dessa forma, é possível que: - Caso a instituição capture dados de forma síncrona essa informação seja de poucos momentos; - Caso a instituição capture dados de forma assíncrona essa informação seja de horas ou dias no passado; - Quando não existente uma data vinculada especificamente ao bloco, se assume a data e hora de atualização do cadastro como um todo.  De toda forma, é preciso continuar respeitando o prazo máximo de tempestividade da API de Contas.   # noqa: E501

        :param update_date_time: The update_date_time of this AccountBalancesData.  # noqa: E501
        :type: datetime
        """
        if update_date_time is None:
            raise ValueError("Invalid value for `update_date_time`, must not be `None`")  # noqa: E501

        self._update_date_time = update_date_time

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
