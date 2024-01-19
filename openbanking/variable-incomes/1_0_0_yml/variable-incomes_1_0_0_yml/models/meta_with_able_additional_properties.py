# coding: utf-8

"""
    API Variable Incomes - Open Finance Brasil

    API de informações de operações de Renda Variável Open Finance Brasil – Fase 4.  API que retorna informações de operações de investimento do tipo Renda Variável mantidas nas instituições transmissoras por seus clientes, incluindo dados como informações do produto, quantidade, saldos em posição do cliente, movimentações financeiras e detalhes da nota de negociação.  Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints.  A granularidade de exposição de operações de renda variável se dá por cada ativo (ticker) da carteira do cliente.  Compartilhamento considera lote padrão e fracionário, entretanto, no Open Finance Brasil, as informações são consolidadas via ticker do lote padrão.  A defasagem em relação ao canal eletrônico da instituição deve ser o fechamento (pregão) do dia anterior (d-1).   Em relação ao aluguel de ações: neste momento não faz parte do escopo de compartilhamento a carteira/posição de aluguel do cliente (ativos alugados e movimentações relacionadas a esses ativos).  Apenas deve ser compartilhado as transações de pagamento ou recebimento de juros oriundos dos contratos de ações alugadas (ou doadas) pelos clientes.  Para o identificador do investimento (investmentId) deve ser adotado o seguinte comportamento:  - Após 12 meses sem movimentações e com quantidade de ativos zerada, o resourceId correspondente ao investmentId em questão deve passar ao status UNAVAILABLE (considerando consentimento válido);  - Nas situações em que o cliente compre novamente o ativo após um período de 12 meses sem movimentação e com quantidade de ativos zerada, o mesmo identificador (investmentId) deve ser utilizado. Especificamente para tais produtos, o status do recurso na resources deve passar de UNAVAILABLE para AVAILABLE.  Segue abaixo tabela com o escopo de produtos a ser considerado para compartilhamento:  ```    |----------------------|-------------------------------|----------------------|-----------------------------------|    | CLASSE DE ATIVOS     | PRODUTO                       | SUBPRODUTO           | DENOMINAÇÃO                       |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de Investimentos       |     -                | FIAGRO                            |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Ações                         | Subscrição           | Bonus / Direito / Recibo          |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de Investimentos       | Fundo imobiliario    | FII                               |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Ações                         | À vista              | ON / PN / UNIT                    |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF                  | ETF de Renda Variável             |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF                  | ETF Internacional                 |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF Renda Fixa       | ETF Renda Fixa                    |    |----------------------|-------------------------------|----------------------|-----------------------------------|    ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MetaWithAbleAdditionalProperties(object):
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
        """MetaWithAbleAdditionalProperties - a model defined in Swagger"""  # noqa: E501
        self._total_records = None
        self._total_pages = None
        self._request_date_time = None
        self.discriminator = None
        self.total_records = total_records
        self.total_pages = total_pages
        self.request_date_time = request_date_time

    @property
    def total_records(self):
        """Gets the total_records of this MetaWithAbleAdditionalProperties.  # noqa: E501

        Número total de registros no resultado  # noqa: E501

        :return: The total_records of this MetaWithAbleAdditionalProperties.  # noqa: E501
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this MetaWithAbleAdditionalProperties.

        Número total de registros no resultado  # noqa: E501

        :param total_records: The total_records of this MetaWithAbleAdditionalProperties.  # noqa: E501
        :type: int
        """
        if total_records is None:
            raise ValueError("Invalid value for `total_records`, must not be `None`")  # noqa: E501

        self._total_records = total_records

    @property
    def total_pages(self):
        """Gets the total_pages of this MetaWithAbleAdditionalProperties.  # noqa: E501

        Número total de páginas no resultado  # noqa: E501

        :return: The total_pages of this MetaWithAbleAdditionalProperties.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this MetaWithAbleAdditionalProperties.

        Número total de páginas no resultado  # noqa: E501

        :param total_pages: The total_pages of this MetaWithAbleAdditionalProperties.  # noqa: E501
        :type: int
        """
        if total_pages is None:
            raise ValueError("Invalid value for `total_pages`, must not be `None`")  # noqa: E501

        self._total_pages = total_pages

    @property
    def request_date_time(self):
        """Gets the request_date_time of this MetaWithAbleAdditionalProperties.  # noqa: E501

        Data e hora da consulta, conforme especificação RFC-3339, formato UTC.  # noqa: E501

        :return: The request_date_time of this MetaWithAbleAdditionalProperties.  # noqa: E501
        :rtype: datetime
        """
        return self._request_date_time

    @request_date_time.setter
    def request_date_time(self, request_date_time):
        """Sets the request_date_time of this MetaWithAbleAdditionalProperties.

        Data e hora da consulta, conforme especificação RFC-3339, formato UTC.  # noqa: E501

        :param request_date_time: The request_date_time of this MetaWithAbleAdditionalProperties.  # noqa: E501
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
        if issubclass(MetaWithAbleAdditionalProperties, dict):
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
        if not isinstance(other, MetaWithAbleAdditionalProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
