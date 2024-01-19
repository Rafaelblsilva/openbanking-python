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

class ResponseConsent(object):
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
        'data': 'ResponseConsentData',
        'links': 'Links',
        'meta': 'Meta'
    }

    attribute_map = {
        'data': 'data',
        'links': 'links',
        'meta': 'meta'
    }

    def __init__(self, data=None, links=None, meta=None):  # noqa: E501
        """ResponseConsent - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._links = None
        self._meta = None
        self.discriminator = None
        self.data = data
        if links is not None:
            self.links = links
        if meta is not None:
            self.meta = meta

    @property
    def data(self):
        """Gets the data of this ResponseConsent.  # noqa: E501


        :return: The data of this ResponseConsent.  # noqa: E501
        :rtype: ResponseConsentData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ResponseConsent.


        :param data: The data of this ResponseConsent.  # noqa: E501
        :type: ResponseConsentData
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def links(self):
        """Gets the links of this ResponseConsent.  # noqa: E501


        :return: The links of this ResponseConsent.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ResponseConsent.


        :param links: The links of this ResponseConsent.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def meta(self):
        """Gets the meta of this ResponseConsent.  # noqa: E501


        :return: The meta of this ResponseConsent.  # noqa: E501
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ResponseConsent.


        :param meta: The meta of this ResponseConsent.  # noqa: E501
        :type: Meta
        """

        self._meta = meta

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
        if issubclass(ResponseConsent, dict):
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
        if not isinstance(other, ResponseConsent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other