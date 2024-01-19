# coding: utf-8

"""
    API's OpenData do Open Finance Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BusinessAccountsBrand(object):
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
        'companies': 'list[BusinessAccountsCompany]'
    }

    attribute_map = {
        'name': 'name',
        'companies': 'companies'
    }

    def __init__(self, name=None, companies=None):  # noqa: E501
        """BusinessAccountsBrand - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._companies = None
        self.discriminator = None
        self.name = name
        self.companies = companies

    @property
    def name(self):
        """Gets the name of this BusinessAccountsBrand.  # noqa: E501

        Nome da Instituição, pertencente à marca, responsável pela comercialização dos produtos e serviços  # noqa: E501

        :return: The name of this BusinessAccountsBrand.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BusinessAccountsBrand.

        Nome da Instituição, pertencente à marca, responsável pela comercialização dos produtos e serviços  # noqa: E501

        :param name: The name of this BusinessAccountsBrand.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def companies(self):
        """Gets the companies of this BusinessAccountsBrand.  # noqa: E501

        Companies traz uma lista de todas as instituições da Marca  # noqa: E501

        :return: The companies of this BusinessAccountsBrand.  # noqa: E501
        :rtype: list[BusinessAccountsCompany]
        """
        return self._companies

    @companies.setter
    def companies(self, companies):
        """Sets the companies of this BusinessAccountsBrand.

        Companies traz uma lista de todas as instituições da Marca  # noqa: E501

        :param companies: The companies of this BusinessAccountsBrand.  # noqa: E501
        :type: list[BusinessAccountsCompany]
        """
        if companies is None:
            raise ValueError("Invalid value for `companies`, must not be `None`")  # noqa: E501

        self._companies = companies

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
        if issubclass(BusinessAccountsBrand, dict):
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
        if not isinstance(other, BusinessAccountsBrand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
