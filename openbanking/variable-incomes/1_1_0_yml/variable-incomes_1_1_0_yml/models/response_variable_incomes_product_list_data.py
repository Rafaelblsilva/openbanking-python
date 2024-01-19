# coding: utf-8

"""
    API Variable Incomes - Open Finance Brasil

    API de informações de operações de Renda Variável Open Finance Brasil – Fase 4.  API que retorna informações de operações de investimento do tipo Renda Variável mantidas nas instituições transmissoras por seus clientes, incluindo dados como informações do produto, quantidade, saldos em posição do cliente, movimentações financeiras e detalhes da nota de negociação.  Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints.  A granularidade de exposição de operações de renda variável se dá por cada ativo (ticker) da carteira do cliente.  Compartilhamento considera lote padrão e fracionário, entretanto, no Open Finance Brasil, as informações são consolidadas via ticker do lote padrão.  A defasagem em relação ao canal eletrônico da instituição deve ser o fechamento (pregão) do dia anterior (d-1).   Em relação ao aluguel de ações: neste momento não faz parte do escopo de compartilhamento a carteira/posição de aluguel do cliente (ativos alugados e movimentações relacionadas a esses ativos).  Apenas deve ser compartilhado as transações de pagamento ou recebimento de juros oriundos dos contratos de ações alugadas (ou doadas) pelos clientes.  Para o identificador do investimento (investmentId) deve ser adotado o seguinte comportamento:  - Após 12 meses sem movimentações e com quantidade de ativos zerada, o resourceId correspondente ao investmentId em questão deve passar ao status UNAVAILABLE (considerando consentimento válido);  - Nas situações em que o cliente compre novamente o ativo após um período de 12 meses sem movimentação e com quantidade de ativos zerada, o mesmo identificador (investmentId) deve ser utilizado. Especificamente para tais produtos, o status do recurso na resources deve passar de UNAVAILABLE para AVAILABLE.  Segue abaixo tabela com o escopo de produtos a ser considerado para compartilhamento:  ```    |----------------------|-------------------------------|----------------------|-----------------------------------|    | CLASSE DE ATIVOS     | PRODUTO                       | SUBPRODUTO           | DENOMINAÇÃO                       |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de Investimentos       |     -                | FIAGRO                            |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Ações                         | Subscrição           | Bonus / Direito / Recibo          |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de Investimentos       | Fundo imobiliario    | FII                               |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Ações                         | À vista              | ON / PN / UNIT                    |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF                  | ETF de Renda Variável             |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF                  | ETF Internacional                 |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF Renda Fixa       | ETF Renda Fixa                    |    |----------------------|-------------------------------|----------------------|-----------------------------------|    ```   # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponseVariableIncomesProductListData(object):
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
        'brand_name': 'str',
        'company_cnpj': 'str',
        'investment_id': 'str'
    }

    attribute_map = {
        'brand_name': 'brandName',
        'company_cnpj': 'companyCnpj',
        'investment_id': 'investmentId'
    }

    def __init__(self, brand_name=None, company_cnpj=None, investment_id=None):  # noqa: E501
        """ResponseVariableIncomesProductListData - a model defined in Swagger"""  # noqa: E501
        self._brand_name = None
        self._company_cnpj = None
        self._investment_id = None
        self.discriminator = None
        self.brand_name = brand_name
        self.company_cnpj = company_cnpj
        self.investment_id = investment_id

    @property
    def brand_name(self):
        """Gets the brand_name of this ResponseVariableIncomesProductListData.  # noqa: E501

        Nome da Marca reportada pelo participante no Open Finance. Recomenda-se utilizar, sempre que possível, o mesmo nome de marca atribuído no campo do diretório Customer Friendly Server Name (Authorisation Server).  # noqa: E501

        :return: The brand_name of this ResponseVariableIncomesProductListData.  # noqa: E501
        :rtype: str
        """
        return self._brand_name

    @brand_name.setter
    def brand_name(self, brand_name):
        """Sets the brand_name of this ResponseVariableIncomesProductListData.

        Nome da Marca reportada pelo participante no Open Finance. Recomenda-se utilizar, sempre que possível, o mesmo nome de marca atribuído no campo do diretório Customer Friendly Server Name (Authorisation Server).  # noqa: E501

        :param brand_name: The brand_name of this ResponseVariableIncomesProductListData.  # noqa: E501
        :type: str
        """
        if brand_name is None:
            raise ValueError("Invalid value for `brand_name`, must not be `None`")  # noqa: E501

        self._brand_name = brand_name

    @property
    def company_cnpj(self):
        """Gets the company_cnpj of this ResponseVariableIncomesProductListData.  # noqa: E501

        Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica. Deve-se ter apenas os números do CNPJ, sem máscara.  # noqa: E501

        :return: The company_cnpj of this ResponseVariableIncomesProductListData.  # noqa: E501
        :rtype: str
        """
        return self._company_cnpj

    @company_cnpj.setter
    def company_cnpj(self, company_cnpj):
        """Sets the company_cnpj of this ResponseVariableIncomesProductListData.

        Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica. Deve-se ter apenas os números do CNPJ, sem máscara.  # noqa: E501

        :param company_cnpj: The company_cnpj of this ResponseVariableIncomesProductListData.  # noqa: E501
        :type: str
        """
        if company_cnpj is None:
            raise ValueError("Invalid value for `company_cnpj`, must not be `None`")  # noqa: E501

        self._company_cnpj = company_cnpj

    @property
    def investment_id(self):
        """Gets the investment_id of this ResponseVariableIncomesProductListData.  # noqa: E501

        Identifica de forma única o relacionamento do cliente com o produto, mantendo as regras de imutabilidade dentro da instituição transmissora. Nos casos em que o cliente, após completar 12 meses da última movimentação e com quantidade de ativos zerada (cliente não tem mais posse do produto sob custódia da transmissora), compre novamente o ativo que já investiu em períodos passados, manter o mesmo investmentId anteriormente utilizado.  # noqa: E501

        :return: The investment_id of this ResponseVariableIncomesProductListData.  # noqa: E501
        :rtype: str
        """
        return self._investment_id

    @investment_id.setter
    def investment_id(self, investment_id):
        """Sets the investment_id of this ResponseVariableIncomesProductListData.

        Identifica de forma única o relacionamento do cliente com o produto, mantendo as regras de imutabilidade dentro da instituição transmissora. Nos casos em que o cliente, após completar 12 meses da última movimentação e com quantidade de ativos zerada (cliente não tem mais posse do produto sob custódia da transmissora), compre novamente o ativo que já investiu em períodos passados, manter o mesmo investmentId anteriormente utilizado.  # noqa: E501

        :param investment_id: The investment_id of this ResponseVariableIncomesProductListData.  # noqa: E501
        :type: str
        """
        if investment_id is None:
            raise ValueError("Invalid value for `investment_id`, must not be `None`")  # noqa: E501

        self._investment_id = investment_id

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
        if issubclass(ResponseVariableIncomesProductListData, dict):
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
        if not isinstance(other, ResponseVariableIncomesProductListData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
