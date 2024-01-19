# coding: utf-8

"""
    API Payment Initiation - Open Banking Brasil

    API de Iniciação de Pagamentos, responsável por viabilizar as operações de iniciação de pagamentos para o Open Banking Brasil.   Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API:  - `CONTA`, referente às instituições detentoras de conta participantes do Open Banking Brasil; - `PAGTO`, referente às instituições iniciadoras de transação de pagamento de conta participantes do Open Banking Brasil.    Os tokens utilizados para consumo dos `endpoints` desta API devem possuir os `scopes` `openid` e `payments`.   Esta API não requer a implementação de `permissions` para sua utilização.   Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão <a href=\"https://openbanking-brasil.github.io/areadesenvolvedor/#assinaturas\" target=\"_blank\">Assinaturas</a> do guia de segurança.  ## Assinatura de payloads  No contexto da API Payment Initiation, os `payloads` de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora  de conta devem estar assinados. Para o processo de assinatura destes `payloads` as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor:   - Certificados exigidos para assinatura de mensagens:   [Padrões de certificados digitais Open Banking Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-certificate-standards-1_ID1.md#certificado-de-assinatura-certificadoassinatura)  - Algoritmos usados para assinatura de mensagens `JWS`:   [Perfil de segurança FAPI - Open Banking Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-financial-api-1_ID1.md#algorithm-considerations)  - Mensagens assinadas, `JWS` e `JWKS`:   [Guia de usuário (Receptoras e iniciadoras de pagamento)](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/tpp-user-guide.md#143-what-is-a-jwt-jwe-jws-and-jwk)    ## Controle de acesso    O endpoint de consulta de pagamento GET /pix/payments/{​​​paymentId}​​​ deve suportar acesso a partir de access_token emitido por meio de um grant_type do tipo `client credentials`, como opção do uso do token vinculado ao consentimento (hybrid flow).    Para evitar vazamento de informação, a detentora deve validar que o pagamento consultado pertence ao ClientId que o criou e, caso haja divergências, retorne um erro HTTP 400.       # noqa: E501

    OpenAPI spec version: 1.0.0-rc5.5
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PaymentConsent(object):
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
        'type': 'str',
        '_date': 'date',
        'currency': 'str',
        'amount': 'str'
    }

    attribute_map = {
        'type': 'type',
        '_date': 'date',
        'currency': 'currency',
        'amount': 'amount'
    }

    def __init__(self, type=None, _date=None, currency=None, amount=None):  # noqa: E501
        """PaymentConsent - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self.__date = None
        self._currency = None
        self._amount = None
        self.discriminator = None
        self.type = type
        self._date = _date
        self.currency = currency
        self.amount = amount

    @property
    def type(self):
        """Gets the type of this PaymentConsent.  # noqa: E501

        Este campo define o tipo de pagamento que será iniciado após a autorização do consentimento.   # noqa: E501

        :return: The type of this PaymentConsent.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PaymentConsent.

        Este campo define o tipo de pagamento que será iniciado após a autorização do consentimento.   # noqa: E501

        :param type: The type of this PaymentConsent.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["PIX"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def _date(self):
        """Gets the _date of this PaymentConsent.  # noqa: E501

        Data do pagamento, conforme especificação RFC-3339.  # noqa: E501

        :return: The _date of this PaymentConsent.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this PaymentConsent.

        Data do pagamento, conforme especificação RFC-3339.  # noqa: E501

        :param _date: The _date of this PaymentConsent.  # noqa: E501
        :type: date
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def currency(self):
        """Gets the currency of this PaymentConsent.  # noqa: E501

        Código da moeda nacional segundo modelo ISO-4217, ou seja, 'BRL'.  Todos os valores monetários informados estão representados com a moeda vigente do Brasil.   # noqa: E501

        :return: The currency of this PaymentConsent.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PaymentConsent.

        Código da moeda nacional segundo modelo ISO-4217, ou seja, 'BRL'.  Todos os valores monetários informados estão representados com a moeda vigente do Brasil.   # noqa: E501

        :param currency: The currency of this PaymentConsent.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def amount(self):
        """Gets the amount of this PaymentConsent.  # noqa: E501

        Valor da transação com 2 casas decimais.   # noqa: E501

        :return: The amount of this PaymentConsent.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentConsent.

        Valor da transação com 2 casas decimais.   # noqa: E501

        :param amount: The amount of this PaymentConsent.  # noqa: E501
        :type: str
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
        if issubclass(PaymentConsent, dict):
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
        if not isinstance(other, PaymentConsent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
