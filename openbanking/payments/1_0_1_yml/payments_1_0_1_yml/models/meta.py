# coding: utf-8

"""
    API Payment Initiation - Open Banking Brasil

    API de Iniciação de Pagamentos, responsável por viabilizar as operações de iniciação de pagamentos para o Open Banking Brasil. Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API: - `CONTA`, referente às instituições detentoras de conta participantes do Open Banking Brasil; - `PAGTO`, referente às instituições iniciadoras de transação de pagamento de conta participantes do Open Banking Brasil. Os tokens utilizados para consumo dos `endpoints` desta API devem possuir os `scopes` `openid` e `payments`. Esta API não requer a implementação de `permissions` para sua utilização. Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão <a href=\"https://openbanking-brasil.github.io/areadesenvolvedor/#assinaturas\" target=\"_blank\">Assinaturas</a> do guia de segurança.  ## Assinatura de payloads  No contexto da API Payment Initiation, os `payloads` de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora de conta devem estar assinados. Para o processo de assinatura destes `payloads` as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor:  - Certificados exigidos para assinatura de mensagens: [Padrões de certificados digitais Open Banking Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-certificate-standards-1_ID1.md#certificado-de-assinatura-certificadoassinatura)  - Como assinar o payload JWS: [https://openbanking-brasil.github.io/areadesenvolvedor/#como-assinar-o-payload](https://openbanking-brasil.github.io/areadesenvolvedor/#como-assinar-o-payload)  ## Controle de acesso  O endpoint de consulta de pagamento GET /pix/payments/{​​​paymentId}​​​ deve suportar acesso a partir de access_token emitido por meio de um grant_type do tipo `client credentials`, como opção do uso do token vinculado ao consentimento (hybrid flow).  Para evitar vazamento de informação, a detentora deve validar que o pagamento consultado pertence ao ClientId que o criou e, caso haja divergências, retorne um erro HTTP 400.   # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Meta(object):
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
        'total_records': 'int',
        'total_pages': 'int',
        'request_date_time': 'datetime'
    }

    attribute_map = {
        'total_records': 'totalRecords',
        'total_pages': 'totalPages',
        'request_date_time': 'requestDateTime'
    }

    def __init__(self, total_records=None, total_pages=None, request_date_time=None):  # noqa: E501
        """Meta - a model defined in Swagger"""  # noqa: E501
        self._total_records = None
        self._total_pages = None
        self._request_date_time = None
        self.discriminator = None
        self.total_records = total_records
        self.total_pages = total_pages
        self.request_date_time = request_date_time

    @property
    def total_records(self):
        """Gets the total_records of this Meta.  # noqa: E501

        Número total de registros no resultado  # noqa: E501

        :return: The total_records of this Meta.  # noqa: E501
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this Meta.

        Número total de registros no resultado  # noqa: E501

        :param total_records: The total_records of this Meta.  # noqa: E501
        :type: int
        """
        if total_records is None:
            raise ValueError("Invalid value for `total_records`, must not be `None`")  # noqa: E501

        self._total_records = total_records

    @property
    def total_pages(self):
        """Gets the total_pages of this Meta.  # noqa: E501

        Número total de páginas no resultado  # noqa: E501

        :return: The total_pages of this Meta.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this Meta.

        Número total de páginas no resultado  # noqa: E501

        :param total_pages: The total_pages of this Meta.  # noqa: E501
        :type: int
        """
        if total_pages is None:
            raise ValueError("Invalid value for `total_pages`, must not be `None`")  # noqa: E501

        self._total_pages = total_pages

    @property
    def request_date_time(self):
        """Gets the request_date_time of this Meta.  # noqa: E501

        Data e hora da consulta, conforme especificação RFC-3339, formato UTC.  # noqa: E501

        :return: The request_date_time of this Meta.  # noqa: E501
        :rtype: datetime
        """
        return self._request_date_time

    @request_date_time.setter
    def request_date_time(self, request_date_time):
        """Sets the request_date_time of this Meta.

        Data e hora da consulta, conforme especificação RFC-3339, formato UTC.  # noqa: E501

        :param request_date_time: The request_date_time of this Meta.  # noqa: E501
        :type: datetime
        """
        if request_date_time is None:
            raise ValueError("Invalid value for `request_date_time`, must not be `None`")  # noqa: E501

        self._request_date_time = request_date_time

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
        if issubclass(Meta, dict):
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
        if not isinstance(other, Meta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
