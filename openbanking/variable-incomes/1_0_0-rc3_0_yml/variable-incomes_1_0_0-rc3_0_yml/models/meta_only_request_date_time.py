# coding: utf-8

"""
    API Variable Incomes - Open Finance Brasil

    API de informações de operações de Renda Variável Open Finance Brasil – Fase 4.  API que retorna informações de operações de investimento do tipo Renda Variável mantidas nas instituições transmissoras por seus clientes, incluindo dados como informações do produto, quantidade, saldos em posição do cliente, movimentações financeiras e detalhes da nota de negociação.  Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints.  A granularidade de exposição de operações de renda variável se dá por cada ativo (ticker) da carteira do cliente.  Compartilhamento considera lote padrão e fracionário, entretanto, no Open Finance Brasil, as informações são consolidadas via ticker do lote padrão.  A defasagem em relação ao canal eletrônico da instituição deve ser o fechamento (pregão) do dia anterior (d-1).   Em relação ao aluguel de ações: neste momento não faz parte do escopo de compartilhamento a carteira/posição de aluguel do cliente (ativos alugados e movimentações relacionadas a esses ativos).  Apenas deve ser compartilhado as transações de pagamento ou recebimento de juros oriundos dos contratos de ações alugadas (ou doadas) pelos clientes.  Segue abaixo tabela com o escopo de produtos a ser considerado para compartilhamento:  ```    |----------------------|-------------------------------|----------------------|-----------------------------------|    | CLASSE DE ATIVOS     | PRODUTO                       | SUBPRODUTO           | DENOMINAÇÃO                       |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de Investimentos       |     -                | FIAGRO                            |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Ações                         | Subscrição           | Bonus / Direito / Recibo          |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de Investimentos       | Fundo imobiliario    | FII                               |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Ações                         | À vista              | ON / PN / UNIT                    |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF                  | ETF de Renda Variável             |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF                  | ETF Internacional                 |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF Renda Fixa       | ETF Renda Fixa                    |    |----------------------|-------------------------------|----------------------|-----------------------------------|    ```   # noqa: E501

    OpenAPI spec version: 1.0.0-rc3.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MetaOnlyRequestDateTime(object):
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
        'request_date_time': 'datetime'
    }

    attribute_map = {
        'request_date_time': 'requestDateTime'
    }

    def __init__(self, request_date_time=None):  # noqa: E501
        """MetaOnlyRequestDateTime - a model defined in Swagger"""  # noqa: E501
        self._request_date_time = None
        self.discriminator = None
        self.request_date_time = request_date_time

    @property
    def request_date_time(self):
        """Gets the request_date_time of this MetaOnlyRequestDateTime.  # noqa: E501

        Data e hora da consulta, conforme especificação RFC-3339, formato UTC.  # noqa: E501

        :return: The request_date_time of this MetaOnlyRequestDateTime.  # noqa: E501
        :rtype: datetime
        """
        return self._request_date_time

    @request_date_time.setter
    def request_date_time(self, request_date_time):
        """Sets the request_date_time of this MetaOnlyRequestDateTime.

        Data e hora da consulta, conforme especificação RFC-3339, formato UTC.  # noqa: E501

        :param request_date_time: The request_date_time of this MetaOnlyRequestDateTime.  # noqa: E501
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
        if issubclass(MetaOnlyRequestDateTime, dict):
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
        if not isinstance(other, MetaOnlyRequestDateTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
