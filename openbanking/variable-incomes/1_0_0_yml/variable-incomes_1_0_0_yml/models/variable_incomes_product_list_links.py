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

class VariableIncomesProductListLinks(object):
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
        '_self': 'str',
        'first': 'str',
        'prev': 'str',
        'next': 'str',
        'last': 'str'
    }

    attribute_map = {
        '_self': 'self',
        'first': 'first',
        'prev': 'prev',
        'next': 'next',
        'last': 'last'
    }

    def __init__(self, _self=None, first=None, prev=None, next=None, last=None):  # noqa: E501
        """VariableIncomesProductListLinks - a model defined in Swagger"""  # noqa: E501
        self.__self = None
        self._first = None
        self._prev = None
        self._next = None
        self._last = None
        self.discriminator = None
        self._self = _self
        if first is not None:
            self.first = first
        if prev is not None:
            self.prev = prev
        if next is not None:
            self.next = next
        if last is not None:
            self.last = last

    @property
    def _self(self):
        """Gets the _self of this VariableIncomesProductListLinks.  # noqa: E501

        URI completo que gerou a resposta atual.  # noqa: E501

        :return: The _self of this VariableIncomesProductListLinks.  # noqa: E501
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this VariableIncomesProductListLinks.

        URI completo que gerou a resposta atual.  # noqa: E501

        :param _self: The _self of this VariableIncomesProductListLinks.  # noqa: E501
        :type: str
        """
        if _self is None:
            raise ValueError("Invalid value for `_self`, must not be `None`")  # noqa: E501

        self.__self = _self

    @property
    def first(self):
        """Gets the first of this VariableIncomesProductListLinks.  # noqa: E501

        URI da primeira página que originou essa lista de resultados. Restrição - Obrigatório quando não for a primeira página da resposta  # noqa: E501

        :return: The first of this VariableIncomesProductListLinks.  # noqa: E501
        :rtype: str
        """
        return self._first

    @first.setter
    def first(self, first):
        """Sets the first of this VariableIncomesProductListLinks.

        URI da primeira página que originou essa lista de resultados. Restrição - Obrigatório quando não for a primeira página da resposta  # noqa: E501

        :param first: The first of this VariableIncomesProductListLinks.  # noqa: E501
        :type: str
        """

        self._first = first

    @property
    def prev(self):
        """Gets the prev of this VariableIncomesProductListLinks.  # noqa: E501

        URI da página anterior dessa lista de resultados. Restrição -  Obrigatório quando não for a primeira página da resposta  # noqa: E501

        :return: The prev of this VariableIncomesProductListLinks.  # noqa: E501
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this VariableIncomesProductListLinks.

        URI da página anterior dessa lista de resultados. Restrição -  Obrigatório quando não for a primeira página da resposta  # noqa: E501

        :param prev: The prev of this VariableIncomesProductListLinks.  # noqa: E501
        :type: str
        """

        self._prev = prev

    @property
    def next(self):
        """Gets the next of this VariableIncomesProductListLinks.  # noqa: E501

        URI da próxima página dessa lista de resultados. Restrição - Obrigatório quando não for a última página da resposta  # noqa: E501

        :return: The next of this VariableIncomesProductListLinks.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this VariableIncomesProductListLinks.

        URI da próxima página dessa lista de resultados. Restrição - Obrigatório quando não for a última página da resposta  # noqa: E501

        :param next: The next of this VariableIncomesProductListLinks.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def last(self):
        """Gets the last of this VariableIncomesProductListLinks.  # noqa: E501

        URI da última página dessa lista de resultados. Restrição - Obrigatório quando não for a última página da resposta.  # noqa: E501

        :return: The last of this VariableIncomesProductListLinks.  # noqa: E501
        :rtype: str
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this VariableIncomesProductListLinks.

        URI da última página dessa lista de resultados. Restrição - Obrigatório quando não for a última página da resposta.  # noqa: E501

        :param last: The last of this VariableIncomesProductListLinks.  # noqa: E501
        :type: str
        """

        self._last = last

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
        if issubclass(VariableIncomesProductListLinks, dict):
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
        if not isinstance(other, VariableIncomesProductListLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
