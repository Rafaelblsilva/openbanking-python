# coding: utf-8

"""
    API Loans - Open Banking Brasil

    API de informações de operações de empréstimos do Open Banking Brasil – Fase 2. API que retorna informações de operações de crédito do tipo empréstimo, mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos, amortizações, garantias, encargos e taxas de juros remuneratórios.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.    <br> ### Observação:   - No endpoint `/contracts/{contratId}/payments` a paginação ocorrerá sob os dados contidos no campo `releases` do tipo lista.    <br> ## Permissions necessárias para a API Loans  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **LOANS_READ** ### `/contracts/{contractId}`   - permissions:     - GET **LOANS_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **LOANS_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **LOANS_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **LOANS_PAYMENTS_READ**   # noqa: E501

    OpenAPI spec version: 2.0.0-RC1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LoansPayments(object):
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
        'paid_instalments': 'float',
        'contract_outstanding_balance': 'str',
        'releases': 'list[LoansReleases]'
    }

    attribute_map = {
        'paid_instalments': 'paidInstalments',
        'contract_outstanding_balance': 'contractOutstandingBalance',
        'releases': 'releases'
    }

    def __init__(self, paid_instalments=None, contract_outstanding_balance=None, releases=None):  # noqa: E501
        """LoansPayments - a model defined in Swagger"""  # noqa: E501
        self._paid_instalments = None
        self._contract_outstanding_balance = None
        self._releases = None
        self.discriminator = None
        self.paid_instalments = paid_instalments
        self.contract_outstanding_balance = contract_outstanding_balance
        self.releases = releases

    @property
    def paid_instalments(self):
        """Gets the paid_instalments of this LoansPayments.  # noqa: E501

        Quantidade total de parcelas pagas do contrato referente à Modalidade de Crédito informada.  # noqa: E501

        :return: The paid_instalments of this LoansPayments.  # noqa: E501
        :rtype: float
        """
        return self._paid_instalments

    @paid_instalments.setter
    def paid_instalments(self, paid_instalments):
        """Sets the paid_instalments of this LoansPayments.

        Quantidade total de parcelas pagas do contrato referente à Modalidade de Crédito informada.  # noqa: E501

        :param paid_instalments: The paid_instalments of this LoansPayments.  # noqa: E501
        :type: float
        """
        if paid_instalments is None:
            raise ValueError("Invalid value for `paid_instalments`, must not be `None`")  # noqa: E501

        self._paid_instalments = paid_instalments

    @property
    def contract_outstanding_balance(self):
        """Gets the contract_outstanding_balance of this LoansPayments.  # noqa: E501

        Valor necessário para o cliente liquidar a dívida.  # noqa: E501

        :return: The contract_outstanding_balance of this LoansPayments.  # noqa: E501
        :rtype: str
        """
        return self._contract_outstanding_balance

    @contract_outstanding_balance.setter
    def contract_outstanding_balance(self, contract_outstanding_balance):
        """Sets the contract_outstanding_balance of this LoansPayments.

        Valor necessário para o cliente liquidar a dívida.  # noqa: E501

        :param contract_outstanding_balance: The contract_outstanding_balance of this LoansPayments.  # noqa: E501
        :type: str
        """
        if contract_outstanding_balance is None:
            raise ValueError("Invalid value for `contract_outstanding_balance`, must not be `None`")  # noqa: E501

        self._contract_outstanding_balance = contract_outstanding_balance

    @property
    def releases(self):
        """Gets the releases of this LoansPayments.  # noqa: E501

        Lista dos pagamentos realizados no período  # noqa: E501

        :return: The releases of this LoansPayments.  # noqa: E501
        :rtype: list[LoansReleases]
        """
        return self._releases

    @releases.setter
    def releases(self, releases):
        """Sets the releases of this LoansPayments.

        Lista dos pagamentos realizados no período  # noqa: E501

        :param releases: The releases of this LoansPayments.  # noqa: E501
        :type: list[LoansReleases]
        """
        if releases is None:
            raise ValueError("Invalid value for `releases`, must not be `None`")  # noqa: E501

        self._releases = releases

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
        if issubclass(LoansPayments, dict):
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
        if not isinstance(other, LoansPayments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
