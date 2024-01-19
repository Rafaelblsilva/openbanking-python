# coding: utf-8

"""
    API Financings - Open Banking Brasil

    API de informações de operações de financiamentos do Open Banking Brasil – Fase 2. API que retorna informações de operações de crédito do tipo financiamento, mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos, amortizações, garantias, encargos e taxas de juros remuneratórios.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ### Observação   - No endpoint `/contracts/{contratId}/payments` a paginação ocorrerá sob os dados contidos no campo `releases` do tipo lista.  ## Permissions necessárias para a API Financings  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **FINANCINGS_READ** ### `/contracts/{contractId}`   - permissions:     - GET **FINANCINGS_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **FINANCINGS_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **FINANCINGS_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **FINANCINGS_PAYMENTS_READ**   # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FinancingsInstalments(object):
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
        'type_number_of_instalments': 'str',
        'total_number_of_instalments': 'float',
        'type_contract_remaining': 'str',
        'contract_remaining_number': 'float',
        'paid_instalments': 'float',
        'due_instalments': 'float',
        'past_due_instalments': 'float',
        'balloon_payments': 'list[FinancingsBalloonPayment]'
    }

    attribute_map = {
        'type_number_of_instalments': 'typeNumberOfInstalments',
        'total_number_of_instalments': 'totalNumberOfInstalments',
        'type_contract_remaining': 'typeContractRemaining',
        'contract_remaining_number': 'contractRemainingNumber',
        'paid_instalments': 'paidInstalments',
        'due_instalments': 'dueInstalments',
        'past_due_instalments': 'pastDueInstalments',
        'balloon_payments': 'balloonPayments'
    }

    def __init__(self, type_number_of_instalments=None, total_number_of_instalments=None, type_contract_remaining=None, contract_remaining_number=None, paid_instalments=None, due_instalments=None, past_due_instalments=None, balloon_payments=None):  # noqa: E501
        """FinancingsInstalments - a model defined in Swagger"""  # noqa: E501
        self._type_number_of_instalments = None
        self._total_number_of_instalments = None
        self._type_contract_remaining = None
        self._contract_remaining_number = None
        self._paid_instalments = None
        self._due_instalments = None
        self._past_due_instalments = None
        self._balloon_payments = None
        self.discriminator = None
        self.type_number_of_instalments = type_number_of_instalments
        if total_number_of_instalments is not None:
            self.total_number_of_instalments = total_number_of_instalments
        self.type_contract_remaining = type_contract_remaining
        if contract_remaining_number is not None:
            self.contract_remaining_number = contract_remaining_number
        self.paid_instalments = paid_instalments
        if due_instalments is not None:
            self.due_instalments = due_instalments
        if past_due_instalments is not None:
            self.past_due_instalments = past_due_instalments
        if balloon_payments is not None:
            self.balloon_payments = balloon_payments

    @property
    def type_number_of_instalments(self):
        """Gets the type_number_of_instalments of this FinancingsInstalments.  # noqa: E501

        Tipo de prazo total do contrato referente à modalidade de crédito informada.  # noqa: E501

        :return: The type_number_of_instalments of this FinancingsInstalments.  # noqa: E501
        :rtype: str
        """
        return self._type_number_of_instalments

    @type_number_of_instalments.setter
    def type_number_of_instalments(self, type_number_of_instalments):
        """Sets the type_number_of_instalments of this FinancingsInstalments.

        Tipo de prazo total do contrato referente à modalidade de crédito informada.  # noqa: E501

        :param type_number_of_instalments: The type_number_of_instalments of this FinancingsInstalments.  # noqa: E501
        :type: str
        """
        if type_number_of_instalments is None:
            raise ValueError("Invalid value for `type_number_of_instalments`, must not be `None`")  # noqa: E501
        allowed_values = ["DIA", "SEMANA", "MES", "ANO", "SEM_PRAZO_TOTAL"]  # noqa: E501
        if type_number_of_instalments not in allowed_values:
            raise ValueError(
                "Invalid value for `type_number_of_instalments` ({0}), must be one of {1}"  # noqa: E501
                .format(type_number_of_instalments, allowed_values)
            )

        self._type_number_of_instalments = type_number_of_instalments

    @property
    def total_number_of_instalments(self):
        """Gets the total_number_of_instalments of this FinancingsInstalments.  # noqa: E501

        Prazo Total segundo o tipo (dia, semana, mês, ano) referente à Modalidade de Crédito informada.  [Restrição] Obrigatoriamente deve ser preenchido caso o typeNumberOfInstalments seja diferente de SEM_PRAZO_TOTAL.   # noqa: E501

        :return: The total_number_of_instalments of this FinancingsInstalments.  # noqa: E501
        :rtype: float
        """
        return self._total_number_of_instalments

    @total_number_of_instalments.setter
    def total_number_of_instalments(self, total_number_of_instalments):
        """Sets the total_number_of_instalments of this FinancingsInstalments.

        Prazo Total segundo o tipo (dia, semana, mês, ano) referente à Modalidade de Crédito informada.  [Restrição] Obrigatoriamente deve ser preenchido caso o typeNumberOfInstalments seja diferente de SEM_PRAZO_TOTAL.   # noqa: E501

        :param total_number_of_instalments: The total_number_of_instalments of this FinancingsInstalments.  # noqa: E501
        :type: float
        """

        self._total_number_of_instalments = total_number_of_instalments

    @property
    def type_contract_remaining(self):
        """Gets the type_contract_remaining of this FinancingsInstalments.  # noqa: E501

        Tipo de prazo remanescente do contrato referente à modalidade de crédito informada.   # noqa: E501

        :return: The type_contract_remaining of this FinancingsInstalments.  # noqa: E501
        :rtype: str
        """
        return self._type_contract_remaining

    @type_contract_remaining.setter
    def type_contract_remaining(self, type_contract_remaining):
        """Sets the type_contract_remaining of this FinancingsInstalments.

        Tipo de prazo remanescente do contrato referente à modalidade de crédito informada.   # noqa: E501

        :param type_contract_remaining: The type_contract_remaining of this FinancingsInstalments.  # noqa: E501
        :type: str
        """
        if type_contract_remaining is None:
            raise ValueError("Invalid value for `type_contract_remaining`, must not be `None`")  # noqa: E501
        allowed_values = ["DIA", "SEMANA", "MES", "ANO", "SEM_PRAZO_REMANESCENTE"]  # noqa: E501
        if type_contract_remaining not in allowed_values:
            raise ValueError(
                "Invalid value for `type_contract_remaining` ({0}), must be one of {1}"  # noqa: E501
                .format(type_contract_remaining, allowed_values)
            )

        self._type_contract_remaining = type_contract_remaining

    @property
    def contract_remaining_number(self):
        """Gets the contract_remaining_number of this FinancingsInstalments.  # noqa: E501

        Prazo Remanescente segundo o tipo (dia, semana, mês, ano) referente à Modalidade de Crédito informada.  [Restrição] Obrigatoriamente deve ser preenchido caso o typeNumberOfInstalments seja diferente de SEM_PRAZO_REMANESCENTE.   # noqa: E501

        :return: The contract_remaining_number of this FinancingsInstalments.  # noqa: E501
        :rtype: float
        """
        return self._contract_remaining_number

    @contract_remaining_number.setter
    def contract_remaining_number(self, contract_remaining_number):
        """Sets the contract_remaining_number of this FinancingsInstalments.

        Prazo Remanescente segundo o tipo (dia, semana, mês, ano) referente à Modalidade de Crédito informada.  [Restrição] Obrigatoriamente deve ser preenchido caso o typeNumberOfInstalments seja diferente de SEM_PRAZO_REMANESCENTE.   # noqa: E501

        :param contract_remaining_number: The contract_remaining_number of this FinancingsInstalments.  # noqa: E501
        :type: float
        """

        self._contract_remaining_number = contract_remaining_number

    @property
    def paid_instalments(self):
        """Gets the paid_instalments of this FinancingsInstalments.  # noqa: E501

        Quantidade de prestações pagas. (No caso de modalidades que não possuam parcelas, o número de prestações é igual a zero)  # noqa: E501

        :return: The paid_instalments of this FinancingsInstalments.  # noqa: E501
        :rtype: float
        """
        return self._paid_instalments

    @paid_instalments.setter
    def paid_instalments(self, paid_instalments):
        """Sets the paid_instalments of this FinancingsInstalments.

        Quantidade de prestações pagas. (No caso de modalidades que não possuam parcelas, o número de prestações é igual a zero)  # noqa: E501

        :param paid_instalments: The paid_instalments of this FinancingsInstalments.  # noqa: E501
        :type: float
        """
        if paid_instalments is None:
            raise ValueError("Invalid value for `paid_instalments`, must not be `None`")  # noqa: E501

        self._paid_instalments = paid_instalments

    @property
    def due_instalments(self):
        """Gets the due_instalments of this FinancingsInstalments.  # noqa: E501

        Quantidade de prestações a vencer.  [Restrição] Obrigatório para modalidades que possuam parcelas.   # noqa: E501

        :return: The due_instalments of this FinancingsInstalments.  # noqa: E501
        :rtype: float
        """
        return self._due_instalments

    @due_instalments.setter
    def due_instalments(self, due_instalments):
        """Sets the due_instalments of this FinancingsInstalments.

        Quantidade de prestações a vencer.  [Restrição] Obrigatório para modalidades que possuam parcelas.   # noqa: E501

        :param due_instalments: The due_instalments of this FinancingsInstalments.  # noqa: E501
        :type: float
        """

        self._due_instalments = due_instalments

    @property
    def past_due_instalments(self):
        """Gets the past_due_instalments of this FinancingsInstalments.  # noqa: E501

        Quantidade de prestações vencidas.  [Restrição] Obrigatório para modalidades que possuam parcelas.   # noqa: E501

        :return: The past_due_instalments of this FinancingsInstalments.  # noqa: E501
        :rtype: float
        """
        return self._past_due_instalments

    @past_due_instalments.setter
    def past_due_instalments(self, past_due_instalments):
        """Sets the past_due_instalments of this FinancingsInstalments.

        Quantidade de prestações vencidas.  [Restrição] Obrigatório para modalidades que possuam parcelas.   # noqa: E501

        :param past_due_instalments: The past_due_instalments of this FinancingsInstalments.  # noqa: E501
        :type: float
        """

        self._past_due_instalments = past_due_instalments

    @property
    def balloon_payments(self):
        """Gets the balloon_payments of this FinancingsInstalments.  # noqa: E501

        Lista que traz as datas de vencimento e valor das parcelas não regulares do contrato da modalidade de crédito consultada  # noqa: E501

        :return: The balloon_payments of this FinancingsInstalments.  # noqa: E501
        :rtype: list[FinancingsBalloonPayment]
        """
        return self._balloon_payments

    @balloon_payments.setter
    def balloon_payments(self, balloon_payments):
        """Sets the balloon_payments of this FinancingsInstalments.

        Lista que traz as datas de vencimento e valor das parcelas não regulares do contrato da modalidade de crédito consultada  # noqa: E501

        :param balloon_payments: The balloon_payments of this FinancingsInstalments.  # noqa: E501
        :type: list[FinancingsBalloonPayment]
        """

        self._balloon_payments = balloon_payments

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
        if issubclass(FinancingsInstalments, dict):
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
        if not isinstance(other, FinancingsInstalments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
