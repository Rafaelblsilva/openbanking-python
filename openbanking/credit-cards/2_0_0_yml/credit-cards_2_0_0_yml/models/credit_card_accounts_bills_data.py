# coding: utf-8

"""
    API Credit-cards-accounts - Open Banking Brasil

    API de contas de pagamento pós-pagas do Open Banking Brasil – Fase 2. API que retorna informações de contas de pagamento pós-paga mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, produto, bandeira, limites de crédito, informações sobre transações de pagamento efetuadas e faturas.  Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.\\ ### `/accounts/{creditCardAccountId}/bills`   - description:     - Só deve ser informada uma fatura já fechada.     - Qualquer pagamento deve ser contado para a última fatura fechada. ### `/accounts/{creditCardAccountId}/bills/{billId}/transactions`   - description:     - A lista a retornar se refere a transações após base 2/clearing/conciliado ### `/accounts/{creditCardAccountId}/transactions`   - description:     - A lista a retornar se refere a transações após base 2/clearing/conciliado  ## Permissions necessárias para a API Credit-cards-accounts  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/accounts`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### `/accounts/{creditCardAccountId}`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### `/accounts/{creditCardAccountId}/bills`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_READ** ### `/accounts/{creditCardAccountId}/bills/{billId}/transactions`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_TRANSACTIONS_READ** ### `/accounts/{creditCardAccountId}/limits`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_LIMITS_READ** ### `/accounts/{creditCardAccountId}/transactions`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ** ### `/accounts/{creditCardAccountId}/transactions-current`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ**   # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreditCardAccountsBillsData(object):
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
        'bill_id': 'str',
        'due_date': 'date',
        'bill_total_amount': 'CreditCardsBillTotalAmount',
        'bill_minimum_amount': 'CreditCardAccountsBillMinimumAmount',
        'is_instalment': 'bool',
        'finance_charges': 'list[CreditCardAccountsBillsFinanceCharge]',
        'payments': 'list[CreditCardAccountsBillsPayment]'
    }

    attribute_map = {
        'bill_id': 'billId',
        'due_date': 'dueDate',
        'bill_total_amount': 'billTotalAmount',
        'bill_minimum_amount': 'billMinimumAmount',
        'is_instalment': 'isInstalment',
        'finance_charges': 'financeCharges',
        'payments': 'payments'
    }

    def __init__(self, bill_id=None, due_date=None, bill_total_amount=None, bill_minimum_amount=None, is_instalment=None, finance_charges=None, payments=None):  # noqa: E501
        """CreditCardAccountsBillsData - a model defined in Swagger"""  # noqa: E501
        self._bill_id = None
        self._due_date = None
        self._bill_total_amount = None
        self._bill_minimum_amount = None
        self._is_instalment = None
        self._finance_charges = None
        self._payments = None
        self.discriminator = None
        self.bill_id = bill_id
        self.due_date = due_date
        self.bill_total_amount = bill_total_amount
        self.bill_minimum_amount = bill_minimum_amount
        self.is_instalment = is_instalment
        if finance_charges is not None:
            self.finance_charges = finance_charges
        self.payments = payments

    @property
    def bill_id(self):
        """Gets the bill_id of this CreditCardAccountsBillsData.  # noqa: E501

        Informação que identifica a fatura  # noqa: E501

        :return: The bill_id of this CreditCardAccountsBillsData.  # noqa: E501
        :rtype: str
        """
        return self._bill_id

    @bill_id.setter
    def bill_id(self, bill_id):
        """Sets the bill_id of this CreditCardAccountsBillsData.

        Informação que identifica a fatura  # noqa: E501

        :param bill_id: The bill_id of this CreditCardAccountsBillsData.  # noqa: E501
        :type: str
        """
        if bill_id is None:
            raise ValueError("Invalid value for `bill_id`, must not be `None`")  # noqa: E501

        self._bill_id = bill_id

    @property
    def due_date(self):
        """Gets the due_date of this CreditCardAccountsBillsData.  # noqa: E501

        Data de vencimento da Fatura, que aparece para pagamento pelo cliente  # noqa: E501

        :return: The due_date of this CreditCardAccountsBillsData.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this CreditCardAccountsBillsData.

        Data de vencimento da Fatura, que aparece para pagamento pelo cliente  # noqa: E501

        :param due_date: The due_date of this CreditCardAccountsBillsData.  # noqa: E501
        :type: date
        """
        if due_date is None:
            raise ValueError("Invalid value for `due_date`, must not be `None`")  # noqa: E501

        self._due_date = due_date

    @property
    def bill_total_amount(self):
        """Gets the bill_total_amount of this CreditCardAccountsBillsData.  # noqa: E501


        :return: The bill_total_amount of this CreditCardAccountsBillsData.  # noqa: E501
        :rtype: CreditCardsBillTotalAmount
        """
        return self._bill_total_amount

    @bill_total_amount.setter
    def bill_total_amount(self, bill_total_amount):
        """Sets the bill_total_amount of this CreditCardAccountsBillsData.


        :param bill_total_amount: The bill_total_amount of this CreditCardAccountsBillsData.  # noqa: E501
        :type: CreditCardsBillTotalAmount
        """
        if bill_total_amount is None:
            raise ValueError("Invalid value for `bill_total_amount`, must not be `None`")  # noqa: E501

        self._bill_total_amount = bill_total_amount

    @property
    def bill_minimum_amount(self):
        """Gets the bill_minimum_amount of this CreditCardAccountsBillsData.  # noqa: E501


        :return: The bill_minimum_amount of this CreditCardAccountsBillsData.  # noqa: E501
        :rtype: CreditCardAccountsBillMinimumAmount
        """
        return self._bill_minimum_amount

    @bill_minimum_amount.setter
    def bill_minimum_amount(self, bill_minimum_amount):
        """Sets the bill_minimum_amount of this CreditCardAccountsBillsData.


        :param bill_minimum_amount: The bill_minimum_amount of this CreditCardAccountsBillsData.  # noqa: E501
        :type: CreditCardAccountsBillMinimumAmount
        """
        if bill_minimum_amount is None:
            raise ValueError("Invalid value for `bill_minimum_amount`, must not be `None`")  # noqa: E501

        self._bill_minimum_amount = bill_minimum_amount

    @property
    def is_instalment(self):
        """Gets the is_instalment of this CreditCardAccountsBillsData.  # noqa: E501

        Indica se a fatura permite parcelamento (true) ou não (false).  # noqa: E501

        :return: The is_instalment of this CreditCardAccountsBillsData.  # noqa: E501
        :rtype: bool
        """
        return self._is_instalment

    @is_instalment.setter
    def is_instalment(self, is_instalment):
        """Sets the is_instalment of this CreditCardAccountsBillsData.

        Indica se a fatura permite parcelamento (true) ou não (false).  # noqa: E501

        :param is_instalment: The is_instalment of this CreditCardAccountsBillsData.  # noqa: E501
        :type: bool
        """
        if is_instalment is None:
            raise ValueError("Invalid value for `is_instalment`, must not be `None`")  # noqa: E501

        self._is_instalment = is_instalment

    @property
    def finance_charges(self):
        """Gets the finance_charges of this CreditCardAccountsBillsData.  # noqa: E501

        Lista dos encargos cobrados na fatura  # noqa: E501

        :return: The finance_charges of this CreditCardAccountsBillsData.  # noqa: E501
        :rtype: list[CreditCardAccountsBillsFinanceCharge]
        """
        return self._finance_charges

    @finance_charges.setter
    def finance_charges(self, finance_charges):
        """Sets the finance_charges of this CreditCardAccountsBillsData.

        Lista dos encargos cobrados na fatura  # noqa: E501

        :param finance_charges: The finance_charges of this CreditCardAccountsBillsData.  # noqa: E501
        :type: list[CreditCardAccountsBillsFinanceCharge]
        """

        self._finance_charges = finance_charges

    @property
    def payments(self):
        """Gets the payments of this CreditCardAccountsBillsData.  # noqa: E501

        Lista que traz os valores relativos aos pagamentos da Fatura da conta de pagamento pós-paga  # noqa: E501

        :return: The payments of this CreditCardAccountsBillsData.  # noqa: E501
        :rtype: list[CreditCardAccountsBillsPayment]
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this CreditCardAccountsBillsData.

        Lista que traz os valores relativos aos pagamentos da Fatura da conta de pagamento pós-paga  # noqa: E501

        :param payments: The payments of this CreditCardAccountsBillsData.  # noqa: E501
        :type: list[CreditCardAccountsBillsPayment]
        """
        if payments is None:
            raise ValueError("Invalid value for `payments`, must not be `None`")  # noqa: E501

        self._payments = payments

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
        if issubclass(CreditCardAccountsBillsData, dict):
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
        if not isinstance(other, CreditCardAccountsBillsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
