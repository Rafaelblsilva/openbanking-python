# coding: utf-8

"""
    API Payment Initiation - Open Banking Brasil

    API de Iniciação de Pagamentos, responsável por viabilizar as operações de iniciação de pagamentos para o Open Banking Brasil. Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API: - `CONTA`, referente às instituições detentoras de conta participantes do Open Banking Brasil; - `PAGTO`, referente às instituições iniciadoras de transação de pagamento de conta participantes do Open Banking Brasil. Os tokens utilizados para consumo dos `endpoints` desta API devem possuir os `scopes` `openid` e `payments`. Esta API não requer a implementação de `permissions` para sua utilização. Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão <a href=\"https://openbanking-brasil.github.io/areadesenvolvedor/#assinaturas\" target=\"_blank\">Assinaturas</a> do guia de segurança.  ## Assinatura de payloads  No contexto da API Payment Initiation, os `payloads` de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora de conta devem estar assinados. Para o processo de assinatura destes `payloads` as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor:  - Certificados exigidos para assinatura de mensagens: [Padrões de certificados digitais Open Banking Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-certificate-standards-1_ID1.md#certificado-de-assinatura-certificadoassinatura)  - Como assinar o payload JWS: [https://openbanking-brasil.github.io/areadesenvolvedor/#como-assinar-o-payload](https://openbanking-brasil.github.io/areadesenvolvedor/#como-assinar-o-payload)  ## Controle de acesso  O endpoint de consulta de pagamento GET /pix/payments/{​​​paymentId}​​​ deve suportar acesso a partir de access_token emitido por meio de um grant_type do tipo `client credentials`, como opção do uso do token vinculado ao consentimento (hybrid flow).  Para evitar vazamento de informação, a detentora deve validar que o pagamento consultado pertence ao ClientId que o criou e, caso haja divergências, retorne um erro HTTP 400.   # noqa: E501

    OpenAPI spec version: 1.1.0-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreditorAccount(object):
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
        'ispb': 'str',
        'issuer': 'str',
        'number': 'str',
        'account_type': 'EnumAccountPaymentsType'
    }

    attribute_map = {
        'ispb': 'ispb',
        'issuer': 'issuer',
        'number': 'number',
        'account_type': 'accountType'
    }

    def __init__(self, ispb=None, issuer=None, number=None, account_type=None):  # noqa: E501
        """CreditorAccount - a model defined in Swagger"""  # noqa: E501
        self._ispb = None
        self._issuer = None
        self._number = None
        self._account_type = None
        self.discriminator = None
        self.ispb = ispb
        if issuer is not None:
            self.issuer = issuer
        self.number = number
        self.account_type = account_type

    @property
    def ispb(self):
        """Gets the ispb of this CreditorAccount.  # noqa: E501

        Deve ser preenchido com o ISPB (Identificador do Sistema de Pagamentos Brasileiros) do participante do SPI (Sistema de pagamentos instantâneos) somente com números.   # noqa: E501

        :return: The ispb of this CreditorAccount.  # noqa: E501
        :rtype: str
        """
        return self._ispb

    @ispb.setter
    def ispb(self, ispb):
        """Sets the ispb of this CreditorAccount.

        Deve ser preenchido com o ISPB (Identificador do Sistema de Pagamentos Brasileiros) do participante do SPI (Sistema de pagamentos instantâneos) somente com números.   # noqa: E501

        :param ispb: The ispb of this CreditorAccount.  # noqa: E501
        :type: str
        """
        if ispb is None:
            raise ValueError("Invalid value for `ispb`, must not be `None`")  # noqa: E501

        self._ispb = ispb

    @property
    def issuer(self):
        """Gets the issuer of this CreditorAccount.  # noqa: E501

        Código da Agência emissora da conta sem dígito.   (Agência é a dependência destinada ao atendimento aos clientes, ao público em geral e aos associados de cooperativas de crédito,   no exercício de atividades da instituição, não podendo ser móvel ou transitória).   [Restrição] Preenchimento obrigatório para os seguintes tipos de conta: CACC (CONTA_DEPOSITO_A_VISTA), SVGS (CONTA_POUPANCA) e SLRY (CONTA_SALARIO).   # noqa: E501

        :return: The issuer of this CreditorAccount.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this CreditorAccount.

        Código da Agência emissora da conta sem dígito.   (Agência é a dependência destinada ao atendimento aos clientes, ao público em geral e aos associados de cooperativas de crédito,   no exercício de atividades da instituição, não podendo ser móvel ou transitória).   [Restrição] Preenchimento obrigatório para os seguintes tipos de conta: CACC (CONTA_DEPOSITO_A_VISTA), SVGS (CONTA_POUPANCA) e SLRY (CONTA_SALARIO).   # noqa: E501

        :param issuer: The issuer of this CreditorAccount.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def number(self):
        """Gets the number of this CreditorAccount.  # noqa: E501

        Deve ser preenchido com o número da conta do usuário recebedor, com dígito verificador (se este existir),   se houver valor alfanumérico, este deve ser convertido para 0.   # noqa: E501

        :return: The number of this CreditorAccount.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this CreditorAccount.

        Deve ser preenchido com o número da conta do usuário recebedor, com dígito verificador (se este existir),   se houver valor alfanumérico, este deve ser convertido para 0.   # noqa: E501

        :param number: The number of this CreditorAccount.  # noqa: E501
        :type: str
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def account_type(self):
        """Gets the account_type of this CreditorAccount.  # noqa: E501


        :return: The account_type of this CreditorAccount.  # noqa: E501
        :rtype: EnumAccountPaymentsType
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this CreditorAccount.


        :param account_type: The account_type of this CreditorAccount.  # noqa: E501
        :type: EnumAccountPaymentsType
        """
        if account_type is None:
            raise ValueError("Invalid value for `account_type`, must not be `None`")  # noqa: E501

        self._account_type = account_type

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
        if issubclass(CreditorAccount, dict):
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
        if not isinstance(other, CreditorAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
