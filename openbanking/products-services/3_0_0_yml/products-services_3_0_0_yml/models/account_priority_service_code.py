# coding: utf-8

"""
    API's OpenData do Open Finance Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AccountPriorityServiceCode(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CADASTRO = "CADASTRO"
    _2_VIA_CARTAO_DEBITO = "2_VIA_CARTAO_DEBITO"
    _2_VIA_CARTAO_POUPANCA = "2_VIA_CARTAO_POUPANCA"
    EXCLUSAO_CCF = "EXCLUSAO_CCF"
    SUSTACAO_REVOGACAO = "SUSTACAO_REVOGACAO"
    FOLHA_CHEQUE = "FOLHA_CHEQUE"
    CHEQUE_ADMINISTRATIVO = "CHEQUE_ADMINISTRATIVO"
    CHEQUE_VISADO = "CHEQUE_VISADO"
    SAQUE_PESSOAL = "SAQUE_PESSOAL"
    SAQUE_TERMINAL = "SAQUE_TERMINAL"
    SAQUE_CORRESPONDENTE = "SAQUE_CORRESPONDENTE"
    DEPOSITO_IDENTIFICADO = "DEPOSITO_IDENTIFICADO"
    EXTRATO_MES_P = "EXTRATO_MES_P"
    EXTRATO_MES_E = "EXTRATO_MES_E"
    EXTRATO_MES_C = "EXTRATO_MES_C"
    EXTRATO_MOVIMENTO_P = "EXTRATO_MOVIMENTO_P"
    EXTRATO_MOVIMENTO_E = "EXTRATO_MOVIMENTO_E"
    EXTRATO_MOVIMENTO_C = "EXTRATO_MOVIMENTO_C"
    MICROFILME = "MICROFILME"
    DOC_PESSOAL = "DOC_PESSOAL"
    DOC_ELETRONICO = "DOC_ELETRONICO"
    DOC_INTERNET = "DOC_INTERNET"
    TED_PESSOAL = "TED_PESSOAL"
    TED_ELETRONICO = "TED_ELETRONICO"
    TED_INTERNET = "TED_INTERNET"
    DOC_TED_AGENDADO_P = "DOC_TED_AGENDADO_P"
    DOC_TED_AGENDADO_E = "DOC_TED_AGENDADO_E"
    DOC_TED_AGENDADO_I = "DOC_TED_AGENDADO_I"
    TRANSF_RECURSO_P = "TRANSF_RECURSO_P"
    TRANSF_RECURSO_E = "TRANSF_RECURSO_E"
    ORDEM_PAGAMENTO = "ORDEM_PAGAMENTO"
    ANUIDADE_NACIONAL = "ANUIDADE_NACIONAL"
    ANUIDADE_INTERNACIONAL = "ANUIDADE_INTERNACIONAL"
    ANUIDADE_DIFERENCIADA = "ANUIDADE_DIFERENCIADA"
    SAQUE_CARTAO_BRASIL = "SAQUE_CARTAO_BRASIL"
    SAQUE_CARTAO_EXTERIOR = "SAQUE_CARTAO_EXTERIOR"
    AVALIACAO_EMERGENCIAL_CREDITO = "AVALIACAO_EMERGENCIAL_CREDITO"
    EMISSAO_SEGUNDA_VIA = "EMISSAO_SEGUNDA_VIA"
    TARIFA_PAGAMENTO_CONTAS = "TARIFA_PAGAMENTO_CONTAS"
    SMS = "SMS"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """AccountPriorityServiceCode - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

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
        if issubclass(AccountPriorityServiceCode, dict):
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
        if not isinstance(other, AccountPriorityServiceCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
