# coding: utf-8

"""
    API Accounts - Open Banking Brasil

    API de contas de depósito à vista, contas de poupança e contas pré-pagas do Open Banking Brasil – Fase 2. API que retorna informações de contas de depósito à vista, contas de poupança e contas de pagamento pré-pagas mantidas nas instituições transmissoras por seus clientes, incluindo dados de identificação da conta, saldos, limites e transações.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Accounts  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/accounts`   - permissions:     - GET: **ACCOUNTS_READ** ### `/accounts/{accountId}`   - permissions:     - GET: **ACCOUNTS_READ** ### `/accounts/{accountId}/balances`   - permissions:     - GET: **ACCOUNTS_BALANCES_READ** ### `/accounts/{accountId}/transactions`   - permissions:     - GET: **ACCOUNTS_TRANSACTIONS_READ** ### `/accounts/{accountId}/overdraft-limits`   - permissions:     - GET: **ACCOUNTS_OVERDRAFT_LIMITS_READ**   # noqa: E501

    OpenAPI spec version: 1.0.0-rc6.6
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AccountTransactionsData(object):
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
        'completed_authorised_payment_type': 'EnumCompletedAuthorisedPaymentIndicator',
        'credit_debit_type': 'EnumCreditDebitIndicator',
        'transaction_name': 'str',
        'type': 'EnumTransactionTypes',
        'amount': 'float',
        'transaction_currency': 'str',
        'transaction_date': 'str',
        'partie_cnpj_cpf': 'str',
        'partie_person_type': 'EnumPartiePersonType',
        'partie_compe_code': 'str',
        'partie_branch_code': 'str',
        'partie_number': 'str',
        'partie_check_digit': 'str'
    }

    attribute_map = {
        'transaction_id': 'transactionId',
        'completed_authorised_payment_type': 'completedAuthorisedPaymentType',
        'credit_debit_type': 'creditDebitType',
        'transaction_name': 'transactionName',
        'type': 'type',
        'amount': 'amount',
        'transaction_currency': 'transactionCurrency',
        'transaction_date': 'transactionDate',
        'partie_cnpj_cpf': 'partieCnpjCpf',
        'partie_person_type': 'partiePersonType',
        'partie_compe_code': 'partieCompeCode',
        'partie_branch_code': 'partieBranchCode',
        'partie_number': 'partieNumber',
        'partie_check_digit': 'partieCheckDigit'
    }

    def __init__(self, transaction_id=None, completed_authorised_payment_type=None, credit_debit_type=None, transaction_name=None, type=None, amount=None, transaction_currency=None, transaction_date=None, partie_cnpj_cpf=None, partie_person_type=None, partie_compe_code=None, partie_branch_code=None, partie_number=None, partie_check_digit=None):  # noqa: E501
        """AccountTransactionsData - a model defined in Swagger"""  # noqa: E501
        self._transaction_id = None
        self._completed_authorised_payment_type = None
        self._credit_debit_type = None
        self._transaction_name = None
        self._type = None
        self._amount = None
        self._transaction_currency = None
        self._transaction_date = None
        self._partie_cnpj_cpf = None
        self._partie_person_type = None
        self._partie_compe_code = None
        self._partie_branch_code = None
        self._partie_number = None
        self._partie_check_digit = None
        self.discriminator = None
        if transaction_id is not None:
            self.transaction_id = transaction_id
        self.completed_authorised_payment_type = completed_authorised_payment_type
        self.credit_debit_type = credit_debit_type
        self.transaction_name = transaction_name
        self.type = type
        self.amount = amount
        self.transaction_currency = transaction_currency
        self.transaction_date = transaction_date
        self.partie_cnpj_cpf = partie_cnpj_cpf
        self.partie_person_type = partie_person_type
        self.partie_compe_code = partie_compe_code
        self.partie_branch_code = partie_branch_code
        self.partie_number = partie_number
        self.partie_check_digit = partie_check_digit

    @property
    def transaction_id(self):
        """Gets the transaction_id of this AccountTransactionsData.  # noqa: E501

        Código ou identificador único prestado pela instituição que mantém a conta para representar a transação individual.  # noqa: E501

        :return: The transaction_id of this AccountTransactionsData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this AccountTransactionsData.

        Código ou identificador único prestado pela instituição que mantém a conta para representar a transação individual.  # noqa: E501

        :param transaction_id: The transaction_id of this AccountTransactionsData.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def completed_authorised_payment_type(self):
        """Gets the completed_authorised_payment_type of this AccountTransactionsData.  # noqa: E501


        :return: The completed_authorised_payment_type of this AccountTransactionsData.  # noqa: E501
        :rtype: EnumCompletedAuthorisedPaymentIndicator
        """
        return self._completed_authorised_payment_type

    @completed_authorised_payment_type.setter
    def completed_authorised_payment_type(self, completed_authorised_payment_type):
        """Sets the completed_authorised_payment_type of this AccountTransactionsData.


        :param completed_authorised_payment_type: The completed_authorised_payment_type of this AccountTransactionsData.  # noqa: E501
        :type: EnumCompletedAuthorisedPaymentIndicator
        """
        if completed_authorised_payment_type is None:
            raise ValueError("Invalid value for `completed_authorised_payment_type`, must not be `None`")  # noqa: E501

        self._completed_authorised_payment_type = completed_authorised_payment_type

    @property
    def credit_debit_type(self):
        """Gets the credit_debit_type of this AccountTransactionsData.  # noqa: E501


        :return: The credit_debit_type of this AccountTransactionsData.  # noqa: E501
        :rtype: EnumCreditDebitIndicator
        """
        return self._credit_debit_type

    @credit_debit_type.setter
    def credit_debit_type(self, credit_debit_type):
        """Sets the credit_debit_type of this AccountTransactionsData.


        :param credit_debit_type: The credit_debit_type of this AccountTransactionsData.  # noqa: E501
        :type: EnumCreditDebitIndicator
        """
        if credit_debit_type is None:
            raise ValueError("Invalid value for `credit_debit_type`, must not be `None`")  # noqa: E501

        self._credit_debit_type = credit_debit_type

    @property
    def transaction_name(self):
        """Gets the transaction_name of this AccountTransactionsData.  # noqa: E501

        Campo livre que corresponde ao identificador da transação na instituição financeira  # noqa: E501

        :return: The transaction_name of this AccountTransactionsData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_name

    @transaction_name.setter
    def transaction_name(self, transaction_name):
        """Sets the transaction_name of this AccountTransactionsData.

        Campo livre que corresponde ao identificador da transação na instituição financeira  # noqa: E501

        :param transaction_name: The transaction_name of this AccountTransactionsData.  # noqa: E501
        :type: str
        """
        if transaction_name is None:
            raise ValueError("Invalid value for `transaction_name`, must not be `None`")  # noqa: E501

        self._transaction_name = transaction_name

    @property
    def type(self):
        """Gets the type of this AccountTransactionsData.  # noqa: E501


        :return: The type of this AccountTransactionsData.  # noqa: E501
        :rtype: EnumTransactionTypes
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccountTransactionsData.


        :param type: The type of this AccountTransactionsData.  # noqa: E501
        :type: EnumTransactionTypes
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def amount(self):
        """Gets the amount of this AccountTransactionsData.  # noqa: E501

        Valor da transação. Expressa em valor monetário com 4 casas decimais.  # noqa: E501

        :return: The amount of this AccountTransactionsData.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AccountTransactionsData.

        Valor da transação. Expressa em valor monetário com 4 casas decimais.  # noqa: E501

        :param amount: The amount of this AccountTransactionsData.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def transaction_currency(self):
        """Gets the transaction_currency of this AccountTransactionsData.  # noqa: E501

        Moeda referente ao valor da transação, segundo modelo ISO-4217. p.ex. 'BRL'.  # noqa: E501

        :return: The transaction_currency of this AccountTransactionsData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_currency

    @transaction_currency.setter
    def transaction_currency(self, transaction_currency):
        """Sets the transaction_currency of this AccountTransactionsData.

        Moeda referente ao valor da transação, segundo modelo ISO-4217. p.ex. 'BRL'.  # noqa: E501

        :param transaction_currency: The transaction_currency of this AccountTransactionsData.  # noqa: E501
        :type: str
        """
        if transaction_currency is None:
            raise ValueError("Invalid value for `transaction_currency`, must not be `None`")  # noqa: E501

        self._transaction_currency = transaction_currency

    @property
    def transaction_date(self):
        """Gets the transaction_date of this AccountTransactionsData.  # noqa: E501

        Se indicador de transação: TRANSACAO_EFETIVADA - corresponde a data de lançamento da transação LANCAMENTO_FUTURO - corresponde a data prevista de efetivação da transação   # noqa: E501

        :return: The transaction_date of this AccountTransactionsData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        """Sets the transaction_date of this AccountTransactionsData.

        Se indicador de transação: TRANSACAO_EFETIVADA - corresponde a data de lançamento da transação LANCAMENTO_FUTURO - corresponde a data prevista de efetivação da transação   # noqa: E501

        :param transaction_date: The transaction_date of this AccountTransactionsData.  # noqa: E501
        :type: str
        """
        if transaction_date is None:
            raise ValueError("Invalid value for `transaction_date`, must not be `None`")  # noqa: E501

        self._transaction_date = transaction_date

    @property
    def partie_cnpj_cpf(self):
        """Gets the partie_cnpj_cpf of this AccountTransactionsData.  # noqa: E501

        Identificação da pessoa envolvida na transação: pagador ou recebedor (Preencher com o CPF ou CNPJ, sem formatação)   # noqa: E501

        :return: The partie_cnpj_cpf of this AccountTransactionsData.  # noqa: E501
        :rtype: str
        """
        return self._partie_cnpj_cpf

    @partie_cnpj_cpf.setter
    def partie_cnpj_cpf(self, partie_cnpj_cpf):
        """Sets the partie_cnpj_cpf of this AccountTransactionsData.

        Identificação da pessoa envolvida na transação: pagador ou recebedor (Preencher com o CPF ou CNPJ, sem formatação)   # noqa: E501

        :param partie_cnpj_cpf: The partie_cnpj_cpf of this AccountTransactionsData.  # noqa: E501
        :type: str
        """
        if partie_cnpj_cpf is None:
            raise ValueError("Invalid value for `partie_cnpj_cpf`, must not be `None`")  # noqa: E501

        self._partie_cnpj_cpf = partie_cnpj_cpf

    @property
    def partie_person_type(self):
        """Gets the partie_person_type of this AccountTransactionsData.  # noqa: E501


        :return: The partie_person_type of this AccountTransactionsData.  # noqa: E501
        :rtype: EnumPartiePersonType
        """
        return self._partie_person_type

    @partie_person_type.setter
    def partie_person_type(self, partie_person_type):
        """Sets the partie_person_type of this AccountTransactionsData.


        :param partie_person_type: The partie_person_type of this AccountTransactionsData.  # noqa: E501
        :type: EnumPartiePersonType
        """
        if partie_person_type is None:
            raise ValueError("Invalid value for `partie_person_type`, must not be `None`")  # noqa: E501

        self._partie_person_type = partie_person_type

    @property
    def partie_compe_code(self):
        """Gets the partie_compe_code of this AccountTransactionsData.  # noqa: E501

        Código identificador atribuído pelo Banco Central do Brasil às instituições participantes do STR (Sistema de Transferência de reservas) referente à pessoa envolvida na transação. O número-código substituiu o antigo código COMPE. Todos os participantes do STR, exceto as Infraestruturas do Mercado Financeiro (IMF) e a Secretaria do Tesouro Nacional, possuem um número-código independentemente de participarem da Centralizadora da Compensação de Cheques (Compe). O campo tem a anotação “n/a” (“não se aplica”) para os participantes do STR aos quais não é atribuído um número-código  # noqa: E501

        :return: The partie_compe_code of this AccountTransactionsData.  # noqa: E501
        :rtype: str
        """
        return self._partie_compe_code

    @partie_compe_code.setter
    def partie_compe_code(self, partie_compe_code):
        """Sets the partie_compe_code of this AccountTransactionsData.

        Código identificador atribuído pelo Banco Central do Brasil às instituições participantes do STR (Sistema de Transferência de reservas) referente à pessoa envolvida na transação. O número-código substituiu o antigo código COMPE. Todos os participantes do STR, exceto as Infraestruturas do Mercado Financeiro (IMF) e a Secretaria do Tesouro Nacional, possuem um número-código independentemente de participarem da Centralizadora da Compensação de Cheques (Compe). O campo tem a anotação “n/a” (“não se aplica”) para os participantes do STR aos quais não é atribuído um número-código  # noqa: E501

        :param partie_compe_code: The partie_compe_code of this AccountTransactionsData.  # noqa: E501
        :type: str
        """
        if partie_compe_code is None:
            raise ValueError("Invalid value for `partie_compe_code`, must not be `None`")  # noqa: E501

        self._partie_compe_code = partie_compe_code

    @property
    def partie_branch_code(self):
        """Gets the partie_branch_code of this AccountTransactionsData.  # noqa: E501

        Código da Agência detentora da conta da pessoa envolvida na transação. (Agência é a dependência destinada ao atendimento aos clientes, ao público em geral e aos associados de cooperativas de crédito, no exercício de atividades da instituição, não podendo ser móvel ou transitória)  # noqa: E501

        :return: The partie_branch_code of this AccountTransactionsData.  # noqa: E501
        :rtype: str
        """
        return self._partie_branch_code

    @partie_branch_code.setter
    def partie_branch_code(self, partie_branch_code):
        """Sets the partie_branch_code of this AccountTransactionsData.

        Código da Agência detentora da conta da pessoa envolvida na transação. (Agência é a dependência destinada ao atendimento aos clientes, ao público em geral e aos associados de cooperativas de crédito, no exercício de atividades da instituição, não podendo ser móvel ou transitória)  # noqa: E501

        :param partie_branch_code: The partie_branch_code of this AccountTransactionsData.  # noqa: E501
        :type: str
        """
        if partie_branch_code is None:
            raise ValueError("Invalid value for `partie_branch_code`, must not be `None`")  # noqa: E501

        self._partie_branch_code = partie_branch_code

    @property
    def partie_number(self):
        """Gets the partie_number of this AccountTransactionsData.  # noqa: E501

        Número da conta da pessoa envolvida na transação  # noqa: E501

        :return: The partie_number of this AccountTransactionsData.  # noqa: E501
        :rtype: str
        """
        return self._partie_number

    @partie_number.setter
    def partie_number(self, partie_number):
        """Sets the partie_number of this AccountTransactionsData.

        Número da conta da pessoa envolvida na transação  # noqa: E501

        :param partie_number: The partie_number of this AccountTransactionsData.  # noqa: E501
        :type: str
        """
        if partie_number is None:
            raise ValueError("Invalid value for `partie_number`, must not be `None`")  # noqa: E501

        self._partie_number = partie_number

    @property
    def partie_check_digit(self):
        """Gets the partie_check_digit of this AccountTransactionsData.  # noqa: E501

        Dígito da conta da pessoa envolvida na transação  # noqa: E501

        :return: The partie_check_digit of this AccountTransactionsData.  # noqa: E501
        :rtype: str
        """
        return self._partie_check_digit

    @partie_check_digit.setter
    def partie_check_digit(self, partie_check_digit):
        """Sets the partie_check_digit of this AccountTransactionsData.

        Dígito da conta da pessoa envolvida na transação  # noqa: E501

        :param partie_check_digit: The partie_check_digit of this AccountTransactionsData.  # noqa: E501
        :type: str
        """
        if partie_check_digit is None:
            raise ValueError("Invalid value for `partie_check_digit`, must not be `None`")  # noqa: E501

        self._partie_check_digit = partie_check_digit

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
        if issubclass(AccountTransactionsData, dict):
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
        if not isinstance(other, AccountTransactionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
