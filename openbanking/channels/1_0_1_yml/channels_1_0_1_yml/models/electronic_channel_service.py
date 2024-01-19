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

class ElectronicChannelService(object):
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
        """ElectronicChannelService - a model defined in Swagger"""  # noqa: E501
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
        """Gets the name of this ElectronicChannelService.  # noqa: E501

        Nome dos Serviços efetivamente prestados pelo Canal de Atendimento  # noqa: E501

        :return: The name of this ElectronicChannelService.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ElectronicChannelService.

        Nome dos Serviços efetivamente prestados pelo Canal de Atendimento  # noqa: E501

        :param name: The name of this ElectronicChannelService.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        allowed_values = ["ABERTURA_CONTAS_DEPOSITOS_OU_PAGAMENTO_PRE_PAGA", "SAQUE_MOEDA_EM_ESPECIE", "RECEBIMENTOS_PAGAMENTOS_QUALQUER_NATUREZA", "TRANSFERENCIAS_ELETRONICAS_VISANDO_MOVIMENTACAO_CONTAS_DEPOSITOS_OU_PAGAMENTO_TITULARIDADE_CLIENTES", "CONSULTA_SALDOS_EXTRATOS_CONTAS_DEPOSITOS_CONTAS_PAGAMENTOS", "APLICACOES_RESGATES_INVESTIMENTOS", "EXECUCAO_ATIVA_PASSIVA_ORDENS_PAGAMENTO_SOLICITACAO_CLIENTES_USUARIOS", "DEPOSITOS_MOEDA_ESPECIE_CHEQUE", "OPERACOES_CREDITO_BEM_COMO_OUTROS_SERVICOS_PRESTADOS_ACOMPANHAMENTO_OPERACAO", "CARTAO_CREDITO", "SEGUROS", "OPERACOES_ARRENDAMENTO_MERCANTIL", "ABERTURA_CONTA_PAGAMENTO_POS_PAGA", "COMPRA_VENDA_MOEDA_ESTRANGEIRA_ESPECIE", "COMPRA_VENDA_CHEQUE_CHEQUE_VIAGEM_BEM_COMO_CARGA_MOEDA_ESTRANGEIRA_CARTAO_PRE_PAGO", "COMPRA_VENDA_OURO", "OUTROS_PRODUTOS_SERVICOS", "CANCELAMENTO", "INFORMACOES", "RECLAMACOES"]  # noqa: E501
        if name not in allowed_values:
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"  # noqa: E501
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def code(self):
        """Gets the code of this ElectronicChannelService.  # noqa: E501

        Código dos Serviços efetivamente prestados pelo Canal de Atendimento  # noqa: E501

        :return: The code of this ElectronicChannelService.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ElectronicChannelService.

        Código dos Serviços efetivamente prestados pelo Canal de Atendimento  # noqa: E501

        :param code: The code of this ElectronicChannelService.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        allowed_values = ["ABRE_CONTA_DEPOSITO_OU_PRE_PAGA", "SAQUE_MOEDA_ESPECIE", "RECEBE_PAGA_QUALQUER_NATUREZA", "TRANSFERENCIAS_ELETRONICAS_MOVIMENTA_CONTAS_DEPOSITOS_OU_PAGTO_TITULARES_CLIENTES", "CONSULTA_SALDOS_EXTRATOS_CONTAS_DEPOSITOS_PAGTOS", "APLICA_RESGATA_INVESTIMENTOS", "EXECUCAO_ATIVA_PASSIVA_ORDENS_PAGTO", "DEPOSITO_MOEDA_ESPECIE_CHEQUE", "OPERA_CREDITO_OUTROS_SERVICOS_ACOMPANHA_OPERACAO", "CARTAO_CREDITO", "SEGUROS", "OPERA_ARRENDAMENTO_MERCANTIL", "ABERTURA_CONTA_PAGAMENTO_POS_PAGA", "COMPRA_VENDA_MOEDA_ESTRANGEIRA_ESPECIE", "COMPRA_VENDA_CHEQUE_CHEQUE_VIAGEM_CARGA_MOEDA_ESTRANGEIRA_CARTAO_PRE_PAGO", "COMPRA_VENDA_OURO", "OUTROS_PRODUTOS_SERVICOS", "CANCELAMENTO", "INFORMACOES", "RECLAMACOES"]  # noqa: E501
        if code not in allowed_values:
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"  # noqa: E501
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def additional_info(self):
        """Gets the additional_info of this ElectronicChannelService.  # noqa: E501

        Texto livre para complementar informação relativa ao Serviço disponível, quando for selecionada a opção 'OUTROS_PRODUTOS_SERVICOS'  # noqa: E501

        :return: The additional_info of this ElectronicChannelService.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this ElectronicChannelService.

        Texto livre para complementar informação relativa ao Serviço disponível, quando for selecionada a opção 'OUTROS_PRODUTOS_SERVICOS'  # noqa: E501

        :param additional_info: The additional_info of this ElectronicChannelService.  # noqa: E501
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
        if issubclass(ElectronicChannelService, dict):
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
        if not isinstance(other, ElectronicChannelService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
