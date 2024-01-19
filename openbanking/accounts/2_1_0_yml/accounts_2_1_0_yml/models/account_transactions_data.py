# coding: utf-8

"""
    API Accounts - Open Finance Brasil

    API de contas de depósito à vista, contas de poupança e contas pré-pagas do Open Finance Brasil – Fase 2. API que retorna informações de contas de depósito à vista, contas de poupança e contas de pagamento pré-pagas mantidas nas instituições transmissoras por seus clientes, incluindo dados de identificação da conta, saldos, limites e transações.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Accounts  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/accounts`   - permissions:     - GET: **ACCOUNTS_READ** ### `/accounts/{accountId}`   - permissions:     - GET: **ACCOUNTS_READ** ### `/accounts/{accountId}/balances`   - permissions:     - GET: **ACCOUNTS_BALANCES_READ** ### `/accounts/{accountId}/transactions`   - permissions:     - GET: **ACCOUNTS_TRANSACTIONS_READ** ### `/accounts/{accountId}/transactions-current`   - permissions:     - GET: **ACCOUNTS_TRANSACTIONS_READ** ### `/accounts/{accountId}/overdraft-limits`   - permissions:     - GET: **ACCOUNTS_OVERDRAFT_LIMITS_READ**  ## Data de imutabilidade por tipo de transação​ O identificador de transações de contas é de envio obrigatório no Open Finance Brasil. De acordo com o tipo da transação deve haver o envio de um identificador único, estável e imutável em D0 ou D+1, conforme tabela abaixo ``` |---------------------------------------|-------------------------|-----------------------| | Tipo de Transação                     | Data da Obrigatoriedade | Data da Imutabilidade | |---------------------------------------|-------------------------|-----------------------| | TED                                   | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | PIX                                   | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | TRANSFERENCIA MESMA INSTITUIÇÃO (TEF) | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | TARIFA SERVIÇOS AVULSOS               | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | FOLHA DE PAGAMENTO                    | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | DOC                                   | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | BOLETO                                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | CONVÊNIO ARRECADAÇÃO                  | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | PACOTE TARIFA SERVIÇOS                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | DEPÓSITO                              | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | SAQUE                                 | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | CARTÃO                                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | ENCARGOS JUROS CHEQUE ESPECIAL        | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | RENDIMENTO APLICAÇÃO FINANCEIRA       | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | PORTABILIDADE SALÁRIO                 | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | RESGATE APLICAÇÃO FINANCEIRA          | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | OPERAÇÃO DE CRÉDITO                   | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | OUTROS                                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| ```   # noqa: E501

    OpenAPI spec version: 2.1.0
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
        'transaction_amount': 'AccountTransactionsDataAmount',
        'transaction_date': 'str',
        'transaction_date_time': 'str',
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
        'transaction_amount': 'transactionAmount',
        'transaction_date': 'transactionDate',
        'transaction_date_time': 'transactionDateTime',
        'partie_cnpj_cpf': 'partieCnpjCpf',
        'partie_person_type': 'partiePersonType',
        'partie_compe_code': 'partieCompeCode',
        'partie_branch_code': 'partieBranchCode',
        'partie_number': 'partieNumber',
        'partie_check_digit': 'partieCheckDigit'
    }

    def __init__(self, transaction_id=None, completed_authorised_payment_type=None, credit_debit_type=None, transaction_name=None, type=None, transaction_amount=None, transaction_date=None, transaction_date_time=None, partie_cnpj_cpf=None, partie_person_type=None, partie_compe_code=None, partie_branch_code=None, partie_number=None, partie_check_digit=None):  # noqa: E501
        """AccountTransactionsData - a model defined in Swagger"""  # noqa: E501
        self._transaction_id = None
        self._completed_authorised_payment_type = None
        self._credit_debit_type = None
        self._transaction_name = None
        self._type = None
        self._transaction_amount = None
        self._transaction_date = None
        self._transaction_date_time = None
        self._partie_cnpj_cpf = None
        self._partie_person_type = None
        self._partie_compe_code = None
        self._partie_branch_code = None
        self._partie_number = None
        self._partie_check_digit = None
        self.discriminator = None
        self.transaction_id = transaction_id
        self.completed_authorised_payment_type = completed_authorised_payment_type
        self.credit_debit_type = credit_debit_type
        self.transaction_name = transaction_name
        self.type = type
        self.transaction_amount = transaction_amount
        self.transaction_date = transaction_date
        self.transaction_date_time = transaction_date_time
        if partie_cnpj_cpf is not None:
            self.partie_cnpj_cpf = partie_cnpj_cpf
        if partie_person_type is not None:
            self.partie_person_type = partie_person_type
        if partie_compe_code is not None:
            self.partie_compe_code = partie_compe_code
        if partie_branch_code is not None:
            self.partie_branch_code = partie_branch_code
        if partie_number is not None:
            self.partie_number = partie_number
        if partie_check_digit is not None:
            self.partie_check_digit = partie_check_digit

    @property
    def transaction_id(self):
        """Gets the transaction_id of this AccountTransactionsData.  # noqa: E501

        Código ou identificador único prestado pela instituição que mantém a conta para representar a transação individual.  O ideal é que o `transactionId` seja imutável.  No entanto, o `transactionId` deve obedecer, no mínimo, as regras de imutabilidade propostas conforme tabela “Data de imutabilidade por tipo de transação” presente nas orientações desta API.   # noqa: E501

        :return: The transaction_id of this AccountTransactionsData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this AccountTransactionsData.

        Código ou identificador único prestado pela instituição que mantém a conta para representar a transação individual.  O ideal é que o `transactionId` seja imutável.  No entanto, o `transactionId` deve obedecer, no mínimo, as regras de imutabilidade propostas conforme tabela “Data de imutabilidade por tipo de transação” presente nas orientações desta API.   # noqa: E501

        :param transaction_id: The transaction_id of this AccountTransactionsData.  # noqa: E501
        :type: str
        """
        if transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501

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

        Literal usada na instituição financeira para identificar a transação. A informação apresentada precisa ser a mesma utilizada nos canais eletrônicos da instituição (extrato).  # noqa: E501

        :return: The transaction_name of this AccountTransactionsData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_name

    @transaction_name.setter
    def transaction_name(self, transaction_name):
        """Sets the transaction_name of this AccountTransactionsData.

        Literal usada na instituição financeira para identificar a transação. A informação apresentada precisa ser a mesma utilizada nos canais eletrônicos da instituição (extrato).  # noqa: E501

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
    def transaction_amount(self):
        """Gets the transaction_amount of this AccountTransactionsData.  # noqa: E501


        :return: The transaction_amount of this AccountTransactionsData.  # noqa: E501
        :rtype: AccountTransactionsDataAmount
        """
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, transaction_amount):
        """Sets the transaction_amount of this AccountTransactionsData.


        :param transaction_amount: The transaction_amount of this AccountTransactionsData.  # noqa: E501
        :type: AccountTransactionsDataAmount
        """
        if transaction_amount is None:
            raise ValueError("Invalid value for `transaction_amount`, must not be `None`")  # noqa: E501

        self._transaction_amount = transaction_amount

    @property
    def transaction_date(self):
        """Gets the transaction_date of this AccountTransactionsData.  # noqa: E501

        Se indicador de transação: TRANSACAO_EFETIVADA - corresponde a data de lançamento da transação LANCAMENTO_FUTURO - corresponde a data prevista de efetivação da transação.   # noqa: E501

        :return: The transaction_date of this AccountTransactionsData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        """Sets the transaction_date of this AccountTransactionsData.

        Se indicador de transação: TRANSACAO_EFETIVADA - corresponde a data de lançamento da transação LANCAMENTO_FUTURO - corresponde a data prevista de efetivação da transação.   # noqa: E501

        :param transaction_date: The transaction_date of this AccountTransactionsData.  # noqa: E501
        :type: str
        """
        if transaction_date is None:
            raise ValueError("Invalid value for `transaction_date`, must not be `None`")  # noqa: E501

        self._transaction_date = transaction_date

    @property
    def transaction_date_time(self):
        """Gets the transaction_date_time of this AccountTransactionsData.  # noqa: E501

        Data e hora original da transação. No primeiro momento, as instituições poderão complementar informações faltantes com 0 (Por exemplo: 2016-01-29T00:00:00.000Z). A partir de 31/01/2024 é esperado que o campo seja preenchido com informações reais.   # noqa: E501

        :return: The transaction_date_time of this AccountTransactionsData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_date_time

    @transaction_date_time.setter
    def transaction_date_time(self, transaction_date_time):
        """Sets the transaction_date_time of this AccountTransactionsData.

        Data e hora original da transação. No primeiro momento, as instituições poderão complementar informações faltantes com 0 (Por exemplo: 2016-01-29T00:00:00.000Z). A partir de 31/01/2024 é esperado que o campo seja preenchido com informações reais.   # noqa: E501

        :param transaction_date_time: The transaction_date_time of this AccountTransactionsData.  # noqa: E501
        :type: str
        """
        if transaction_date_time is None:
            raise ValueError("Invalid value for `transaction_date_time`, must not be `None`")  # noqa: E501

        self._transaction_date_time = transaction_date_time

    @property
    def partie_cnpj_cpf(self):
        """Gets the partie_cnpj_cpf of this AccountTransactionsData.  # noqa: E501

        Identificação da pessoa envolvida na transação: pagador ou recebedor (Preencher com o CPF ou CNPJ, sem formatação). Com a IN BCB nº 371, a partir de 02/05/23, o envio das informações de identificação de contraparte tornou-se obrigatória para transações de pagamento. Para maiores detalhes, favor consultar a página `Orientações - Contas`.   # noqa: E501

        :return: The partie_cnpj_cpf of this AccountTransactionsData.  # noqa: E501
        :rtype: str
        """
        return self._partie_cnpj_cpf

    @partie_cnpj_cpf.setter
    def partie_cnpj_cpf(self, partie_cnpj_cpf):
        """Sets the partie_cnpj_cpf of this AccountTransactionsData.

        Identificação da pessoa envolvida na transação: pagador ou recebedor (Preencher com o CPF ou CNPJ, sem formatação). Com a IN BCB nº 371, a partir de 02/05/23, o envio das informações de identificação de contraparte tornou-se obrigatória para transações de pagamento. Para maiores detalhes, favor consultar a página `Orientações - Contas`.   # noqa: E501

        :param partie_cnpj_cpf: The partie_cnpj_cpf of this AccountTransactionsData.  # noqa: E501
        :type: str
        """

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
