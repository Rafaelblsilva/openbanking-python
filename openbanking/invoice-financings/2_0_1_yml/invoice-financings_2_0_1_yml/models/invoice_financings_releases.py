# coding: utf-8

"""
    API Invoice-financings - Open Finance Brasil

    API de informações de operações de antecipação de recebíveis do Open Finance Brasil – Fase 2. API que retorna informações de operações de crédito do tipo antecipação de recebíveis – direitos creditórios descontados - mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos, amortizações, garantias, encargos e taxas de juros remuneratórios.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ### Observação:   - No endpoint `/contracts/{contratId}/payments` a paginação ocorrerá sob os dados contidos no campo `releases` do tipo lista.     ## Permissions necessárias para a API Invoice-financings  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **INVOICE_FINANCINGS_READ** ### `/contracts/{contractId}`   - permissions:     - GET: **INVOICE_FINANCINGS_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **INVOICE_FINANCINGS_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **INVOICE_FINANCINGS_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **INVOICE_FINANCINGS_PAYMENTS_READ**   # noqa: E501

    OpenAPI spec version: 2.0.1
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InvoiceFinancingsReleases(object):
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
        'payment_id': 'str',
        'is_over_parcel_payment': 'bool',
        'instalment_id': 'str',
        'paid_date': 'date',
        'currency': 'str',
        'paid_amount': 'str',
        'over_parcel': 'InvoiceFinancingsReleasesOverParcel'
    }

    attribute_map = {
        'payment_id': 'paymentId',
        'is_over_parcel_payment': 'isOverParcelPayment',
        'instalment_id': 'instalmentId',
        'paid_date': 'paidDate',
        'currency': 'currency',
        'paid_amount': 'paidAmount',
        'over_parcel': 'overParcel'
    }

    def __init__(self, payment_id=None, is_over_parcel_payment=None, instalment_id=None, paid_date=None, currency=None, paid_amount=None, over_parcel=None):  # noqa: E501
        """InvoiceFinancingsReleases - a model defined in Swagger"""  # noqa: E501
        self._payment_id = None
        self._is_over_parcel_payment = None
        self._instalment_id = None
        self._paid_date = None
        self._currency = None
        self._paid_amount = None
        self._over_parcel = None
        self.discriminator = None
        if payment_id is not None:
            self.payment_id = payment_id
        self.is_over_parcel_payment = is_over_parcel_payment
        if instalment_id is not None:
            self.instalment_id = instalment_id
        self.paid_date = paid_date
        self.currency = currency
        self.paid_amount = paid_amount
        if over_parcel is not None:
            self.over_parcel = over_parcel

    @property
    def payment_id(self):
        """Gets the payment_id of this InvoiceFinancingsReleases.  # noqa: E501

        Identificador de pagamento de responsabilidade de cada Instituição transmissora.  # noqa: E501

        :return: The payment_id of this InvoiceFinancingsReleases.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this InvoiceFinancingsReleases.

        Identificador de pagamento de responsabilidade de cada Instituição transmissora.  # noqa: E501

        :param payment_id: The payment_id of this InvoiceFinancingsReleases.  # noqa: E501
        :type: str
        """

        self._payment_id = payment_id

    @property
    def is_over_parcel_payment(self):
        """Gets the is_over_parcel_payment of this InvoiceFinancingsReleases.  # noqa: E501

        Identifica se é um pagamento pactuado (false) ou avulso (true).  # noqa: E501

        :return: The is_over_parcel_payment of this InvoiceFinancingsReleases.  # noqa: E501
        :rtype: bool
        """
        return self._is_over_parcel_payment

    @is_over_parcel_payment.setter
    def is_over_parcel_payment(self, is_over_parcel_payment):
        """Sets the is_over_parcel_payment of this InvoiceFinancingsReleases.

        Identifica se é um pagamento pactuado (false) ou avulso (true).  # noqa: E501

        :param is_over_parcel_payment: The is_over_parcel_payment of this InvoiceFinancingsReleases.  # noqa: E501
        :type: bool
        """
        if is_over_parcel_payment is None:
            raise ValueError("Invalid value for `is_over_parcel_payment`, must not be `None`")  # noqa: E501

        self._is_over_parcel_payment = is_over_parcel_payment

    @property
    def instalment_id(self):
        """Gets the instalment_id of this InvoiceFinancingsReleases.  # noqa: E501

        Identificador de parcela, de responsabilidade de cada Instituição transmissora.   [Restrição] Informação de envio obrigatório quando isOverParcelPayment tiver o valor FALSE.   # noqa: E501

        :return: The instalment_id of this InvoiceFinancingsReleases.  # noqa: E501
        :rtype: str
        """
        return self._instalment_id

    @instalment_id.setter
    def instalment_id(self, instalment_id):
        """Sets the instalment_id of this InvoiceFinancingsReleases.

        Identificador de parcela, de responsabilidade de cada Instituição transmissora.   [Restrição] Informação de envio obrigatório quando isOverParcelPayment tiver o valor FALSE.   # noqa: E501

        :param instalment_id: The instalment_id of this InvoiceFinancingsReleases.  # noqa: E501
        :type: str
        """

        self._instalment_id = instalment_id

    @property
    def paid_date(self):
        """Gets the paid_date of this InvoiceFinancingsReleases.  # noqa: E501

        Data efetiva do pagamento referente ao contrato da modalidade de crédito consultada, conforme especificação RFC-3339. p.ex. 2014-03-19  # noqa: E501

        :return: The paid_date of this InvoiceFinancingsReleases.  # noqa: E501
        :rtype: date
        """
        return self._paid_date

    @paid_date.setter
    def paid_date(self, paid_date):
        """Sets the paid_date of this InvoiceFinancingsReleases.

        Data efetiva do pagamento referente ao contrato da modalidade de crédito consultada, conforme especificação RFC-3339. p.ex. 2014-03-19  # noqa: E501

        :param paid_date: The paid_date of this InvoiceFinancingsReleases.  # noqa: E501
        :type: date
        """
        if paid_date is None:
            raise ValueError("Invalid value for `paid_date`, must not be `None`")  # noqa: E501

        self._paid_date = paid_date

    @property
    def currency(self):
        """Gets the currency of this InvoiceFinancingsReleases.  # noqa: E501

        Moeda referente ao valor monetário informado, segundo modelo ISO-4217. p.ex. ''BRL'_'_'. Todos os valores monetários informados estão representados com a moeda vigente do Brasil.   # noqa: E501

        :return: The currency of this InvoiceFinancingsReleases.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InvoiceFinancingsReleases.

        Moeda referente ao valor monetário informado, segundo modelo ISO-4217. p.ex. ''BRL'_'_'. Todos os valores monetários informados estão representados com a moeda vigente do Brasil.   # noqa: E501

        :param currency: The currency of this InvoiceFinancingsReleases.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def paid_amount(self):
        """Gets the paid_amount of this InvoiceFinancingsReleases.  # noqa: E501

        Valor do pagamento referente ao  contrato da modalidade de crédito consultada. Expresso em valor monetário com no mínimo 2 casas e no máximo 4 casas decimais.   # noqa: E501

        :return: The paid_amount of this InvoiceFinancingsReleases.  # noqa: E501
        :rtype: str
        """
        return self._paid_amount

    @paid_amount.setter
    def paid_amount(self, paid_amount):
        """Sets the paid_amount of this InvoiceFinancingsReleases.

        Valor do pagamento referente ao  contrato da modalidade de crédito consultada. Expresso em valor monetário com no mínimo 2 casas e no máximo 4 casas decimais.   # noqa: E501

        :param paid_amount: The paid_amount of this InvoiceFinancingsReleases.  # noqa: E501
        :type: str
        """
        if paid_amount is None:
            raise ValueError("Invalid value for `paid_amount`, must not be `None`")  # noqa: E501

        self._paid_amount = paid_amount

    @property
    def over_parcel(self):
        """Gets the over_parcel of this InvoiceFinancingsReleases.  # noqa: E501


        :return: The over_parcel of this InvoiceFinancingsReleases.  # noqa: E501
        :rtype: InvoiceFinancingsReleasesOverParcel
        """
        return self._over_parcel

    @over_parcel.setter
    def over_parcel(self, over_parcel):
        """Sets the over_parcel of this InvoiceFinancingsReleases.


        :param over_parcel: The over_parcel of this InvoiceFinancingsReleases.  # noqa: E501
        :type: InvoiceFinancingsReleasesOverParcel
        """

        self._over_parcel = over_parcel

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
        if issubclass(InvoiceFinancingsReleases, dict):
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
        if not isinstance(other, InvoiceFinancingsReleases):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
