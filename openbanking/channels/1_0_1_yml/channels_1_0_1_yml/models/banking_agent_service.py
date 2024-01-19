# coding: utf-8

"""
    APIs OpenData do Open Banking Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BankingAgentService(object):
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
        'name': 'str',
        'code': 'str',
        'additional_info': 'str'
    }

    attribute_map = {
        'name': 'name',
        'code': 'code',
        'additional_info': 'additionalInfo'
    }

    def __init__(self, name=None, code=None, additional_info=None):  # noqa: E501
        """BankingAgentService - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._code = None
        self._additional_info = None
        self.discriminator = None
        self.name = name
        self.code = code
        if additional_info is not None:
            self.additional_info = additional_info

    @property
    def name(self):
        """Gets the name of this BankingAgentService.  # noqa: E501

        Relação dos Nomes de serviços prestados pelo Correspondente  # noqa: E501

        :return: The name of this BankingAgentService.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BankingAgentService.

        Relação dos Nomes de serviços prestados pelo Correspondente  # noqa: E501

        :param name: The name of this BankingAgentService.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        allowed_values = ["RECEPCAO_ENCAMINHAMENTO_PROPOSTAS_ABERTURA_CONTAS_DEPOSITOS_VISTA_PRAZO_POUPANCA_MANTIDOS_INSTITUICAO_CONTRATANTE", "REALIZACAO_RECEBIMENTOS_PAGAMENTOS_TRANSFERENCIAS_ELETRONICAS_VISANDO_MOVIMENTACAO_CONTAS_DEPOSITOS_TITULARIDADE_CLIENTES_MANTIDAS_INSTITUICAO_CONTRATANTE", "RECEBIMENTOS_PAGAMENTOS_QUALQUER_NATUREZA_OUTRAS_ATIVIDADES_DECORRENTES_EXECUCAO_CONTRATOS_CONVENIOS_PRESTACAO_SERVICOS", "EXECUCAO_ATIVA_PASSIVA_ORDENS_PAGAMENTO_CURSADAS_INTERMEDIO_INSTITUICAO_CONTRATANTE_SOLICITACAO_CLIENTES_USUARIOS", "RECEPCAO_ENCAMINHAMENTO_PROPOSTAS_OPERACAO_CREDITO_ARRENDAMENTO_MERCANTIL_CONCESSAO_INSTITUICAO_CONTRATANTE", "RECEBIMENTOS_PAGAMENTOS_RELACIONADOS_LETRAS_CAMBIO_ACEITE_INSTITUICAO_CONTRATANTE", "RECEPCAO_ENCAMINHAMENTO_PROPOSTAS_FORNECIMENTO_CARTAO_CREDITO_RESPONSABILIDADE_INSTITUICAO_CONTRATANTE", "REALIZACAO_OPERACOES_CAMBIO_RESPONSABILIDADE_INSTITUICAO_CONTRATANTE", "OUTROS"]  # noqa: E501
        if name not in allowed_values:
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"  # noqa: E501
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def code(self):
        """Gets the code of this BankingAgentService.  # noqa: E501

        > Relação dos Códigos relativos aos serviços prestados pelo Correspondente  * `RECEBE_ENCAMINHA_PROPOSTAS_ABERTURA_CONTAS` - Recepção e encaminhamento de propostas de abertura de contas  * `REALIZA_RECEBIMENTOS_PAGAMENTOS_TRANSFERENCIAS_ELETRONICAS` - Realização de recebimentos, pagamentos e transferências eletrônicas  * `RECEBIMENTOS_PAGAMENTOS_QUALQUER_NATUREZA_EXECUCAO_CONTRATOS_CONVENIO` - Recebimentos e pagamentos de qualquer natureza  * `EXECUCAO_ATIVA_PASSIVA_ORDENS_PAGAMENTO` - Execução ativa e passiva de ordens de pagamento  * `RECEBE_ENCAMINHA_PROPOSTAS_CREDITO_ARRENDAMENTO_MERCANTIL` - Recepção e encaminhamento de propostas de operações de crédito e de arrendamento mercantil  * `RECEBE_PAGAMENTOS_RELACIONADOS_LETRAS_CAMBIO_ACEITE_INSTITUICAO` - Recebimento e pagamentos relacionados a letras de câmbio de aceite da instituição  * `RECEBE_ENCAMINHA_PROPOSTAS_FORNECIMENTO_CARTAO_CREDITO` - Recepção e encaminhamento de propostas de fornecimento de cartões de crédito  * `REALIZA_OPERACOES_CAMBIO` - Realização de operações de câmbio  * `OUTROS` - Outros  # noqa: E501

        :return: The code of this BankingAgentService.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this BankingAgentService.

        > Relação dos Códigos relativos aos serviços prestados pelo Correspondente  * `RECEBE_ENCAMINHA_PROPOSTAS_ABERTURA_CONTAS` - Recepção e encaminhamento de propostas de abertura de contas  * `REALIZA_RECEBIMENTOS_PAGAMENTOS_TRANSFERENCIAS_ELETRONICAS` - Realização de recebimentos, pagamentos e transferências eletrônicas  * `RECEBIMENTOS_PAGAMENTOS_QUALQUER_NATUREZA_EXECUCAO_CONTRATOS_CONVENIO` - Recebimentos e pagamentos de qualquer natureza  * `EXECUCAO_ATIVA_PASSIVA_ORDENS_PAGAMENTO` - Execução ativa e passiva de ordens de pagamento  * `RECEBE_ENCAMINHA_PROPOSTAS_CREDITO_ARRENDAMENTO_MERCANTIL` - Recepção e encaminhamento de propostas de operações de crédito e de arrendamento mercantil  * `RECEBE_PAGAMENTOS_RELACIONADOS_LETRAS_CAMBIO_ACEITE_INSTITUICAO` - Recebimento e pagamentos relacionados a letras de câmbio de aceite da instituição  * `RECEBE_ENCAMINHA_PROPOSTAS_FORNECIMENTO_CARTAO_CREDITO` - Recepção e encaminhamento de propostas de fornecimento de cartões de crédito  * `REALIZA_OPERACOES_CAMBIO` - Realização de operações de câmbio  * `OUTROS` - Outros  # noqa: E501

        :param code: The code of this BankingAgentService.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        allowed_values = ["RECEBE_ENCAMINHA_PROPOSTAS_ABERTURA_CONTAS", "REALIZA_RECEBIMENTOS_PAGAMENTOS_TRANSFERENCIAS_ELETRONICAS", "RECEBIMENTOS_PAGAMENTOS_QUALQUER_NATUREZA_EXECUCAO_CONTRATOS_CONVENIO", "EXECUCAO_ATIVA_PASSIVA_ORDENS_PAGAMENTO", "RECEBE_ENCAMINHA_PROPOSTAS_CREDITO_ARRENDAMENTO_MERCANTIL", "RECEBE_PAGAMENTOS_RELACIONADOS_LETRAS_CAMBIO_ACEITE_INSTITUICAO", "RECEBE_ENCAMINHA_PROPOSTAS_FORNECIMENTO_CARTAO_CREDITO", "REALIZA_OPERACOES_CAMBIO", "OUTROS"]  # noqa: E501
        if code not in allowed_values:
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"  # noqa: E501
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def additional_info(self):
        """Gets the additional_info of this BankingAgentService.  # noqa: E501

        Campo aberto para detalhamento  # noqa: E501

        :return: The additional_info of this BankingAgentService.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this BankingAgentService.

        Campo aberto para detalhamento  # noqa: E501

        :param additional_info: The additional_info of this BankingAgentService.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

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
        if issubclass(BankingAgentService, dict):
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
        if not isinstance(other, BankingAgentService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
