# coding: utf-8

"""
    API Exchanges - Open Finance Brasil

    API de informações de operações de Câmbio Open Finance Brasil – Fase 4.  API que retorna informações de operações de Câmbio realizadas nas instituições transmissoras por seus clientes, incluindo dados como informações da operação contratada, valor da operação em moeda nacional e moeda estrangeira, classificação da operação, forma de entrega, VET e, quando aplicável, valor a liquidar.  Também serão compartilhados os eventos de alteração da operação, caso existam, com as informações modificadas.  Não possui segregação entre pessoa natural e pessoa jurídica.  Requer consentimento do cliente para todos os endpoints.  __São escopo de compartilhamento as operações de compra e venda de moeda estrangeira de liquidação pronta ou futura, inclusive com adiantamento.  Operações de câmbio anuladas não são escopo de exposição, bem como eventos de vinculação de operações.  A exposição se dará por cada operação de câmbio contratada pelo cliente.__   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProductList(object):
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
        'operation_id': 'str'
    }

    attribute_map = {
        'brand_name': 'brandName',
        'company_cnpj': 'companyCnpj',
        'operation_id': 'operationId'
    }

    def __init__(self, brand_name=None, company_cnpj=None, operation_id=None):  # noqa: E501
        """ProductList - a model defined in Swagger"""  # noqa: E501
        self._brand_name = None
        self._company_cnpj = None
        self._operation_id = None
        self.discriminator = None
        self.brand_name = brand_name
        self.company_cnpj = company_cnpj
        self.operation_id = operation_id

    @property
    def brand_name(self):
        """Gets the brand_name of this ProductList.  # noqa: E501

        Nome da Marca reportada pelo participante no Open Finance. Recomenda-se utilizar, sempre que possível, o mesmo nome de marca atribuído no campo do diretório Customer Friendly Server Name (Authorisation Server). Instituição autorizada a operar  # noqa: E501

        :return: The brand_name of this ProductList.  # noqa: E501
        :rtype: str
        """
        return self._brand_name

    @brand_name.setter
    def brand_name(self, brand_name):
        """Sets the brand_name of this ProductList.

        Nome da Marca reportada pelo participante no Open Finance. Recomenda-se utilizar, sempre que possível, o mesmo nome de marca atribuído no campo do diretório Customer Friendly Server Name (Authorisation Server). Instituição autorizada a operar  # noqa: E501

        :param brand_name: The brand_name of this ProductList.  # noqa: E501
        :type: str
        """
        if brand_name is None:
            raise ValueError("Invalid value for `brand_name`, must not be `None`")  # noqa: E501

        self._brand_name = brand_name

    @property
    def company_cnpj(self):
        """Gets the company_cnpj of this ProductList.  # noqa: E501

        Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica. Deve-se ter apenas os números do CNPJ, sem máscara.  # noqa: E501

        :return: The company_cnpj of this ProductList.  # noqa: E501
        :rtype: str
        """
        return self._company_cnpj

    @company_cnpj.setter
    def company_cnpj(self, company_cnpj):
        """Sets the company_cnpj of this ProductList.

        Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica. Deve-se ter apenas os números do CNPJ, sem máscara.  # noqa: E501

        :param company_cnpj: The company_cnpj of this ProductList.  # noqa: E501
        :type: str
        """
        if company_cnpj is None:
            raise ValueError("Invalid value for `company_cnpj`, must not be `None`")  # noqa: E501

        self._company_cnpj = company_cnpj

    @property
    def operation_id(self):
        """Gets the operation_id of this ProductList.  # noqa: E501

        Identifica de forma única  o relacionamento do cliente com o produto, mantendo as regras de imutabilidade dentro da instituição transmissora.  # noqa: E501

        :return: The operation_id of this ProductList.  # noqa: E501
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        """Sets the operation_id of this ProductList.

        Identifica de forma única  o relacionamento do cliente com o produto, mantendo as regras de imutabilidade dentro da instituição transmissora.  # noqa: E501

        :param operation_id: The operation_id of this ProductList.  # noqa: E501
        :type: str
        """
        if operation_id is None:
            raise ValueError("Invalid value for `operation_id`, must not be `None`")  # noqa: E501

        self._operation_id = operation_id

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
        if issubclass(ProductList, dict):
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
        if not isinstance(other, ProductList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
