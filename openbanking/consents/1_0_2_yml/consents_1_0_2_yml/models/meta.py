# coding: utf-8

"""
    API Consents - Open Banking Brasil

    API que trata da criação, consulta e revogação de consentimentos para o Open Banking Brasil Fase 2 - customer-data.   Não possui segregação entre pessoa natural e pessoa jurídica.      # Orientações importantes A API Consents trata dos consentimentos exclusivamente para a fase 2 do Open Banking Brasil. - As informações da instituição receptora não trafegam na API Consents – a autenticação da receptora se dá através do [DCR](https://openbanking-brasil.github.io/specs-seguranca/open-banking-brasil-dynamic-client-registration-1_ID1.html).    - Na chamada para a criação do consentimento deve-se utilizar um token gerado via `client_credentials`. - Após o `POST` de criação do consentimento, o `STATUS` devolvido na resposta deverá ser `AWAITING_AUTHORISATION`. - O `STATUS` será alterado para `AUTHORISED` somente após autenticação e confirmação por parte do usuário na instituição transmissora dos dados. - Todas as datas trafegadas nesta API seguem o padrão da [RFC3339](https://tools.ietf.org/html/rfc3339) e formato \"zulu\". - A descrição do fluxo de consentimento encontra-se disponível no [Portal do desenvolvedor](https://openbanking-brasil.github.io/areadesenvolvedor/#em-revisao-fluxo-de-consentimento). - O arquivo com o mapeamento completo entre `Roles`, `scopes` e `permissions` está disponibilizado no Portal do desenvolvedor, no mesmo item acima - descrição do fluxo de consentimento. - É de responsabilidade da instituição receptora de dados, no pedido de criação do consentimento, o envio de todas as `permissions` correspondentes aos agrupamentos de dados selecionados pelo cliente e necessárias às consultas nos endpoints de cada uma das APIs de dados.        # noqa: E501

    OpenAPI spec version: 1.0.2
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
