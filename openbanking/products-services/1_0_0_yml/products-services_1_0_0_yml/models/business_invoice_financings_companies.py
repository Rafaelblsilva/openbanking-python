# coding: utf-8

"""
    API's OpenData do Open Banking Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from products-services_1_0_0_yml.models.cnpj import CNPJ  # noqa: F401,E501

class BusinessInvoiceFinancingsCompanies(CNPJ):
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
        'url_complementary_list': 'str',
        'business_invoice_financings': 'list[BusinessInvoiceFinancings]'
    }
    if hasattr(CNPJ, "swagger_types"):
        swagger_types.update(CNPJ.swagger_types)

    attribute_map = {
        'name': 'name',
        'url_complementary_list': 'urlComplementaryList',
        'business_invoice_financings': 'businessInvoiceFinancings'
    }
    if hasattr(CNPJ, "attribute_map"):
        attribute_map.update(CNPJ.attribute_map)

    def __init__(self, name=None, url_complementary_list=None, business_invoice_financings=None, *args, **kwargs):  # noqa: E501
        """BusinessInvoiceFinancingsCompanies - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._url_complementary_list = None
        self._business_invoice_financings = None
        self.discriminator = None
        self.name = name
        if url_complementary_list is not None:
            self.url_complementary_list = url_complementary_list
        self.business_invoice_financings = business_invoice_financings
        CNPJ.__init__(self, *args, **kwargs)

    @property
    def name(self):
        """Gets the name of this BusinessInvoiceFinancingsCompanies.  # noqa: E501

        Nome da Instituição, pertencente à marca, responsável pela comercialização das modalidades de Direitos Creditórios Descontados para Pessoas Jurídicas consultadas. p.ex.'Empresa da Organização A'  # noqa: E501

        :return: The name of this BusinessInvoiceFinancingsCompanies.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BusinessInvoiceFinancingsCompanies.

        Nome da Instituição, pertencente à marca, responsável pela comercialização das modalidades de Direitos Creditórios Descontados para Pessoas Jurídicas consultadas. p.ex.'Empresa da Organização A'  # noqa: E501

        :param name: The name of this BusinessInvoiceFinancingsCompanies.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def url_complementary_list(self):
        """Gets the url_complementary_list of this BusinessInvoiceFinancingsCompanies.  # noqa: E501

        URL do link que conterá a lista complementar com os nomes e CNPJs agrupados sob o mesmo cnpjNumber. Os contidos nessa lista possuem as mesmas características para produtos e serviços. Endereço eletrônico de acesso ao canal. URLs são limitadas a 2048 caracteres mas, para o contexto do Sistema Financeiro aberto, será adotado a metade deste tamanho. Ex. 'https://example.com/mobile-banking'   # noqa: E501

        :return: The url_complementary_list of this BusinessInvoiceFinancingsCompanies.  # noqa: E501
        :rtype: str
        """
        return self._url_complementary_list

    @url_complementary_list.setter
    def url_complementary_list(self, url_complementary_list):
        """Sets the url_complementary_list of this BusinessInvoiceFinancingsCompanies.

        URL do link que conterá a lista complementar com os nomes e CNPJs agrupados sob o mesmo cnpjNumber. Os contidos nessa lista possuem as mesmas características para produtos e serviços. Endereço eletrônico de acesso ao canal. URLs são limitadas a 2048 caracteres mas, para o contexto do Sistema Financeiro aberto, será adotado a metade deste tamanho. Ex. 'https://example.com/mobile-banking'   # noqa: E501

        :param url_complementary_list: The url_complementary_list of this BusinessInvoiceFinancingsCompanies.  # noqa: E501
        :type: str
        """

        self._url_complementary_list = url_complementary_list

    @property
    def business_invoice_financings(self):
        """Gets the business_invoice_financings of this BusinessInvoiceFinancingsCompanies.  # noqa: E501

        Lista de adiantamento de recebíveis  # noqa: E501

        :return: The business_invoice_financings of this BusinessInvoiceFinancingsCompanies.  # noqa: E501
        :rtype: list[BusinessInvoiceFinancings]
        """
        return self._business_invoice_financings

    @business_invoice_financings.setter
    def business_invoice_financings(self, business_invoice_financings):
        """Sets the business_invoice_financings of this BusinessInvoiceFinancingsCompanies.

        Lista de adiantamento de recebíveis  # noqa: E501

        :param business_invoice_financings: The business_invoice_financings of this BusinessInvoiceFinancingsCompanies.  # noqa: E501
        :type: list[BusinessInvoiceFinancings]
        """
        if business_invoice_financings is None:
            raise ValueError("Invalid value for `business_invoice_financings`, must not be `None`")  # noqa: E501

        self._business_invoice_financings = business_invoice_financings

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
        if issubclass(BusinessInvoiceFinancingsCompanies, dict):
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
        if not isinstance(other, BusinessInvoiceFinancingsCompanies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
