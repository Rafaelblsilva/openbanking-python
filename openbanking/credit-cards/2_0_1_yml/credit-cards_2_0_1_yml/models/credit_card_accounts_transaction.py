# coding: utf-8

"""
    API Credit-cards-accounts - Open Finance Brasil

    API de contas de pagamento pós-pagas do Open Finance Brasil – Fase 2. API que retorna informações de contas de pagamento pós-paga mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, produto, bandeira, limites de crédito, informações sobre transações de pagamento efetuadas e faturas.  Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.\\ ### `/accounts/{creditCardAccountId}/bills`   - description:     - Só deve ser informada uma fatura já fechada.     - Qualquer pagamento deve ser contado para a última fatura fechada. ### `/accounts/{creditCardAccountId}/bills/{billId}/transactions`   - description:     - A lista a retornar se refere a transações após base 2/clearing/conciliado ### `/accounts/{creditCardAccountId}/transactions`   - description:     - A lista a retornar se refere a transações após base 2/clearing/conciliado  ## Permissions necessárias para a API Credit-cards-accounts  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/accounts`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### `/accounts/{creditCardAccountId}`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### `/accounts/{creditCardAccountId}/bills`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_READ** ### `/accounts/{creditCardAccountId}/bills/{billId}/transactions`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_TRANSACTIONS_READ** ### `/accounts/{creditCardAccountId}/limits`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_LIMITS_READ** ### `/accounts/{creditCardAccountId}/transactions`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ** ### `/accounts/{creditCardAccountId}/transactions-current`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ**   # noqa: E501

    OpenAPI spec version: 2.0.1
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreditCardAccountsTransaction(object):
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
        'identification_number': 'str',
        'transaction_name': 'str',
        'bill_id': 'str',
        'credit_debit_type': 'EnumCreditDebitIndicator',
        'transaction_type': 'EnumCreditCardTransactionType',
        'transactional_additional_info': 'str',
        'payment_type': 'EnumCreditCardAccountsPaymentType',
        'fee_type': 'EnumCreditCardAccountFee',
        'fee_type_additional_info': 'str',
        'other_credits_type': 'EnumCreditCardAccountsOtherCreditType',
        'other_credits_additional_info': 'str',
        'charge_identificator': 'str',
        'charge_number': 'float',
        'brazilian_amount': 'CreditCardAccountsTransactionBrazilianAmount',
        'amount': 'CreditCardAccountsTransactionAmount',
        'transaction_date': 'date',
        'bill_post_date': 'date',
        'payee_mcc': 'float'
    }

    attribute_map = {
        'transaction_id': 'transactionId',
        'identification_number': 'identificationNumber',
        'transaction_name': 'transactionName',
        'bill_id': 'billId',
        'credit_debit_type': 'creditDebitType',
        'transaction_type': 'transactionType',
        'transactional_additional_info': 'transactionalAdditionalInfo',
        'payment_type': 'paymentType',
        'fee_type': 'feeType',
        'fee_type_additional_info': 'feeTypeAdditionalInfo',
        'other_credits_type': 'otherCreditsType',
        'other_credits_additional_info': 'otherCreditsAdditionalInfo',
        'charge_identificator': 'chargeIdentificator',
        'charge_number': 'chargeNumber',
        'brazilian_amount': 'brazilianAmount',
        'amount': 'amount',
        'transaction_date': 'transactionDate',
        'bill_post_date': 'billPostDate',
        'payee_mcc': 'payeeMCC'
    }

    def __init__(self, transaction_id=None, identification_number=None, transaction_name=None, bill_id=None, credit_debit_type=None, transaction_type=None, transactional_additional_info=None, payment_type=None, fee_type=None, fee_type_additional_info=None, other_credits_type=None, other_credits_additional_info=None, charge_identificator=None, charge_number=None, brazilian_amount=None, amount=None, transaction_date=None, bill_post_date=None, payee_mcc=None):  # noqa: E501
        """CreditCardAccountsTransaction - a model defined in Swagger"""  # noqa: E501
        self._transaction_id = None
        self._identification_number = None
        self._transaction_name = None
        self._bill_id = None
        self._credit_debit_type = None
        self._transaction_type = None
        self._transactional_additional_info = None
        self._payment_type = None
        self._fee_type = None
        self._fee_type_additional_info = None
        self._other_credits_type = None
        self._other_credits_additional_info = None
        self._charge_identificator = None
        self._charge_number = None
        self._brazilian_amount = None
        self._amount = None
        self._transaction_date = None
        self._bill_post_date = None
        self._payee_mcc = None
        self.discriminator = None
        if transaction_id is not None:
            self.transaction_id = transaction_id
        self.identification_number = identification_number
        self.transaction_name = transaction_name
        if bill_id is not None:
            self.bill_id = bill_id
        self.credit_debit_type = credit_debit_type
        self.transaction_type = transaction_type
        if transactional_additional_info is not None:
            self.transactional_additional_info = transactional_additional_info
        if payment_type is not None:
            self.payment_type = payment_type
        if fee_type is not None:
            self.fee_type = fee_type
        if fee_type_additional_info is not None:
            self.fee_type_additional_info = fee_type_additional_info
        if other_credits_type is not None:
            self.other_credits_type = other_credits_type
        if other_credits_additional_info is not None:
            self.other_credits_additional_info = other_credits_additional_info
        self.charge_identificator = charge_identificator
        if charge_number is not None:
            self.charge_number = charge_number
        self.brazilian_amount = brazilian_amount
        self.amount = amount
        self.transaction_date = transaction_date
        self.bill_post_date = bill_post_date
        if payee_mcc is not None:
            self.payee_mcc = payee_mcc

    @property
    def transaction_id(self):
        """Gets the transaction_id of this CreditCardAccountsTransaction.  # noqa: E501

        Código ou identificador único prestado pela instituição que mantém a conta para representar a transação individual.  # noqa: E501

        :return: The transaction_id of this CreditCardAccountsTransaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this CreditCardAccountsTransaction.

        Código ou identificador único prestado pela instituição que mantém a conta para representar a transação individual.  # noqa: E501

        :param transaction_id: The transaction_id of this CreditCardAccountsTransaction.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def identification_number(self):
        """Gets the identification_number of this CreditCardAccountsTransaction.  # noqa: E501

        Número de identificação do cartão: corresponde aos 4 últimos dígitos do cartão para PF, ou então, preencher com um identificador para PJ, com as caracteristicas definidas para os IDs no Open Finance.   # noqa: E501

        :return: The identification_number of this CreditCardAccountsTransaction.  # noqa: E501
        :rtype: str
        """
        return self._identification_number

    @identification_number.setter
    def identification_number(self, identification_number):
        """Sets the identification_number of this CreditCardAccountsTransaction.

        Número de identificação do cartão: corresponde aos 4 últimos dígitos do cartão para PF, ou então, preencher com um identificador para PJ, com as caracteristicas definidas para os IDs no Open Finance.   # noqa: E501

        :param identification_number: The identification_number of this CreditCardAccountsTransaction.  # noqa: E501
        :type: str
        """
        if identification_number is None:
            raise ValueError("Invalid value for `identification_number`, must not be `None`")  # noqa: E501

        self._identification_number = identification_number

    @property
    def transaction_name(self):
        """Gets the transaction_name of this CreditCardAccountsTransaction.  # noqa: E501

        Campo de livre preenchimento. Literal usada na instituição financeira para identificar a transação  # noqa: E501

        :return: The transaction_name of this CreditCardAccountsTransaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_name

    @transaction_name.setter
    def transaction_name(self, transaction_name):
        """Sets the transaction_name of this CreditCardAccountsTransaction.

        Campo de livre preenchimento. Literal usada na instituição financeira para identificar a transação  # noqa: E501

        :param transaction_name: The transaction_name of this CreditCardAccountsTransaction.  # noqa: E501
        :type: str
        """
        if transaction_name is None:
            raise ValueError("Invalid value for `transaction_name`, must not be `None`")  # noqa: E501

        self._transaction_name = transaction_name

    @property
    def bill_id(self):
        """Gets the bill_id of this CreditCardAccountsTransaction.  # noqa: E501

        Informação que identifica a fatura onde consta a transação informada.  # noqa: E501

        :return: The bill_id of this CreditCardAccountsTransaction.  # noqa: E501
        :rtype: str
        """
        return self._bill_id

    @bill_id.setter
    def bill_id(self, bill_id):
        """Sets the bill_id of this CreditCardAccountsTransaction.

        Informação que identifica a fatura onde consta a transação informada.  # noqa: E501

        :param bill_id: The bill_id of this CreditCardAccountsTransaction.  # noqa: E501
        :type: str
        """

        self._bill_id = bill_id

    @property
    def credit_debit_type(self):
        """Gets the credit_debit_type of this CreditCardAccountsTransaction.  # noqa: E501


        :return: The credit_debit_type of this CreditCardAccountsTransaction.  # noqa: E501
        :rtype: EnumCreditDebitIndicator
        """
        return self._credit_debit_type

    @credit_debit_type.setter
    def credit_debit_type(self, credit_debit_type):
        """Sets the credit_debit_type of this CreditCardAccountsTransaction.


        :param credit_debit_type: The credit_debit_type of this CreditCardAccountsTransaction.  # noqa: E501
        :type: EnumCreditDebitIndicator
        """
        if credit_debit_type is None:
            raise ValueError("Invalid value for `credit_debit_type`, must not be `None`")  # noqa: E501

        self._credit_debit_type = credit_debit_type

    @property
    def transaction_type(self):
        """Gets the transaction_type of this CreditCardAccountsTransaction.  # noqa: E501


        :return: The transaction_type of this CreditCardAccountsTransaction.  # noqa: E501
        :rtype: EnumCreditCardTransactionType
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this CreditCardAccountsTransaction.


        :param transaction_type: The transaction_type of this CreditCardAccountsTransaction.  # noqa: E501
        :type: EnumCreditCardTransactionType
        """
        if transaction_type is None:
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501

        self._transaction_type = transaction_type

    @property
    def transactional_additional_info(self):
        """Gets the transactional_additional_info of this CreditCardAccountsTransaction.  # noqa: E501

        Campo livre, de preenchimento obrigatório quando selecionado tipo de transação \"OUTROS\"  # noqa: E501

        :return: The transactional_additional_info of this CreditCardAccountsTransaction.  # noqa: E501
        :rtype: str
        """
        return self._transactional_additional_info

    @transactional_additional_info.setter
    def transactional_additional_info(self, transactional_additional_info):
        """Sets the transactional_additional_info of this CreditCardAccountsTransaction.

        Campo livre, de preenchimento obrigatório quando selecionado tipo de transação \"OUTROS\"  # noqa: E501

        :param transactional_additional_info: The transactional_additional_info of this CreditCardAccountsTransaction.  # noqa: E501
        :type: str
        """

        self._transactional_additional_info = transactional_additional_info

    @property
    def payment_type(self):
        """Gets the payment_type of this CreditCardAccountsTransaction.  # noqa: E501


        :return: The payment_type of this CreditCardAccountsTransaction.  # noqa: E501
        :rtype: EnumCreditCardAccountsPaymentType
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this CreditCardAccountsTransaction.


        :param payment_type: The payment_type of this CreditCardAccountsTransaction.  # noqa: E501
        :type: EnumCreditCardAccountsPaymentType
        """

        self._payment_type = payment_type

    @property
    def fee_type(self):
        """Gets the fee_type of this CreditCardAccountsTransaction.  # noqa: E501


        :return: The fee_type of this CreditCardAccountsTransaction.  # noqa: E501
        :rtype: EnumCreditCardAccountFee
        """
        return self._fee_type

    @fee_type.setter
    def fee_type(self, fee_type):
        """Sets the fee_type of this CreditCardAccountsTransaction.


        :param fee_type: The fee_type of this CreditCardAccountsTransaction.  # noqa: E501
        :type: EnumCreditCardAccountFee
        """

        self._fee_type = fee_type

    @property
    def fee_type_additional_info(self):
        """Gets the fee_type_additional_info of this CreditCardAccountsTransaction.  # noqa: E501

        Campo livre, de preenchimento obrigatório quando selecionada tipo de tarifa \"OUTRA\"  # noqa: E501

        :return: The fee_type_additional_info of this CreditCardAccountsTransaction.  # noqa: E501
        :rtype: str
        """
        return self._fee_type_additional_info

    @fee_type_additional_info.setter
    def fee_type_additional_info(self, fee_type_additional_info):
        """Sets the fee_type_additional_info of this CreditCardAccountsTransaction.

        Campo livre, de preenchimento obrigatório quando selecionada tipo de tarifa \"OUTRA\"  # noqa: E501

        :param fee_type_additional_info: The fee_type_additional_info of this CreditCardAccountsTransaction.  # noqa: E501
        :type: str
        """

        self._fee_type_additional_info = fee_type_additional_info

    @property
    def other_credits_type(self):
        """Gets the other_credits_type of this CreditCardAccountsTransaction.  # noqa: E501


        :return: The other_credits_type of this CreditCardAccountsTransaction.  # noqa: E501
        :rtype: EnumCreditCardAccountsOtherCreditType
        """
        return self._other_credits_type

    @other_credits_type.setter
    def other_credits_type(self, other_credits_type):
        """Sets the other_credits_type of this CreditCardAccountsTransaction.


        :param other_credits_type: The other_credits_type of this CreditCardAccountsTransaction.  # noqa: E501
        :type: EnumCreditCardAccountsOtherCreditType
        """

        self._other_credits_type = other_credits_type

    @property
    def other_credits_additional_info(self):
        """Gets the other_credits_additional_info of this CreditCardAccountsTransaction.  # noqa: E501

        Campo livre para preenchimento de dados adicionais de outros tipos de crédito contratados no cartão.  [Restrição] Preenchimento obrigatório quando selecionado no campo outros tipos de crédito \"OUTROS\".   # noqa: E501

        :return: The other_credits_additional_info of this CreditCardAccountsTransaction.  # noqa: E501
        :rtype: str
        """
        return self._other_credits_additional_info

    @other_credits_additional_info.setter
    def other_credits_additional_info(self, other_credits_additional_info):
        """Sets the other_credits_additional_info of this CreditCardAccountsTransaction.

        Campo livre para preenchimento de dados adicionais de outros tipos de crédito contratados no cartão.  [Restrição] Preenchimento obrigatório quando selecionado no campo outros tipos de crédito \"OUTROS\".   # noqa: E501

        :param other_credits_additional_info: The other_credits_additional_info of this CreditCardAccountsTransaction.  # noqa: E501
        :type: str
        """

        self._other_credits_additional_info = other_credits_additional_info

    @property
    def charge_identificator(self):
        """Gets the charge_identificator of this CreditCardAccountsTransaction.  # noqa: E501

        Identificador da parcela que está sendo informada. Campo de livre preenchimento  # noqa: E501

        :return: The charge_identificator of this CreditCardAccountsTransaction.  # noqa: E501
        :rtype: str
        """
        return self._charge_identificator

    @charge_identificator.setter
    def charge_identificator(self, charge_identificator):
        """Sets the charge_identificator of this CreditCardAccountsTransaction.

        Identificador da parcela que está sendo informada. Campo de livre preenchimento  # noqa: E501

        :param charge_identificator: The charge_identificator of this CreditCardAccountsTransaction.  # noqa: E501
        :type: str
        """
        if charge_identificator is None:
            raise ValueError("Invalid value for `charge_identificator`, must not be `None`")  # noqa: E501

        self._charge_identificator = charge_identificator

    @property
    def charge_number(self):
        """Gets the charge_number of this CreditCardAccountsTransaction.  # noqa: E501

        Quantidade de parcelas.    [Restrição] O campo deve ser preenchido quando houverem parcelas relacionadas a transação.   # noqa: E501

        :return: The charge_number of this CreditCardAccountsTransaction.  # noqa: E501
        :rtype: float
        """
        return self._charge_number

    @charge_number.setter
    def charge_number(self, charge_number):
        """Sets the charge_number of this CreditCardAccountsTransaction.

        Quantidade de parcelas.    [Restrição] O campo deve ser preenchido quando houverem parcelas relacionadas a transação.   # noqa: E501

        :param charge_number: The charge_number of this CreditCardAccountsTransaction.  # noqa: E501
        :type: float
        """

        self._charge_number = charge_number

    @property
    def brazilian_amount(self):
        """Gets the brazilian_amount of this CreditCardAccountsTransaction.  # noqa: E501


        :return: The brazilian_amount of this CreditCardAccountsTransaction.  # noqa: E501
        :rtype: CreditCardAccountsTransactionBrazilianAmount
        """
        return self._brazilian_amount

    @brazilian_amount.setter
    def brazilian_amount(self, brazilian_amount):
        """Sets the brazilian_amount of this CreditCardAccountsTransaction.


        :param brazilian_amount: The brazilian_amount of this CreditCardAccountsTransaction.  # noqa: E501
        :type: CreditCardAccountsTransactionBrazilianAmount
        """
        if brazilian_amount is None:
            raise ValueError("Invalid value for `brazilian_amount`, must not be `None`")  # noqa: E501

        self._brazilian_amount = brazilian_amount

    @property
    def amount(self):
        """Gets the amount of this CreditCardAccountsTransaction.  # noqa: E501


        :return: The amount of this CreditCardAccountsTransaction.  # noqa: E501
        :rtype: CreditCardAccountsTransactionAmount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreditCardAccountsTransaction.


        :param amount: The amount of this CreditCardAccountsTransaction.  # noqa: E501
        :type: CreditCardAccountsTransactionAmount
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def transaction_date(self):
        """Gets the transaction_date of this CreditCardAccountsTransaction.  # noqa: E501

        Data original da transação  # noqa: E501

        :return: The transaction_date of this CreditCardAccountsTransaction.  # noqa: E501
        :rtype: date
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        """Sets the transaction_date of this CreditCardAccountsTransaction.

        Data original da transação  # noqa: E501

        :param transaction_date: The transaction_date of this CreditCardAccountsTransaction.  # noqa: E501
        :type: date
        """
        if transaction_date is None:
            raise ValueError("Invalid value for `transaction_date`, must not be `None`")  # noqa: E501

        self._transaction_date = transaction_date

    @property
    def bill_post_date(self):
        """Gets the bill_post_date of this CreditCardAccountsTransaction.  # noqa: E501

        Data em que a transação foi inserida na fatura  # noqa: E501

        :return: The bill_post_date of this CreditCardAccountsTransaction.  # noqa: E501
        :rtype: date
        """
        return self._bill_post_date

    @bill_post_date.setter
    def bill_post_date(self, bill_post_date):
        """Sets the bill_post_date of this CreditCardAccountsTransaction.

        Data em que a transação foi inserida na fatura  # noqa: E501

        :param bill_post_date: The bill_post_date of this CreditCardAccountsTransaction.  # noqa: E501
        :type: date
        """
        if bill_post_date is None:
            raise ValueError("Invalid value for `bill_post_date`, must not be `None`")  # noqa: E501

        self._bill_post_date = bill_post_date

    @property
    def payee_mcc(self):
        """Gets the payee_mcc of this CreditCardAccountsTransaction.  # noqa: E501

        O MCC ou o código da categoria do estabelecimento comercial. Os MCCs são agrupados segundo suas similaridades. O MCC é usado para classificar o negócio pelo tipo fornecido de bens ou serviços. Os MCCs são atribuídos por tipo de comerciante (por exemplo, um para hotéis, um para lojas de materiais de escritório, etc.) ou por nome de comerciante (por exemplo, 3000 para a United Airlines).   # noqa: E501

        :return: The payee_mcc of this CreditCardAccountsTransaction.  # noqa: E501
        :rtype: float
        """
        return self._payee_mcc

    @payee_mcc.setter
    def payee_mcc(self, payee_mcc):
        """Sets the payee_mcc of this CreditCardAccountsTransaction.

        O MCC ou o código da categoria do estabelecimento comercial. Os MCCs são agrupados segundo suas similaridades. O MCC é usado para classificar o negócio pelo tipo fornecido de bens ou serviços. Os MCCs são atribuídos por tipo de comerciante (por exemplo, um para hotéis, um para lojas de materiais de escritório, etc.) ou por nome de comerciante (por exemplo, 3000 para a United Airlines).   # noqa: E501

        :param payee_mcc: The payee_mcc of this CreditCardAccountsTransaction.  # noqa: E501
        :type: float
        """

        self._payee_mcc = payee_mcc

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
        if issubclass(CreditCardAccountsTransaction, dict):
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
        if not isinstance(other, CreditCardAccountsTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
