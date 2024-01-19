# coding: utf-8

"""
    APIs OpenData do Open Banking Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-rc5.1
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from channels_1_0_0-rc5_1_yml.models.cnpj import CNPJ  # noqa: F401,E501

class BranchesCompany(CNPJ):
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
        'cnpj_number': 'str',
        'url_complementary_list': 'str',
        'branches': 'list[Branch]'
    }
    if hasattr(CNPJ, "swagger_types"):
        swagger_types.update(CNPJ.swagger_types)

    attribute_map = {
        'name': 'name',
        'cnpj_number': 'cnpjNumber',
        'url_complementary_list': 'urlComplementaryList',
        'branches': 'branches'
    }
    if hasattr(CNPJ, "attribute_map"):
        attribute_map.update(CNPJ.attribute_map)

    def __init__(self, name=None, cnpj_number=None, url_complementary_list=None, branches=None, *args, **kwargs):  # noqa: E501
        """BranchesCompany - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._cnpj_number = None
        self._url_complementary_list = None
        self._branches = None
        self.discriminator = None
        self.name = name
        self.cnpj_number = cnpj_number
        if url_complementary_list is not None:
            self.url_complementary_list = url_complementary_list
        if branches is not None:
            self.branches = branches
        CNPJ.__init__(self, *args, **kwargs)

    @property
    def name(self):
        """Gets the name of this BranchesCompany.  # noqa: E501


        :return: The name of this BranchesCompany.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BranchesCompany.


        :param name: The name of this BranchesCompany.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def cnpj_number(self):
        """Gets the cnpj_number of this BranchesCompany.  # noqa: E501

        Número completo do CNPJ da instituição responsável pela dependência - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica. Deve-se ter apenas os números do CNPJ, sem máscara   # noqa: E501

        :return: The cnpj_number of this BranchesCompany.  # noqa: E501
        :rtype: str
        """
        return self._cnpj_number

    @cnpj_number.setter
    def cnpj_number(self, cnpj_number):
        """Sets the cnpj_number of this BranchesCompany.

        Número completo do CNPJ da instituição responsável pela dependência - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica. Deve-se ter apenas os números do CNPJ, sem máscara   # noqa: E501

        :param cnpj_number: The cnpj_number of this BranchesCompany.  # noqa: E501
        :type: str
        """
        if cnpj_number is None:
            raise ValueError("Invalid value for `cnpj_number`, must not be `None`")  # noqa: E501

        self._cnpj_number = cnpj_number

    @property
    def url_complementary_list(self):
        """Gets the url_complementary_list of this BranchesCompany.  # noqa: E501


        :return: The url_complementary_list of this BranchesCompany.  # noqa: E501
        :rtype: str
        """
        return self._url_complementary_list

    @url_complementary_list.setter
    def url_complementary_list(self, url_complementary_list):
        """Sets the url_complementary_list of this BranchesCompany.


        :param url_complementary_list: The url_complementary_list of this BranchesCompany.  # noqa: E501
        :type: str
        """

        self._url_complementary_list = url_complementary_list

    @property
    def branches(self):
        """Gets the branches of this BranchesCompany.  # noqa: E501

        Lista de Dependências de uma Instituição  # noqa: E501

        :return: The branches of this BranchesCompany.  # noqa: E501
        :rtype: list[Branch]
        """
        return self._branches

    @branches.setter
    def branches(self, branches):
        """Sets the branches of this BranchesCompany.

        Lista de Dependências de uma Instituição  # noqa: E501

        :param branches: The branches of this BranchesCompany.  # noqa: E501
        :type: list[Branch]
        """

        self._branches = branches

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
        if issubclass(BranchesCompany, dict):
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
        if not isinstance(other, BranchesCompany):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
