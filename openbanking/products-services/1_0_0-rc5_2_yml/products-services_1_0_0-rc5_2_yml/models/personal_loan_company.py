# coding: utf-8

"""
    API's OpenData do Open Banking Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-rc5.2
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from products-services_1_0_0-rc5_2_yml.models.cnpj import CNPJ  # noqa: F401,E501

class PersonalLoanCompany(CNPJ):
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
        'personal_loans': 'list[PersonalLoan]'
    }
    if hasattr(CNPJ, "swagger_types"):
        swagger_types.update(CNPJ.swagger_types)

    attribute_map = {
        'name': 'name',
        'url_complementary_list': 'urlComplementaryList',
        'personal_loans': 'personalLoans'
    }
    if hasattr(CNPJ, "attribute_map"):
        attribute_map.update(CNPJ.attribute_map)

    def __init__(self, name=None, url_complementary_list=None, personal_loans=None, *args, **kwargs):  # noqa: E501
        """PersonalLoanCompany - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._url_complementary_list = None
        self._personal_loans = None
        self.discriminator = None
        self.name = name
        if url_complementary_list is not None:
            self.url_complementary_list = url_complementary_list
        self.personal_loans = personal_loans
        CNPJ.__init__(self, *args, **kwargs)

    @property
    def name(self):
        """Gets the name of this PersonalLoanCompany.  # noqa: E501

        Nome da Instituição, pertencente à marca, responsável pela comercialização dos produtos e serviços  # noqa: E501

        :return: The name of this PersonalLoanCompany.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PersonalLoanCompany.

        Nome da Instituição, pertencente à marca, responsável pela comercialização dos produtos e serviços  # noqa: E501

        :param name: The name of this PersonalLoanCompany.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def url_complementary_list(self):
        """Gets the url_complementary_list of this PersonalLoanCompany.  # noqa: E501

        URL do link que conterá a lista complementar com os nomes e CNPJs agrupados sob o mesmo cnpjNumber. Os contidos nessa lista possuem as mesmas características para produtos e serviços. Endereço eletrônico de acesso ao canal.  # noqa: E501

        :return: The url_complementary_list of this PersonalLoanCompany.  # noqa: E501
        :rtype: str
        """
        return self._url_complementary_list

    @url_complementary_list.setter
    def url_complementary_list(self, url_complementary_list):
        """Sets the url_complementary_list of this PersonalLoanCompany.

        URL do link que conterá a lista complementar com os nomes e CNPJs agrupados sob o mesmo cnpjNumber. Os contidos nessa lista possuem as mesmas características para produtos e serviços. Endereço eletrônico de acesso ao canal.  # noqa: E501

        :param url_complementary_list: The url_complementary_list of this PersonalLoanCompany.  # noqa: E501
        :type: str
        """

        self._url_complementary_list = url_complementary_list

    @property
    def personal_loans(self):
        """Gets the personal_loans of this PersonalLoanCompany.  # noqa: E501

        Lista de modalidades de empréstimos  # noqa: E501

        :return: The personal_loans of this PersonalLoanCompany.  # noqa: E501
        :rtype: list[PersonalLoan]
        """
        return self._personal_loans

    @personal_loans.setter
    def personal_loans(self, personal_loans):
        """Sets the personal_loans of this PersonalLoanCompany.

        Lista de modalidades de empréstimos  # noqa: E501

        :param personal_loans: The personal_loans of this PersonalLoanCompany.  # noqa: E501
        :type: list[PersonalLoan]
        """
        if personal_loans is None:
            raise ValueError("Invalid value for `personal_loans`, must not be `None`")  # noqa: E501

        self._personal_loans = personal_loans

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
        if issubclass(PersonalLoanCompany, dict):
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
        if not isinstance(other, PersonalLoanCompany):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
