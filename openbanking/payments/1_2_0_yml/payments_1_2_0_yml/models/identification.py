# coding: utf-8

"""
    API Payment Initiation - Open Banking Brasil

    API de Iniciação de Pagamentos, responsável por viabilizar as operações de iniciação de pagamentos para o Open Banking Brasil. Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API: - `CONTA`, referente às instituições detentoras de conta participantes do Open Banking Brasil; - `PAGTO`, referente às instituições iniciadoras de transação de pagamento de conta participantes do Open Banking Brasil. Os tokens utilizados para consumo dos `endpoints` desta API devem possuir os `scopes` `openid` e `payments`. Esta API não requer a implementação de `permissions` para sua utilização. Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão <a href=\"https://openbanking-brasil.github.io/areadesenvolvedor/#assinaturas\" target=\"_blank\">Assinaturas</a> do guia de segurança.  ## Assinatura de payloads  No contexto da API Payment Initiation, os `payloads` de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora de conta devem estar assinados. Para o processo de assinatura destes `payloads` as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor:  - Certificados exigidos para assinatura de mensagens: [Padrões de certificados digitais Open Banking Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-certificate-standards-1_ID1.md#certificado-de-assinatura-certificadoassinatura)  - Como assinar o payload JWS: [https://openbanking-brasil.github.io/areadesenvolvedor/#como-assinar-o-payload](https://openbanking-brasil.github.io/areadesenvolvedor/#como-assinar-o-payload)  ## Controle de acesso  O endpoint de consulta de pagamento GET /pix/payments/{​​​paymentId}​​​ deve suportar acesso a partir de access_token emitido por meio de um grant_type do tipo `client credentials`, como opção do uso do token vinculado ao consentimento (hybrid flow).  Para evitar vazamento de informação, a detentora deve validar que o pagamento consultado pertence ao ClientId que o criou e, caso haja divergências, retorne um erro HTTP 400.   # noqa: E501

    OpenAPI spec version: 1.2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Identification(object):
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
        'person_type': 'EnumPaymentPersonType',
        'cpf_cnpj': 'str',
        'name': 'str'
    }

    attribute_map = {
        'person_type': 'personType',
        'cpf_cnpj': 'cpfCnpj',
        'name': 'name'
    }

    def __init__(self, person_type=None, cpf_cnpj=None, name=None):  # noqa: E501
        """Identification - a model defined in Swagger"""  # noqa: E501
        self._person_type = None
        self._cpf_cnpj = None
        self._name = None
        self.discriminator = None
        self.person_type = person_type
        self.cpf_cnpj = cpf_cnpj
        self.name = name

    @property
    def person_type(self):
        """Gets the person_type of this Identification.  # noqa: E501


        :return: The person_type of this Identification.  # noqa: E501
        :rtype: EnumPaymentPersonType
        """
        return self._person_type

    @person_type.setter
    def person_type(self, person_type):
        """Sets the person_type of this Identification.


        :param person_type: The person_type of this Identification.  # noqa: E501
        :type: EnumPaymentPersonType
        """
        if person_type is None:
            raise ValueError("Invalid value for `person_type`, must not be `None`")  # noqa: E501

        self._person_type = person_type

    @property
    def cpf_cnpj(self):
        """Gets the cpf_cnpj of this Identification.  # noqa: E501

        Identificação da pessoa envolvida na transação.   Preencher com o CPF ou CNPJ, de acordo com o valor escolhido no campo type.   O CPF será utilizado com 11 números e deverá ser informado sem pontos ou traços.   O CNPJ será utilizado com 14 números e deverá ser informado sem pontos ou traços.   # noqa: E501

        :return: The cpf_cnpj of this Identification.  # noqa: E501
        :rtype: str
        """
        return self._cpf_cnpj

    @cpf_cnpj.setter
    def cpf_cnpj(self, cpf_cnpj):
        """Sets the cpf_cnpj of this Identification.

        Identificação da pessoa envolvida na transação.   Preencher com o CPF ou CNPJ, de acordo com o valor escolhido no campo type.   O CPF será utilizado com 11 números e deverá ser informado sem pontos ou traços.   O CNPJ será utilizado com 14 números e deverá ser informado sem pontos ou traços.   # noqa: E501

        :param cpf_cnpj: The cpf_cnpj of this Identification.  # noqa: E501
        :type: str
        """
        if cpf_cnpj is None:
            raise ValueError("Invalid value for `cpf_cnpj`, must not be `None`")  # noqa: E501

        self._cpf_cnpj = cpf_cnpj

    @property
    def name(self):
        """Gets the name of this Identification.  # noqa: E501

        Em caso de pessoa natural deve ser informado o nome completo do titular da conta do recebedor.   Em caso de pessoa jurídica deve ser informada a razão social ou o nome fantasia da conta do recebedor.   # noqa: E501

        :return: The name of this Identification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Identification.

        Em caso de pessoa natural deve ser informado o nome completo do titular da conta do recebedor.   Em caso de pessoa jurídica deve ser informada a razão social ou o nome fantasia da conta do recebedor.   # noqa: E501

        :param name: The name of this Identification.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(Identification, dict):
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
        if not isinstance(other, Identification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
