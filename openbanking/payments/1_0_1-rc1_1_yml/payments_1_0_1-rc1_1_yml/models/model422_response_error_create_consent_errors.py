# coding: utf-8

"""
    API Payment Initiation - Open Banking Brasil

    API de Iniciação de Pagamentos, responsável por viabilizar as operações de iniciação de pagamentos para o Open Banking Brasil.   Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API:  - `CONTA`, referente às instituições detentoras de conta participantes do Open Banking Brasil; - `PAGTO`, referente às instituições iniciadoras de transação de pagamento de conta participantes do Open Banking Brasil.    Os tokens utilizados para consumo dos `endpoints` desta API devem possuir os `scopes` `openid` e `payments`.   Esta API não requer a implementação de `permissions` para sua utilização.   Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão <a href=\"https://openbanking-brasil.github.io/areadesenvolvedor/#assinaturas\" target=\"_blank\">Assinaturas</a> do guia de segurança.  ## Assinatura de payloads  No contexto da API Payment Initiation, os `payloads` de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora  de conta devem estar assinados. Para o processo de assinatura destes `payloads` as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor:   - Certificados exigidos para assinatura de mensagens:   [Padrões de certificados digitais Open Banking Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-certificate-standards-1_ID1.md#certificado-de-assinatura-certificadoassinatura)  - Como assinar o payload JWS: [https://openbanking-brasil.github.io/areadesenvolvedor/#como-assinar-o-payload](https://openbanking-brasil.github.io/areadesenvolvedor/#como-assinar-o-payload)  ## Controle de acesso    O endpoint de consulta de pagamento GET /pix/payments/{​​​paymentId}​​​ deve suportar acesso a partir de access_token emitido por meio de um grant_type do tipo `client credentials`, como opção do uso do token vinculado ao consentimento (hybrid flow).    Para evitar vazamento de informação, a detentora deve validar que o pagamento consultado pertence ao ClientId que o criou e, caso haja divergências, retorne um erro HTTP 400.       # noqa: E501

    OpenAPI spec version: 1.0.1-rc1.1
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Model422ResponseErrorCreateConsentErrors(object):
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
        'code': 'EnumErrorsCreateConsent',
        'title': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'code': 'code',
        'title': 'title',
        'detail': 'detail'
    }

    def __init__(self, code=None, title=None, detail=None):  # noqa: E501
        """Model422ResponseErrorCreateConsentErrors - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._title = None
        self._detail = None
        self.discriminator = None
        self.code = code
        self.title = title
        self.detail = detail

    @property
    def code(self):
        """Gets the code of this Model422ResponseErrorCreateConsentErrors.  # noqa: E501


        :return: The code of this Model422ResponseErrorCreateConsentErrors.  # noqa: E501
        :rtype: EnumErrorsCreateConsent
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Model422ResponseErrorCreateConsentErrors.


        :param code: The code of this Model422ResponseErrorCreateConsentErrors.  # noqa: E501
        :type: EnumErrorsCreateConsent
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def title(self):
        """Gets the title of this Model422ResponseErrorCreateConsentErrors.  # noqa: E501

        Título específico do erro reportado, de acordo com o código enviado:   • FORMA_PGTO_INVALIDA: Forma de pagamento inválida.   • DATA_PGTO_INVALIDA: Data de pagamento inválida.  • DETALHE_PGTO_INVALIDO: Detalhe do pagamento inválido. • NAO_INFORMADO: Não informado.       # noqa: E501

        :return: The title of this Model422ResponseErrorCreateConsentErrors.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Model422ResponseErrorCreateConsentErrors.

        Título específico do erro reportado, de acordo com o código enviado:   • FORMA_PGTO_INVALIDA: Forma de pagamento inválida.   • DATA_PGTO_INVALIDA: Data de pagamento inválida.  • DETALHE_PGTO_INVALIDO: Detalhe do pagamento inválido. • NAO_INFORMADO: Não informado.       # noqa: E501

        :param title: The title of this Model422ResponseErrorCreateConsentErrors.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def detail(self):
        """Gets the detail of this Model422ResponseErrorCreateConsentErrors.  # noqa: E501

        Descrição específica do erro de acordo com o código reportado:   • FORMA_PGTO_INVALIDA – Meio de pagamento inválido.   • DATA_PGTO_INVALIDA – Data de pagamento inválida no contexto, por exemplo, data no passado. Para pagamentos únicos deve ser informada a data atual, do dia corrente.   • DETALHE_PGTO_INVALIDO: O campo [nome_campo] não atende os requisitos de preenchimento.   • NAO_INFORMADO – Não reportado/identificado pela instituição detentora de conta.     # noqa: E501

        :return: The detail of this Model422ResponseErrorCreateConsentErrors.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this Model422ResponseErrorCreateConsentErrors.

        Descrição específica do erro de acordo com o código reportado:   • FORMA_PGTO_INVALIDA – Meio de pagamento inválido.   • DATA_PGTO_INVALIDA – Data de pagamento inválida no contexto, por exemplo, data no passado. Para pagamentos únicos deve ser informada a data atual, do dia corrente.   • DETALHE_PGTO_INVALIDO: O campo [nome_campo] não atende os requisitos de preenchimento.   • NAO_INFORMADO – Não reportado/identificado pela instituição detentora de conta.     # noqa: E501

        :param detail: The detail of this Model422ResponseErrorCreateConsentErrors.  # noqa: E501
        :type: str
        """
        if detail is None:
            raise ValueError("Invalid value for `detail`, must not be `None`")  # noqa: E501

        self._detail = detail

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
        if issubclass(Model422ResponseErrorCreateConsentErrors, dict):
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
        if not isinstance(other, Model422ResponseErrorCreateConsentErrors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
