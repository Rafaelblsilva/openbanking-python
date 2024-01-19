# coding: utf-8

"""
    API OpenData Accounts do Open Finance Brasil

    A API descrita neste documento é referente as API Accounts da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-beta.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PersonalDataParticipant(object):
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
        'brand': 'str',
        'name': 'str',
        'cnpj_number': 'str',
        'url_complementary_list': 'str'
    }

    attribute_map = {
        'brand': 'brand',
        'name': 'name',
        'cnpj_number': 'cnpjNumber',
        'url_complementary_list': 'urlComplementaryList'
    }

    def __init__(self, brand=None, name=None, cnpj_number=None, url_complementary_list=None):  # noqa: E501
        """PersonalDataParticipant - a model defined in Swagger"""  # noqa: E501
        self._brand = None
        self._name = None
        self._cnpj_number = None
        self._url_complementary_list = None
        self.discriminator = None
        self.brand = brand
        self.name = name
        self.cnpj_number = cnpj_number
        if url_complementary_list is not None:
            self.url_complementary_list = url_complementary_list

    @property
    def brand(self):
        """Gets the brand of this PersonalDataParticipant.  # noqa: E501

        Nome da Marca reportada pelo participante do Open Finance. O conceito a que se refere a 'marca' é em essência uma promessa da empresa em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes  # noqa: E501

        :return: The brand of this PersonalDataParticipant.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this PersonalDataParticipant.

        Nome da Marca reportada pelo participante do Open Finance. O conceito a que se refere a 'marca' é em essência uma promessa da empresa em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes  # noqa: E501

        :param brand: The brand of this PersonalDataParticipant.  # noqa: E501
        :type: str
        """
        if brand is None:
            raise ValueError("Invalid value for `brand`, must not be `None`")  # noqa: E501

        self._brand = brand

    @property
    def name(self):
        """Gets the name of this PersonalDataParticipant.  # noqa: E501

        Nome da Instituição, pertencente à marca, responsável pela modalidade de Empréstimos. p.ex.'Empresa da Organização A'  # noqa: E501

        :return: The name of this PersonalDataParticipant.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PersonalDataParticipant.

        Nome da Instituição, pertencente à marca, responsável pela modalidade de Empréstimos. p.ex.'Empresa da Organização A'  # noqa: E501

        :param name: The name of this PersonalDataParticipant.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def cnpj_number(self):
        """Gets the cnpj_number of this PersonalDataParticipant.  # noqa: E501

        CNPJ  # noqa: E501

        :return: The cnpj_number of this PersonalDataParticipant.  # noqa: E501
        :rtype: str
        """
        return self._cnpj_number

    @cnpj_number.setter
    def cnpj_number(self, cnpj_number):
        """Sets the cnpj_number of this PersonalDataParticipant.

        CNPJ  # noqa: E501

        :param cnpj_number: The cnpj_number of this PersonalDataParticipant.  # noqa: E501
        :type: str
        """
        if cnpj_number is None:
            raise ValueError("Invalid value for `cnpj_number`, must not be `None`")  # noqa: E501

        self._cnpj_number = cnpj_number

    @property
    def url_complementary_list(self):
        """Gets the url_complementary_list of this PersonalDataParticipant.  # noqa: E501

        URL do link que conterá a lista complementar com os nomes e CNPJs agrupados sob o mesmo cnpjNumber. Os contidos nessa lista possuem as mesmas características para produtos e serviços. Endereço eletrônico de acesso ao canal. Será obrigatoriamente preenchido se houver lista complementar com os nomes e CNPJs a ser disponibilizada. Restrição: Será obrigatorimente preenchido se houver lista complementar com os nomes e CNPJs a ser disponibilizada   # noqa: E501

        :return: The url_complementary_list of this PersonalDataParticipant.  # noqa: E501
        :rtype: str
        """
        return self._url_complementary_list

    @url_complementary_list.setter
    def url_complementary_list(self, url_complementary_list):
        """Sets the url_complementary_list of this PersonalDataParticipant.

        URL do link que conterá a lista complementar com os nomes e CNPJs agrupados sob o mesmo cnpjNumber. Os contidos nessa lista possuem as mesmas características para produtos e serviços. Endereço eletrônico de acesso ao canal. Será obrigatoriamente preenchido se houver lista complementar com os nomes e CNPJs a ser disponibilizada. Restrição: Será obrigatorimente preenchido se houver lista complementar com os nomes e CNPJs a ser disponibilizada   # noqa: E501

        :param url_complementary_list: The url_complementary_list of this PersonalDataParticipant.  # noqa: E501
        :type: str
        """

        self._url_complementary_list = url_complementary_list

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
        if issubclass(PersonalDataParticipant, dict):
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
        if not isinstance(other, PersonalDataParticipant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
