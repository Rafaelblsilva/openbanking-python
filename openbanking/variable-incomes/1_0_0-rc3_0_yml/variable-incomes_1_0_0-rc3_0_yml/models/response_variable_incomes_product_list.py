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

class ResponseVariableIncomesProductList(object):
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
        'data': 'list[ResponseVariableIncomesProductListData]',
        'links': 'VariableIncomesLinks',
        'meta': 'VariableIncomesMeta'
    }

    attribute_map = {
        'data': 'data',
        'links': 'links',
        'meta': 'meta'
    }

    def __init__(self, data=None, links=None, meta=None):  # noqa: E501
        """ResponseVariableIncomesProductList - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._links = None
        self._meta = None
        self.discriminator = None
        self.data = data
        self.links = links
        self.meta = meta

    @property
    def data(self):
        """Gets the data of this ResponseVariableIncomesProductList.  # noqa: E501


        :return: The data of this ResponseVariableIncomesProductList.  # noqa: E501
        :rtype: list[ResponseVariableIncomesProductListData]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ResponseVariableIncomesProductList.


        :param data: The data of this ResponseVariableIncomesProductList.  # noqa: E501
        :type: list[ResponseVariableIncomesProductListData]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def links(self):
        """Gets the links of this ResponseVariableIncomesProductList.  # noqa: E501


        :return: The links of this ResponseVariableIncomesProductList.  # noqa: E501
        :rtype: VariableIncomesLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ResponseVariableIncomesProductList.


        :param links: The links of this ResponseVariableIncomesProductList.  # noqa: E501
        :type: VariableIncomesLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def meta(self):
        """Gets the meta of this ResponseVariableIncomesProductList.  # noqa: E501


        :return: The meta of this ResponseVariableIncomesProductList.  # noqa: E501
        :rtype: VariableIncomesMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ResponseVariableIncomesProductList.


        :param meta: The meta of this ResponseVariableIncomesProductList.  # noqa: E501
        :type: VariableIncomesMeta
        """
        if meta is None:
            raise ValueError("Invalid value for `meta`, must not be `None`")  # noqa: E501

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
        if issubclass(ResponseVariableIncomesProductList, dict):
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
        if not isinstance(other, ResponseVariableIncomesProductList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
