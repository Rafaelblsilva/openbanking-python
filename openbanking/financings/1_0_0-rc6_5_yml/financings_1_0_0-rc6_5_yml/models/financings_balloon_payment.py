# coding: utf-8

"""
    API Financings - Open Banking Brasil

    API de informações de operações de financiamentos do Open Banking Brasil – Fase 2. API que retorna informações de operações de crédito do tipo financiamento, mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos, amortizações, garantias, encargos e taxas de juros remuneratórios.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Financings  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **FINANCINGS_READ** ### `/contracts/{contractId}`   - permissions:     - GET **FINANCINGS_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **FINANCINGS_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **FINANCINGS_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **FINANCINGS_PAYMENTS_READ**   # noqa: E501

    OpenAPI spec version: 1.0.0-rc6.5
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FinancingsBalloonPayment(object):
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
        'due_date': 'date',
        'currency': 'str',
        'amount': 'float'
    }

    attribute_map = {
        'due_date': 'dueDate',
        'currency': 'currency',
        'amount': 'amount'
    }

    def __init__(self, due_date=None, currency=None, amount=None):  # noqa: E501
        """FinancingsBalloonPayment - a model defined in Swagger"""  # noqa: E501
        self._due_date = None
        self._currency = None
        self._amount = None
        self.discriminator = None
        self.due_date = due_date
        self.currency = currency
        self.amount = amount

    @property
    def due_date(self):
        """Gets the due_date of this FinancingsBalloonPayment.  # noqa: E501

        Data de vencimento da parcela não regular  a vencer do contrato da modalidade de crédito consultada, conforme especificação RFC-3339. p.ex. 2014-03-19  # noqa: E501

        :return: The due_date of this FinancingsBalloonPayment.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this FinancingsBalloonPayment.

        Data de vencimento da parcela não regular  a vencer do contrato da modalidade de crédito consultada, conforme especificação RFC-3339. p.ex. 2014-03-19  # noqa: E501

        :param due_date: The due_date of this FinancingsBalloonPayment.  # noqa: E501
        :type: date
        """
        if due_date is None:
            raise ValueError("Invalid value for `due_date`, must not be `None`")  # noqa: E501

        self._due_date = due_date

    @property
    def currency(self):
        """Gets the currency of this FinancingsBalloonPayment.  # noqa: E501

        Moeda referente ao valor monetário informado, segundo modelo ISO-4217. p.ex. 'BRL'  Todos os valores monetários informados estão representados com a moeda vigente do Brasil   # noqa: E501

        :return: The currency of this FinancingsBalloonPayment.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this FinancingsBalloonPayment.

        Moeda referente ao valor monetário informado, segundo modelo ISO-4217. p.ex. 'BRL'  Todos os valores monetários informados estão representados com a moeda vigente do Brasil   # noqa: E501

        :param currency: The currency of this FinancingsBalloonPayment.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def amount(self):
        """Gets the amount of this FinancingsBalloonPayment.  # noqa: E501

        Valor monetário da parcela não regular a vencer. Expresso em valor monetário com 4 casas decimais.  # noqa: E501

        :return: The amount of this FinancingsBalloonPayment.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this FinancingsBalloonPayment.

        Valor monetário da parcela não regular a vencer. Expresso em valor monetário com 4 casas decimais.  # noqa: E501

        :param amount: The amount of this FinancingsBalloonPayment.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

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
        if issubclass(FinancingsBalloonPayment, dict):
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
        if not isinstance(other, FinancingsBalloonPayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
