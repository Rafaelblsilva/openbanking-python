# coding: utf-8

"""
    API Treasure Titles - Open Finance Brasil

    API de informações de operações de Títulos do Tesouro Direto Open Finance Brasil – Fase 4. API que retorna informações de operações de investimento do tipo Títulos do Tesouro Direto mantidas nas instituições transmissoras por seus clientes, incluindo dados como informações do produto, quantidade, saldos em posição do cliente e movimentações financeiras. Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints. Devem ser considerados como escopo de exposição todos os títulos ofertados pelo Tesouro Direto. A exposição se dará por cada operação de títulos do Tesouro Direto contratada pelo cliente.   # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponseTreasureTitlesListProductData(object):
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
        'brand_name': 'TreasureTitlesBrandName',
        'company_cnpj': 'TreasureTitlesCompanyCnpj',
        'investment_id': 'TreasureTitlesInvestmentId'
    }

    attribute_map = {
        'brand_name': 'brandName',
        'company_cnpj': 'companyCnpj',
        'investment_id': 'investmentId'
    }

    def __init__(self, brand_name=None, company_cnpj=None, investment_id=None):  # noqa: E501
        """ResponseTreasureTitlesListProductData - a model defined in Swagger"""  # noqa: E501
        self._brand_name = None
        self._company_cnpj = None
        self._investment_id = None
        self.discriminator = None
        self.brand_name = brand_name
        self.company_cnpj = company_cnpj
        self.investment_id = investment_id

    @property
    def brand_name(self):
        """Gets the brand_name of this ResponseTreasureTitlesListProductData.  # noqa: E501


        :return: The brand_name of this ResponseTreasureTitlesListProductData.  # noqa: E501
        :rtype: TreasureTitlesBrandName
        """
        return self._brand_name

    @brand_name.setter
    def brand_name(self, brand_name):
        """Sets the brand_name of this ResponseTreasureTitlesListProductData.


        :param brand_name: The brand_name of this ResponseTreasureTitlesListProductData.  # noqa: E501
        :type: TreasureTitlesBrandName
        """
        if brand_name is None:
            raise ValueError("Invalid value for `brand_name`, must not be `None`")  # noqa: E501

        self._brand_name = brand_name

    @property
    def company_cnpj(self):
        """Gets the company_cnpj of this ResponseTreasureTitlesListProductData.  # noqa: E501


        :return: The company_cnpj of this ResponseTreasureTitlesListProductData.  # noqa: E501
        :rtype: TreasureTitlesCompanyCnpj
        """
        return self._company_cnpj

    @company_cnpj.setter
    def company_cnpj(self, company_cnpj):
        """Sets the company_cnpj of this ResponseTreasureTitlesListProductData.


        :param company_cnpj: The company_cnpj of this ResponseTreasureTitlesListProductData.  # noqa: E501
        :type: TreasureTitlesCompanyCnpj
        """
        if company_cnpj is None:
            raise ValueError("Invalid value for `company_cnpj`, must not be `None`")  # noqa: E501

        self._company_cnpj = company_cnpj

    @property
    def investment_id(self):
        """Gets the investment_id of this ResponseTreasureTitlesListProductData.  # noqa: E501


        :return: The investment_id of this ResponseTreasureTitlesListProductData.  # noqa: E501
        :rtype: TreasureTitlesInvestmentId
        """
        return self._investment_id

    @investment_id.setter
    def investment_id(self, investment_id):
        """Sets the investment_id of this ResponseTreasureTitlesListProductData.


        :param investment_id: The investment_id of this ResponseTreasureTitlesListProductData.  # noqa: E501
        :type: TreasureTitlesInvestmentId
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
        if issubclass(ResponseTreasureTitlesListProductData, dict):
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
        if not isinstance(other, ResponseTreasureTitlesListProductData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
